from django.shortcuts import render
from webapp.models import GuestsList
from webapp.models import StatusChoices
from webapp.forms import GuestSearchForm


def index_view(request):
    form = GuestSearchForm()
    if request.method == 'GET' and 'author' in request.GET:
        author = request.GET['author']
        guests = GuestsList.objects.filter(author=author)
    else:
        guests = GuestsList.objects.filter(status="active").order_by("-created_at")
    context = {"guests": guests,
               "choices": StatusChoices.choices,
               "form": form}
    return render(request, "index.html", context)
