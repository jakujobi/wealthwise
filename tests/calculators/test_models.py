import pytest
from django.test import TestCase
from datetime import date
from calculators.models import FinancialToolUsage
from tests.calculators.factories import FinancialToolUsageFactory

# Pytest style tests
@pytest.mark.django_db
class TestFinancialToolUsage:
    def test_financial_tool_usage_creation(self):
        tool_usage = FinancialToolUsageFactory()
        assert tool_usage.usage_id is not None
        assert tool_usage.user_id is not None
        assert tool_usage.tool_type in ['budget', 'compound_interest', 'retirement']
        assert tool_usage.input_data is not None
        assert tool_usage.usage_date is not None
        assert tool_usage.budget_for_date is not None

    def test_financial_tool_usage_str_representation(self):
        tool_usage = FinancialToolUsageFactory()
        expected_str = f"{tool_usage.tool_type} usage by User {tool_usage.user_id} on {tool_usage.usage_date}"
        assert str(tool_usage) == expected_str

# Django TestCase style tests
class FinancialToolUsageTests(TestCase):
    def setUp(self):
        self.tool_usage = FinancialToolUsageFactory()

    def test_default_budget_date(self):
        # Create a tool usage without specifying budget_for_date
        tool_usage = FinancialToolUsageFactory(budget_for_date=None)
        # The default date should be date(1000, 10, 10)
        self.assertEqual(tool_usage.budget_for_date, date(1000, 10, 10)) 