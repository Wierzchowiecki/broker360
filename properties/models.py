from django.db import models
from django.utils.text import slugify


class Property(models.Model):
    PROPERTY_TYPES = [
        ("apartment", "Mieszkanie"),
        ("house", "Dom"),
        ("plot", "Działka"),
        ("commercial", "Lokal użytkowy"),
    ]

    OFFER_TYPES = [
        ("sale", "Sprzedaż"),
        ("rent", "Wynajem"),
    ]

    STATUS_CHOICES = [
        ("active", "Aktywna"),
        ("reserved", "Rezerwacja"),
        ("sold", "Sprzedana"),
        ("rented", "Wynajęta"),
    ]

    title = models.CharField(
        "Tytuł",
        max_length=200,
    )

    slug = models.SlugField(
        "Adres oferty",
        max_length=240,
        unique=True,
        blank=True,
        null=True,
        editable=False,
    )

    description = models.TextField(
        "Opis",
    )

    property_type = models.CharField(
        "Rodzaj nieruchomości",
        max_length=20,
        choices=PROPERTY_TYPES,
    )

    offer_type = models.CharField(
        "Rodzaj oferty",
        max_length=10,
        choices=OFFER_TYPES,
    )

    city = models.CharField(
        "Miasto",
        max_length=100,
        default="Poznań",
    )

    district = models.CharField(
        "Dzielnica",
        max_length=100,
        blank=True,
    )

    price = models.DecimalField(
        "Cena",
        max_digits=12,
        decimal_places=2,
    )

    area = models.DecimalField(
        "Powierzchnia",
        max_digits=10,
        decimal_places=2,
    )

    rooms = models.PositiveSmallIntegerField(
        "Liczba pokoi",
        null=True,
        blank=True,
    )

    status = models.CharField(
        "Status",
        max_length=20,
        choices=STATUS_CHOICES,
        default="active",
    )

    is_featured = models.BooleanField(
        "Oferta wyróżniona",
        default=False,
    )

    created_at = models.DateTimeField(
        "Data dodania",
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        "Data aktualizacji",
        auto_now=True,
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            polish_characters = str.maketrans(
                "ąćęłńóśźżĄĆĘŁŃÓŚŹŻ",
                "acelnoszzACELNOSZZ",
            )

            normalized_title = self.title.translate(
                polish_characters
            )

            base_slug = slugify(normalized_title)[:220]

            if not base_slug:
                base_slug = "oferta"

            new_slug = base_slug
            number = 2

            while Property.objects.filter(
                slug=new_slug
            ).exclude(pk=self.pk).exists():
                new_slug = f"{base_slug}-{number}"
                number += 1

            self.slug = new_slug

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "nieruchomość"
        verbose_name_plural = "nieruchomości"
        ordering = ["-created_at"]


class PropertyImage(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Nieruchomość",
    )

    image = models.ImageField(
        "Zdjęcie",
        upload_to="properties/",
    )

    description = models.CharField(
        "Opis zdjęcia",
        max_length=200,
        blank=True,
    )

    is_main = models.BooleanField(
        "Zdjęcie główne",
        default=False,
    )

    created_at = models.DateTimeField(
        "Data dodania",
        auto_now_add=True,
    )

    def __str__(self):
        return f"Zdjęcie: {self.property.title}"

    class Meta:
        verbose_name = "zdjęcie nieruchomości"
        verbose_name_plural = "zdjęcia nieruchomości"
        ordering = ["-is_main", "created_at"]