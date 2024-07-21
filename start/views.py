from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
def default_view(request):
    return redirect('login')


