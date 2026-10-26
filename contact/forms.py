from django import forms

from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage

        fields = [
            "name",
            "email",
            "phone",
            "message",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Imię i nazwisko",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Adres e-mail",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "placeholder": "Numer telefonu",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "placeholder": "W czym mogę Ci pomóc?",
                    "rows": 6,
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")

        if not email and not phone:
            raise forms.ValidationError(
                "Podaj adres e-mail lub numer telefonu."
            )

        return cleaned_data