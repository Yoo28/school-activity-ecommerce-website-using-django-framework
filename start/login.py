from django.contrib.auth.hashers import check_password
from django.shortcuts import redirect, render
from django.views import View
from django.urls import reverse

from start.customer import Customer

class Login(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        customer = Customer.get_customer_by_email(email)
        error_message = None

        if customer:
            if check_password(password, customer.password):
                request.session['customer_id'] = customer.id
                return redirect('home')
            else:
                error_message = 'Invalid email or password!'
        else:
            error_message = 'Invalid email or password!'

        return render(request, self.template_name, {'error': error_message})

