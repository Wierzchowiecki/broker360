from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(
        "Imię i nazwisko",
        max_length=150,
    )

    email = models.EmailField(
        "Adres e-mail",
        blank=True,
    )

    phone = models.CharField(
        "Numer telefonu",
        max_length=30,
        blank=True,
    )

    message = models.TextField(
        "Treść wiadomości",
    )

    privacy_notice_confirmed = models.BooleanField(
        "Potwierdzenie zapoznania się z polityką prywatności",
        default=False,
    )

    created_at = models.DateTimeField(
        "Data wysłania",
        auto_now_add=True,
    )

    is_read = models.BooleanField(
        "Wiadomość przeczytana",
        default=False,
    )

    def __str__(self):
        return f"{self.name} – {self.created_at:%d.%m.%Y %H:%M}"

    class Meta:
        verbose_name = "wiadomość kontaktowa"
        verbose_name_plural = "wiadomości kontaktowe"
        ordering = ["-created_at"]