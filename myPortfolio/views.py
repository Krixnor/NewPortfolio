from django.shortcuts import render, redirect
from .forms import MessageForm
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from .models import Education,Skills,Service,Porfolio
from django.contrib import messages

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
            content = f"{message}\nfrom: {mail}"
            
            # Create an EmailMessage object
            email = EmailMessage(
                subject=f'New message from {mail} on your website',
                body=content,
                from_email=mail,
                to=['udodorchristabel@gmail.com'],
            )
            
            # Attempt to send the email
            try:
                email.send()
                messages.success(request, 'Message Sent')
            except Exception as e:
                messages.error(request, f'Error sending message')

            return redirect('port')
        else:
            messages.error(request, 'Error sending message')
            return redirect('port')
    else:
        form = MessageForm()
    return render(request, 'myPortfolio/index.html', {'form': form})
