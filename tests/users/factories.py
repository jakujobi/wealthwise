import factory
from django.contrib.auth import get_user_model
from users.models import UserProfile

User = get_user_model()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')
    password = factory.PostGenerationMethodCall('set_password', 'testpass123')
    is_active = True

    @factory.post_generation
    def profile(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for profile in extracted:
                self.profile.add(profile)
        else:
            UserProfile.objects.create(user=self, **kwargs)

class UserProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserProfile

    user = factory.SubFactory(UserFactory)
    bio = factory.Faker('text')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name') 