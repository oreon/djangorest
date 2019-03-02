from .views import *

#from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from rest_framework import routers
from django.urls import path, include

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'products', ProductViewSet)
#router.register(r'categorys', CategoryViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'customerOrders', CustomerOrderViewSet)
router.register(r'orderItems', OrderItemViewSet)

urlpatterns = {
    path('auth/', include('rest_framework.urls',  namespace='rest_framework')),
    path('bucketlists/$', CreateView.as_view(), name="create"),
    path('bucketlists/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name="details")
}

#urlpatterns = format_suffix_patterns(urlpatterns)

