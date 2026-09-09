from django.shortcuts import render, redirect
from django.core.mail import EmailMessage  # <--- Changed this import
from django.conf import settings
from .models import (
    Service, PortfolioProject, TeamMember, Stat, 
    HeroContent, ValueProposition, ContactMessage, ContactPageSettings
)
from .forms import ContactForm

# 1. Home Page (Dynamic Landing Page)
def home_view(request):
    hero = HeroContent.objects.first() 
    propositions = ValueProposition.objects.all()
    featured_projects = PortfolioProject.objects.filter(is_featured=True)[:2] 
    
    return render(request, 'agency/home.html', {
        'hero': hero,
        'propositions': propositions,
        'featured_projects': featured_projects
    })

# 2. Services Page
def services_view(request):
    services = Service.objects.all()
    return render(request, 'agency/services.html', {'services': services})

# 3. Work / Portfolio Page
def work_view(request):
    projects = PortfolioProject.objects.all()
    categories = ['All', 'Web', 'App', 'E-commerce']
    
    return render(request, 'agency/work.html', {
        'projects': projects, 
        'categories': categories
    })

# 4. About Page
def about_view(request):
    team = TeamMember.objects.all()
    stats = Stat.objects.all()
    return render(request, 'agency/about.html', {
        'team': team,
        'stats': stats
    })

# 5. Contact Page (Secure Form Handling)
def contact_view(request):
    page_settings = ContactPageSettings.objects.first()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # 1. Save the message to your database
            contact_msg = form.save() 
            
            # 2. Format the email you will receive
            subject = f"New Project Inquiry from {contact_msg.name}"
            message_body = f"""
You have received a new message from your agency website!

Name: {contact_msg.name}
Email: {contact_msg.email}
Phone: {contact_msg.phone_number}
Project Type: {contact_msg.project_type}

Message:
{contact_msg.message}
"""            
            # 3. Send the email using EmailMessage (so 'Reply' works correctly!)
            email = EmailMessage(
                subject=subject,
                body=message_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.EMAIL_HOST_USER], 
                reply_to=[contact_msg.email],  # <--- This is the magic line!
            )
            email.send(fail_silently=False)
            
            return redirect('success')
    else:
        form = ContactForm()
        
    return render(request, 'agency/contact.html', {
        'form': form,
        'page_settings': page_settings
    })

# 6. Success Page (After Contact Form Submission)
def success_view(request):
    return render(request, 'agency/success.html')