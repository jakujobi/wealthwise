from django.db import models
from datetime import date

# budget
class FinancialToolUsage(models.Model):
    usage_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    tool_type = models.CharField(max_length=20)
    input_data = models.JSONField()
    usage_date = models.DateTimeField(auto_now_add=True)
    budget_for_date = models.DateField(default=date(1000, 10, 10))
    
    def __str__(self):
        return f"{self.tool_type} usage by User {self.user_id} on {self.usage_date}"