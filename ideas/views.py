from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Idea
from django.utils import timezone

def home(request):
    ideas = Idea.objects 
    return render(request, 'ideas/home.html',{'ideas':ideas})

def about(request):
    return render(request, 'ideas/about.html')

@login_required(login_url="/accounts/signup")
def create(request): 
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.FILES['icon'] and request.FILES['image']:
            idea = Idea()
            idea.title = request.POST['title']
            idea.body = request.POST['body']
            idea.icon = request.FILES['icon']
            idea.image = request.FILES['image']
            idea.pub_date = timezone.datetime.now()
            idea.hunter = request.user
            idea.save()
            return redirect('/ideas/'+str(idea.id))

        else:
            return render(request, 'ideas/create.html',{'error':"All fields re"})

    else:
        return render(request, 'ideas/create.html')

def detail(request,idea_id):
    idea = get_object_or_404(Idea,pk=idea_id)
    return render(request,'ideas/detail.html',{'idea':idea})

@login_required(login_url="/accounts/login")
def upvote(request,idea_id):
    if request.method == 'POST':
        idea = get_object_or_404(Idea,pk=idea_id)
        idea.votes_total += 1
        idea.save()
        return redirect('/ideas/' + str(idea.id))
