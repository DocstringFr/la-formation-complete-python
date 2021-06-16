from django.urls import path

from contacts.views import index, add_contact, delete_contact

urlpatterns = [
    path('', index, name="index"),
    path('add/', add_contact, name="add-contact"),
    path('delete/', delete_contact, name="delete-contact"),
]
