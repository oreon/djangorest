from api.modelsBase import *


class Bucketlist(models.Model):
    """This class represents the bucketlist model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    owner = models.ForeignKey('auth.User',  related_name='bucketlists', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)



class Product(ProductBase):
    pass

class Category(CategoryBase):
    pass


class Customer(CustomerBase):
    pass


class CustomerOrderManager(models.Manager):
    def create_Or_update_custom(self, items):

        ois = items['orderItems']
        del items['orderItems']

        co = CustomerOrder(**items)
        co.save()

        for i in ois:
            oi = OrderItem()
            for k, v in i.items():
                setattr(oi, k, v)
            oi.customerOrder = co
            oi.save()
            # co.orderItems.add(oi)

        return co


class CustomerOrder(CustomerOrderBase):
    #objects = CustomerOrderManager()
    pass


class OrderItem(OrderItemBase):
    pass


class Person(PersonBase):
    class Meta:
        abstract = True


class Employee(EmployeeBase):
    pass


class CustomerReview(CustomerReviewBase):
    pass
