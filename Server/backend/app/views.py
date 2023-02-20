from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, 'index.html')

# from django.contrib.auth.models import User
# from django.http import JsonResponse

# def user_list(request):
#     users = User.objects.all().values('username', 'email', 'first_name', 'last_name', 'is_staff', 'type')
#     return JsonResponse({'users': list(users)})
