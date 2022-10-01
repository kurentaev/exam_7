from django.shortcuts import render
from webapp.models import GuestsList
from webapp.models import StatusChoices


def index_view(request):
    guests = GuestsList.objects.filter(status="active").order_by("-created_at")
    context = {
        "guests": guests,
        "choices": StatusChoices.choices
    }
    return render(request, "index.html", context)

