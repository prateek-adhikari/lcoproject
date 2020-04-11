from django.shortcuts import render
from lco.models import Frequentlyaskquest, TeamMember, Moments, Story
# Create your views here.
def home(request):
    return render(request, "home.html")

def team(request):
    members = TeamMember.objects.all()
    context = {
        'member': members
    }
    return render(request, "team.html", context)

def tournament(request):
    return render(request, "tournament.html")

def faq(request):
    faqs = Frequentlyaskquest.objects.all()
    context = {
        'faqz': faqs
    }
    return render(request, "faq.html", context)

def about(request):
    stories = Story.objects.all()
    moments = Moments.objects.all()
    context = {
        'story': stories,
        'moment': moments
    }
    return render(request, "about.html", context)