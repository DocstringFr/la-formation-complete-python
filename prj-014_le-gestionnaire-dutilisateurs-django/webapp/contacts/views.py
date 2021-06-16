from django.shortcuts import render, redirect
from api.crm import get_all_users, User


def index(request):
    return render(request, 'contacts/index.html', {'users': get_all_users()})


def add_contact(request):
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    address = request.POST.get("address")
    phone_number = request.POST.get("phone_number")

    user = User(first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                address=address)
    user.save()

    return redirect('index')


def delete_contact(request):
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    user = User(first_name, last_name)
    user.delete()

    return redirect('index')