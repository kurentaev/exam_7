from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import GuestsList
from webapp.forms import GuestsListForm


def add_view(request):
    if request.method == "GET":
        form = GuestsListForm()
        return render(request, "guest_create.html", context={'form': form})
    elif request.method == "POST":
        form = GuestsListForm(request.POST)
        if form.is_valid():
            guest_data = {
                'author': request.POST.get('author'),
                'email': request.POST.get('email'),
                'content': request.POST.get('content')
            }
            GuestsList.objects.create(**guest_data)
            return redirect('index')


def update_view(request, pk):
    guest = get_object_or_404(GuestsList, pk=pk)
    if request.method == 'GET':
        form = GuestsListForm(initial={
            'author': guest.author,
            'email': guest.email,
            'content': guest.content,
        })
        return render(request, 'guest_update.html', context={'form': form, 'guest': guest})
    elif request.method == 'POST':
        guest.author = request.POST.get('author')
        guest.email = request.POST.get('email')
        guest.content = request.POST.get('content')
        guest.save()
        return redirect('index')
    return render(request, 'guest_update.html', context={'guest': guest})


# def delete_view(request, pk):
#     guest = get_object_or_404(GuestsList, pk=pk)
#     return render(request, 'guest_confirm_delete.html', context={'task': task})
#
#
# def confirm_delete(request, pk):
#     task = get_object_or_404(TasksList, pk=pk)
#     task.delete()
#     return redirect('index')
#
#
