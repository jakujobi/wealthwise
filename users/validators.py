from django.core.exceptions import ValidationError
import re

class CustomRegexPasswordValidator:
    """
    Validates that the password contains at least one lowercase letter,
    one uppercase letter, and one special character.
    """
    def validate(self, password, user=None):
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\W).+$', password):
            raise ValidationError(
                "Password must contain at least one lowercase letter, one uppercase letter, and one special character.",
                code='password_no_match',
            )

    def get_help_text(self):
        return "Your password must contain at least one lowercase letter, one uppercase letter, and one special character."