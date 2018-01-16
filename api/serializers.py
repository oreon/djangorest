from rest_framework import serializers
from .models import *
import sys

class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    owner = serializers.ReadOnlyField(source='owner.username')  # ADD THIS LINE

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Bucketlist
        fields = ('id', 'name', 'date_created', 'owner','date_modified')
        read_only_fields = ('date_created', 'date_modified')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = OrderItem
        fields = '__all__'

class CustomerOrderWriteSerializer(serializers.ModelSerializer):
    #orderItems = OrderItemSerializer(many=True)

    class Meta:
        model = CustomerOrder
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': False, 'required': True}}


class CustomerOrderSerializer(serializers.ModelSerializer):
    orderItems = OrderItemSerializer(many=True)

    class Meta:
        model = CustomerOrder
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': False, 'required': True}}

    def get_unique_together_validators(self):
        '''
        Overriding method to disable unique together checks
        '''
        return []

    def create(self, validated_data):

        orderItems = validated_data.pop('orderItems')
        customerOrder = CustomerOrder.objects.create(**validated_data)
        for orderItem in orderItems:
            OrderItem.objects.create(customerOrder=customerOrder, **orderItems)
        return customerOrder

    #@transaction.atomic
    def update(self, instance, validated_data):
        try:
            self.updateOrderItems(instance, validated_data)
            co =  CustomerOrder.objects.update(**validated_data)
            return CustomerOrder.objects.get(pk=instance.id)
            #return super(self, CustomerOrderSerializer).update(instance, validated_data)
        except:
            print (sys.exc_info()[0])
            return instance

    def updateOrderItems(self, instance, validated_data):
        if not 'orderItems' in validated_data.keys(): return;

        orderItemsCurrent = validated_data.pop('orderItems')

        ids = [item['id'] for item in orderItemsCurrent if 'id' in item.keys()]

        for item in instance.orderItems.all():
            #if item.id not in ids:
                item.delete()

        for item in orderItemsCurrent:
            OrderItem( **item).save()

        print (len(orderItemsCurrent))