from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)

def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        # send an email
        send_mail(
            message_name, # subject
            message, # message
            message_email, # from email
            ['okpomub98@gmail.com'],# To Email
        )
        return render(request, 'contact.html', {'message_name': message_name})
    else:
         return render(request, 'contact.html', {})

def about(request):
    context = {}
    return render(request, 'about.html', context)

def pricing(request):
    context = {}
    return render(request, 'pricing.html', context)

def service(request):
    context = {}
    return render(request, 'service.html', context)

def blogDetails(request):
    context = {}
    return render(request, 'blog-details.html', context)

def blog(request):
    context = {}
    return render(request, 'blog.html', context)

def appointment(request):
    if request.method == 'POST':
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST.get('your-schedule')
        your_date = request.POST['your-date']
        your_message = request.POST['your-message']

        
        # send an email
        appointment ='Name: ' + your_name + " " + your_phone + " Email: " + your_email ,
        " Address: " + your_address + " Date:" + your_date  + " Message:" + your_message

        send_mail(
            'Appointment Request',
            appointment, # subject 
            your_email, # from email
            ['okpomub98@gmail.com'],# To Email
        )
        context = {'your_name': your_name, 'your_phone': your_phone, 'your_email': your_email, 'your_address': your_address,
         'your_schedule': your_schedule, 'your_date': your_date, 'your_message': your_message}
        return render(request, 'appointment.html', context)
    else:
         return render(request, 'home.html', {})