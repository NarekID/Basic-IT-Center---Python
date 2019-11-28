from django.shortcuts import render, redirect, reverse
from .forms import SendEmailForm
from django.core.mail import send_mail
from django.conf.global_settings import EMAIL_HOST_USER
from django.http import HttpResponseRedirect


# Create your views here.
def send_page(request):
    sent = False
    if request.method == "POST":
        form = SendEmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message = "{}\n\n\n From {}".format(cd["message"], cd["name"])
            send_mail(cd["subject"], message, EMAIL_HOST_USER, [cd["to"]])
            sent = True
            form = SendEmailForm()
    else:
        form = SendEmailForm()
    return render(request, 'send.html', {'form': form,
                                         'sent': sent})
