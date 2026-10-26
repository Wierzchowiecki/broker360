from django.shortcuts import get_object_or_404, render

from .models import Property


def home(request):
    properties = (
        Property.objects
        .filter(status="active")
        .prefetch_related("images")
        .order_by("-created_at")
    )

    return render(
        request,
        "properties/home.html",
        {
            "properties": properties,
        },
    )


def property_detail(request, slug):
    property_object = get_object_or_404(
        Property.objects.prefetch_related("images"),
        slug=slug,
        status="active",
    )

    images = property_object.images.all()

    main_image = images.filter(
        is_main=True,
    ).first()

    if main_image is None:
        main_image = images.first()

    return render(
        request,
        "properties/property_detail.html",
        {
            "property": property_object,
            "images": images,
            "main_image": main_image,
        },
    )