import factory
from datetime import date, datetime, timedelta
from calculators.models import FinancialToolUsage
from tests.users.factories import UserProfileFactory

class FinancialToolUsageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FinancialToolUsage

    user_id = factory.SubFactory(UserProfileFactory)
    tool_type = factory.Faker('random_element', elements=['budget', 'compound_interest', 'retirement'])
    input_data = factory.Faker('json')
    usage_date = factory.Faker('date_time_this_year')
    budget_for_date = factory.Faker('date_this_year') 