from django.core.exceptions import ValidationError

class DifferentFromCurrentPasswordValidator:

    def validate(self, password, user=None):

        if user and user.check_password(password):
            raise ValidationError(
                "Your new password cannot be the same as your current password."
            )

    def get_help_text(self):
        return (
            "Your new password must be different from your current password."
        )