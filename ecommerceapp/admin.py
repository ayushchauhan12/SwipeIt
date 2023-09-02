from django.contrib import admin
from ecommerceapp.models import  Contact,Product,Orders,OrderUpdate,Tokens,Rewards,RedeemRewards
# Register your models here.
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
admin.site.register(Tokens)
admin.site.register(Rewards)
admin.site.register(RedeemRewards)