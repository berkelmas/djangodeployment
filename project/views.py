from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    if request.method == 'POST':
        fullname = request.POST.get("fullname", "")
        email = request.POST.get("email", "")
        topic = request.POST.get("topic", "")
        message_form = request.POST.get("message", "")

        subject = topic
        message = 'email: ' + email + '\n' + 'mesaj: ' + message_form + '\n'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['berkelmas96@gmail.com', ]

        send_mail( subject, message, email_from, recipient_list )
        return render(request, 'project/base.html')
    else:
        return render(request, 'project/base.html')