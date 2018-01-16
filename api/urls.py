from .views import *
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'products', ProductViewSet)
#router.register(r'categorys', CategoryViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'customerOrders', CustomerOrderViewSet)
router.register(r'orderItems', OrderItemViewSet)

urlpatterns = {
    url(r'^auth/', include('rest_framework.urls',  namespace='rest_framework')),
    url(r'^bucketlists/$', CreateView.as_view(), name="create"),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name="details")
}

urlpatterns = format_suffix_patterns(urlpatterns)

