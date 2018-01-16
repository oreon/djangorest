from factory.django import DjangoModelFactory
import factory
from . import models



class UserFactory(DjangoModelFactory):
    class Meta:
        model = 'auth.user'

    username = factory.Sequence(lambda n: 'user%d' % n)

    @factory.lazy_attribute
    def email(self):
        return '%s@example.com' % self.username

class BucketListFactory(DjangoModelFactory):
    class Meta:
        model = 'api.Bucketlist'

    name = 'Java Dev'
    owner = factory.SubFactory('api.factories.UserFactory', profile=None)

# Another, different, factory for the same object
# class AdminFactory(factory.Factory):
#     class Meta:
#         model = models.User
#
#     first_name = 'Admin'
#     last_name = 'User'
#     admin = True