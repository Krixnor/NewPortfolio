from django.shortcuts import render, redirect
from .forms import MessageForm
from django.core.mail import send_mail, EmailMessage

# Create your views here.


def port(request):
    form = MessageForm()
    return render(request, 'myPortfolio/index.html',{
        'form':form
    })
    pass


def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail('New message from your website', message, email, ['udodorchristabel@gmail.com'])
            return redirect('port')
    else:
        form = MessageForm()
    return render(request, 'myPortfolio/index.html', {'form': form})
