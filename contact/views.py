from django.shortcuts import redirect, render

from .forms import ContactMessageForm


def contact(request):
    if request.method == "POST":
        form = ContactMessageForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("contact:success")
    else:
        form = ContactMessageForm()

    return render(
        request,
        "contact/contact.html",
        {"form": form},
    )


def contact_success(request):
    return render(
        request,
        "contact/contact_success.html",
    )
def privacy_policy(request):
    return render(request, "contact/privacy_policy.html")
