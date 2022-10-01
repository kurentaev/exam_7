from django.urls import path

from webapp.views.base import index_view
from webapp.views.guests import add_view
from webapp.views.guests import update_view
from webapp.views.guests import delete_view
from webapp.views.guests import confirm_delete


urlpatterns = [
    path('', index_view, name='index'),
    path('guest_book/', index_view, name='index'),
    path('guest_book/add/', add_view, name='guest_add'),
    path('guest_book/update/<int:pk>', update_view, name='guest_update'),
    path('guest_book/delete/<int:pk>', delete_view, name='guest_delete'),
    path('guest_book/confirm_delete/<int:pk>', confirm_delete, name='confirm_delete')
]
