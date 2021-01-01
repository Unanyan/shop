from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import HttpResponseRedirect
from .models import Subscriber
from django.contrib import messages


def subscribe(request):
    email = request.POST['email']
    try:
        if request.method == 'POST':
            # if exist try exception
            Subscriber.objects.get(mail=email)
            print("Subscriber with this email exist: ", email)
        messages.success(request, 'Thank you, you are already subscribed!')
        return HttpResponseRedirect('/', {'email': email.__str__()})
    except Subscriber.DoesNotExist as i:
        try:
            validate_email(email)
            sub = Subscriber()
            sub.mail = email
            sub.save()
            print("Created subscriber with this email: ", email, i)
            messages.success(request, 'Thank you, you are successfully subscribed!')
            return HttpResponseRedirect('/')
        except ValidationError as e:
            print("bad email, details: ", e)
            messages.success(request, 'Please input correct email!')
            return HttpResponseRedirect('/')
