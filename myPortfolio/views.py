from django.shortcuts import render, redirect
from .forms import MessageForm
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from .models import Education,Skills,Service,Porfolio

# Create your views here.


def port(request):
    education = Education.objects.all()
    skills = Skills.objects.all()
    services = Service.objects.all()
    projects = Porfolio.objects.all()
    form = MessageForm()
    return render(request, 'myPortfolio/index.html',{
        'form':form,
        'education': education,
        'skills':skills,
        'services':services,
        'projects':projects
    })
    pass


def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            mail = form.cleaned_data['email']
            message = form.cleaned_data['message']
            content = message + '\n' + mail 
            #             from_mail = mail ]
            # message = form.cleaned_data['message']
            send_mail(f'New message from {mail} on your website', content, mail, [settings.EMAIL_HOST_USER])
            return redirect('port')
    else:
        form = MessageForm()
    return render(request, 'myPortfolio/index.html', {'form': form})
