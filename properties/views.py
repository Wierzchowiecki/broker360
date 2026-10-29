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

    gallery_images = list(
        property_object.images.all()
    )

    main_image = next(
        (
            image
            for image in gallery_images
            if image.is_main
        ),
        None,
    )

    if main_image is None and gallery_images:
        main_image = gallery_images[0]

    if main_image is not None:
        gallery_images = [
            main_image,
            *[
                image
                for image in gallery_images
                if image.pk != main_image.pk
            ],
        ]

        additional_images = [
            image
            for image in gallery_images
            if image.pk != main_image.pk
        ]
    else:
        additional_images = []

    return render(
        request,
        "properties/property_detail.html",
        {
            "property": property_object,
            "main_image": main_image,
            "gallery_images": gallery_images,
            "additional_images": additional_images,
        },
    )