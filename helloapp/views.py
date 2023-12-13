from django.shortcuts import render
from django.conf import settings

def index(request):
    print("epta index")
    username = request.GET.get('username', '')
    if username:
        message = f"Hello, {username}!"
    else:
        message = "Hello, Unnamed!"

    template_path = f'{settings.BASE_DIR}/helloapp/templates/index.html'

    return render(request, template_path, {'message': message})
