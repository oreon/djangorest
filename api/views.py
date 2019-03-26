from django.shortcuts import render
from rest_framework import  viewsets
from .serializers import *
from .models import Bucketlist
from rest_framework import permissions, generics
from .permissions import IsOwner
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    #queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)  # ADD THIS LINE


    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        title = self.request.query_params.get('title', None)
        print(title)

        return Bucketlist.objects.filter(name__contains=title) if title else Bucketlist.objects.all()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class NestedViewSetMixin(object):
    parent = None
    parent_lookup_field = 'nested'

    def get_nested_filter_dict(self):
        filter_dict = {}
        if not self.parent:
            return filter_dict
        viewset = self.parent(request=self.request)
        if isinstance(viewset, NestedViewSetMixin):
            filter_dict.update(viewset.get_nested_filter_dict())
        filter_dict.update({self.parent_lookup_field:
                            self.kwargs.get('%s_%s' % (self.parent_lookup_field, viewset.lookup_field))})
        return filter_dict

    def get_queryset(self):
        return super(NestedViewSetMixin, self).get_queryset().filter(**self.get_nested_filter_dict())

    def perform_create(self, serializer):
        viewset = self.parent(request=self.request, kwargs={self.parent.lookup_field: self.get_nested_filter_dict().get(self.parent_lookup_field)})
        serializer.save(**{self.parent_lookup_field: viewset.get_object()})


class CustomerOrderViewSet(viewsets.ModelViewSet):

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(owner=self.request.user)
    queryset = CustomerOrder.objects.all()

    # def get_serializer_class(self):
    #     # Define your HTTP method-to-serializer mapping freely.
    #     # This also works with CoreAPI and Swagger documentation,
    #     # which produces clean and readable API documentation,
    #     # so I have chosen to believe this is the way the
    #     # Django REST Framework author intended things to work:
    #     if self.request.method in ('GET',):
    #         # Since the ReadSerializer does nested lookups
    #         # in multiple tables, only use it when necessary
    #         return CustomerOrderSerializer
    #     return CustomerOrderWriteSerializer
    serializer_class = CustomerOrderSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^firstName', '^lastName')

        # GET: /api/v1/foo/1/bar/
    @action(methods=['get'], detail= True)
    def customerOrders(self, request, pk=None):
        
        customer = self.get_object()
        qs = customer.customerOrders.all().order_by('id')
        
        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = CustomerOrderSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CustomerOrderSerializer(qs, many=True)
        return Response(serializer.data)

class OrderItemViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    parent = CustomerOrderViewSet
    parent_lookup_field = 'customerOrder'  # must be the same as in the router and your Order model
    #queryset = Order.objects.all()
    #serializer_class = ClientOrderSerialize

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
