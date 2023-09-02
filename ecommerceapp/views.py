from django.shortcuts import render,redirect
from ecommerceapp.models import Contact,Product,OrderUpdate,Orders,Tokens,Rewards,RedeemRewards
from django.contrib import messages
from math import ceil
from ecommerceapp import keys
from django.conf import settings

import json
from django.views.decorators.csrf import  csrf_exempt
from PayTm import Checksum
from django.contrib.auth import get_user_model
User = get_user_model()



# Importing the libraries
import datetime
import hashlib
import json
import requests
from uuid import uuid4
from urllib.parse import urlparse

# Part 1 - Building a Blockchain

class Blockchain:

    def __init__(self):
        self.chain = []
        self.transactions = []
        self.create_block(proof = 1, previous_hash = '0')
        self.nodes = set()
    
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'transactions': self.transactions}
        self.transactions = []
        self.chain.append(block)
        return block
    
    

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True
    
    def add_transaction(self,receiver, amount):
        self.transactions.append({'receiver': receiver,
                                  'amount': amount})
        previous_block = self.get_previous_block()
        # print(self.chain)
        return previous_block['index'] + 1
    
    def add_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)
    
    def replace_chain(self):
        network = self.nodes
        longest_chain = None
        max_length = len(self.chain)
        for node in network:
            response = requests.get(f'http://{node}/get_chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                if length > max_length and self.is_chain_valid(chain):
                    max_length = length
                    longest_chain = chain
        if longest_chain:
            self.chain = longest_chain
            return True
        return False







blockchain = Blockchain()





















# froon_dm django.shortcuts import render
# from web3 import Web3

#    # Connect to a local Ethereum node or provider
# w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

#    # Contract address and ABI
# contract_address = "0xd9145CCE52D386f254917e481eB44e9943F39138"
# contract_abi = [
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "paymentAmount",
# 				"type": "uint256"
# 			}
# 		],
# 		"name": "makePaymentAndReward",
# 		"outputs": [],
# 		"stateMutability": "payable",
# 		"type": "function"
# 	},
# 	{
# 		"anonymous": False,
# 		"inputs": [
# 			{
# 				"indexed": True,
# 				"internalType": "address",
# 				"name": "from",
# 				"type": "address"
# 			},
# 			{
# 				"indexed": False,
# 				"internalType": "uint256",
# 				"name": "amount",
# 				"type": "uint256"
# 			},
# 			{
# 				"indexed": False,
# 				"internalType": "uint256",
# 				"name": "rewardTokens",
# 				"type": "uint256"
# 			}
# 		],
# 		"name": "PaymentReceived",
# 		"type": "event"
# 	},
# 	{
# 		"anonymous": False,
# 		"inputs": [
# 			{
# 				"indexed": True,
# 				"internalType": "address",
# 				"name": "by",
# 				"type": "address"
# 			},
# 			{
# 				"indexed": False,
# 				"internalType": "uint256",
# 				"name": "amount",
# 				"type": "uint256"
# 			}
# 		],
# 		"name": "TokensWithdrawn",
# 		"type": "event"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "amountToWithdraw",
# 				"type": "uint256"
# 			}
# 		],
# 		"name": "withdrawTokens",
# 		"outputs": [],
# 		"stateMutability": "nonpayable",
# 		"type": "function"
# 	},
# 	{
# 		"stateMutability": "payable",
# 		"type": "receive"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "address",
# 				"name": "account",
# 				"type": "address"
# 			}
# 		],
# 		"name": "getBalance",
# 		"outputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "",
# 				"type": "uint256"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	}
# ]  # Your contract ABI

#    # Load the contract
# contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# def record_transaction(amount):
#        # Perform some form handling to get the necessary data
#     # buyer_address = request.POST.get('buyer_address')
#     # seller/_address = request.POST.get('seller_address')
#     # amount = int(request.POST.get('amount'))

#        # Perform the transaction
#     tx_hash = contract.functions.makePaymentAndReward( amount).call()

#     # return render 'transaction_recorded.html', {'tx_hash': tx_hash.hex()})

# def withdraw_Tokens(tokens):
#     transactiata = contract.functions.withdrawTokens(tokens).call()
#     # buyer, seller, amount, timestamp = transaction_data

#     # return render(request, 'transaction_detail.html', {
#     #     'buyer': buyer,
#     #     'seller': seller,
#     #     'amount': amount,
#     #     'timestamp': timestamp
#     # })













# Create your views here.
def index(request):

    allProds = []
    catprods = Product.objects.values('category','id')
    # print(catprods)
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod= Product.objects.filter(category=cat)
        n=len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params= {'allProds':allProds,'class1':'active'}

    return render(request,"index.html",params)

    
def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        desc=request.POST.get("desc")
        pnumber=request.POST.get("pnumber")
        # myquery=Contact(name=name,email=email,desc=desc,phonenumber=pnumber)
        # myquery.save()
        messages.info(request,"we will get back to you soon..")
        return render(request,"contact.html")


    return render(request,"contact.html")

def about(request):
    allProds = []
    catprods = Rewards.objects.values('category','id')
    # print(catprods)
    cats = {item['category'] for item in catprods}
    currentuser=request.user.username
    tokens=Tokens.objects.filter(email=currentuser)
    currentloyalpoint=0
    if len(tokens)==0:
        currentloyalpoint=0
    else:
        currentloyalpoint=tokens[len(tokens)-1].tokens
    for cat in cats:
        prod= Rewards.objects.filter(category=cat)
        n=len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params= {'allProds':allProds,'class2':'active','tokens':currentloyalpoint}
    
    if request.method=="POST":
        name=request.POST.get('name','')
        tokens_spent = request.POST.get('tokens', '')
        # print(tokens_spent)
        currentuser=request.user.username
        # print(currentuser)
        tokens=Tokens.objects.filter(email=currentuser)
        currentloyalpoint=0
        if len(tokens)==0:
            currentloyalpoint=0
        else:
            currentloyalpoint=tokens[len(tokens)-1].tokens
        # loyalpoints=currentloyalpoint+tokenn
        # Token=Tokens(email=currentuser,tokens=loyalpoints)
        # Token.save()
        if currentloyalpoint>=int(tokens_spent):
            context={"name":name,"tokens_spent":tokens_spent}
            return render(request,'confirmredeem.html',context)
        else:
            messages.warning(request,"you have less tokens than required")
            return redirect('/about')
        
        return render(request,'about.html',params)
       
        

    return render(request,"about.html",params)

def redeem(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login & Try Again")
        return redirect('/auth/login')
    currentuser=request.user.username
    name=request.POST.get('name','')
    tokens_spent = request.POST.get('tokens', '')
    tokens=Tokens.objects.filter(email=currentuser)
    currentloyalpoint=tokens[len(tokens)-1].tokens
    loyalpoints=currentloyalpoint-int(tokens_spent)
    Token=Tokens(email=currentuser,tokens=loyalpoints)
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    blockchain.add_transaction(currentuser, tokens_spent)
    block = blockchain.create_block(proof, previous_hash)
    hash=blockchain.hash(block)
    print(blockchain.chain)
    Token=Tokens(email=currentuser,tokens=loyalpoints,hash=hash)
    Token.save()
    Redeemrewards=RedeemRewards(product_name=name,hash=hash,email=currentuser,tokens=tokens_spent)
    Redeemrewards.save()
    context={"name":name,"tokens_spent":tokens_spent}
    return render(request,'redeem.html',context)


def confirmredeem(request):
    return render(request,'confirmredeem.html')
    
def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login & Try Again")
        return redirect('/auth/login')

    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amt')
        email = request.POST.get('email', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2','')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        Order = Orders(items_json=items_json,name=name,amount=amount, email=email, 
                       address1=address1,address2=address2,city=city,state=state,
                       zip_code=zip_code,phone=phone)
        Order.save()
        update = OrderUpdate(order_id=Order.order_id,update_desc="the order has been placed")
        update.save()
        thank = True
        id = Order.order_id
        oid=str(id)+"ShopyCart"
        Order=Orders(oid=oid)

        tokenn=(int(amount))/50
        currentuser=request.user.username
        
        tokens=Tokens.objects.filter(email=currentuser)
        currentloyalpoint=0
        if len(tokens)==0:
            currentloyalpoint=0
        else:
            currentloyalpoint=tokens[len(tokens)-1].tokens
        loyalpoints=currentloyalpoint+tokenn
        
        previous_block = blockchain.get_previous_block()
        previous_proof = previous_block['proof']
        proof = blockchain.proof_of_work(previous_proof)
        previous_hash = blockchain.hash(previous_block) 
        blockchain.add_transaction(currentuser, tokenn)
        block = blockchain.create_block(proof, previous_hash)
        hash=str(blockchain.hash(block))
        print(blockchain.chain)
        Token=Tokens(email=currentuser,tokens=loyalpoints,hash=hash)
        Token.save()
        
        response_dict = {
            'ORDER_ID': oid,
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'token': (int(amount))/50,
        }
        form = request.POST
        return render(request, 'paymentstatus.html', {'response': response_dict})
    params= {'class3':'active'}
    return render(request, 'checkout.html',params)


def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login & Try Again")
        return redirect('/auth/login')
    

    return render(request,"profile.html")

def orders(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login & Try Again")
        return redirect('/auth/login')
    
    currentuser=request.user.username
    print(currentuser)
    items=Orders.objects.filter(email=currentuser)
    # print(items)
    if items.count()==0:
        
        return render(request,'emptyprofile.html')
    rid=""
    for i in items:
        # print(i.order_id)
        # print(i.order_id)
        myid=i.order_id
        rid=myid
        # print(rid)
    status=OrderUpdate.objects.filter(order_id=int(rid))
    # print("this is status     ")
    # print(status)
    # for j in status:
        # print(j.update_desc)

   
    context ={"items":items,"status":status,"class4":'active'} 
    return render(request,"orderhistory.html",context)

def rewards(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login & Try Again")
        return redirect('/auth/login')
    
    currentuser=request.user.username
    # print(currentuser)
    items=RedeemRewards.objects.filter(email=currentuser)
    # print(items)
    if items.count()==0:
        
        return render(request,'emptyrewards.html')
    rid=""
    # for i in items:
    #     print(i.order_id)
    #     # print(i.order_id)
    #     myid=i.order_id
    #     rid=myid
    #     # print(rid)
    # # status=OrderUpdate.objects.filter(order_id=int(rid))
    # print("this is status     ")
    # print(status)
    # for j in status:
    #     print(j.update_desc)

   
    context ={"items":items,"class4":'active'}
    
    # # print(currentuser)
    # params= {'allProds':allProds,'class':'active'}
    return render(request,"rewardshistory.html",context)

def tokens(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login & Try Again")
        return redirect('/auth/login')
    
    currentuser=request.user.username
    token=Tokens.objects.filter(email=currentuser)

    if token.count()==0:
        return render(request,'emptytokens.html')
    
    totaltokens=token[len(token)-1].tokens
   
    context ={"items":token,"total_tokens":totaltokens,"class5":'active'} 
    return render(request,"tokens.html",context)
