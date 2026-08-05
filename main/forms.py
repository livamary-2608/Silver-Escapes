from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
class CustomPasswordResetForm(PasswordResetForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["email"].widget.attrs.update({
            "placeholder": "Email Address...",
            "class": "form-control"
        })
        from django.contrib.auth.models import User
from django import forms
class EditProfileForm(forms.ModelForm):
    phone_number = forms.CharField(
    max_length=10,
    required=False,
    validators=[
        RegexValidator(
            regex=r'^\d{10}$',
            message="Phone number must contain exactly 10 digits."
        )
    ],
    widget=forms.TextInput(attrs={
        "placeholder": "Enter phone number"
    })
)
    profile_picture = forms.ImageField(
    required=False
)
    delete_profile_picture = forms.BooleanField(
    required=False,
    label="Remove Profile Picture"
)
    class Meta:
        model = User
        fields = [
            "first_name",
            "username",
            "email"
        ]
        labels = {
            "first_name": "Full Name"
        }