from rest_framework import serializers
from billing.models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name','created_at','email','phone','status']

class SubcriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcription
        fields = ['customer_name','from_date','to_date','amount','status','customer']
        depth = 1
        
