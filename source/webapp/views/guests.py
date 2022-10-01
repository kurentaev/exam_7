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
# def update_view(request, pk):
#     errors = {}
#     task = get_object_or_404(TasksList, pk=pk)
#     if request.method == 'GET':
#         form = TasksListForm(initial={
#             'title': task.title,
#             'status': task.status,
#             'deadline': task.deadline,
#             'description': task.description
#         })
#         return render(request, 'task_update.html', context={'form': form, 'task': task})
#     elif request.method == 'POST':
#         if request.POST.get('deadline') == '':
#             deadline = None
#         else:
#             deadline = request.POST.get('deadline')
#         task.title = request.POST.get('title')
#         task.status = request.POST.get('status')
#         task.deadline = deadline
#         task.description = request.POST.get('description')
#         if errors:
#             return render(
#                 request,
#                 'task_update.html',
#                 context={
#                     'task': task,
#                     'choices': StatusChoices.choices,
#                     'errors': errors
#                     })
#         task.save()
#         return redirect('todo_detail', pk=task.pk)
#     return render(
#         request,
#         'task_update.html',
#         context={
#             'task': task,
#             'choices': StatusChoices.choices
#             })
