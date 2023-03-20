from django.shortcuts import get_object_or_404, render
from .models import Event, Famil, Portfolio, Post,  Team
from .models import Testimonial

# Create your views here.
def index(request):
    testimonials =Testimonial.objects.all()
    portfolios=Portfolio.objects.all()
    teams = Team.objects.all()
    posts = Post.objects.all()
    famils=Famil.objects.all()
    events=Event.objects.all()
    context = {'testimonials': testimonials,
               'posts': posts,
               "portfolios":portfolios,'teams': teams,
               "famils":famils,"events":events}

    return render(request, 'webblock/index.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    posts = Post.objects.all()
    return render(request, 'webblock/post_details.html', {'post': post,'posts': posts})

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'webblock/team.html', {'teams': teams})

def vmv(request):
    return render(request, 'webblock/vmv.html')
    
def belives(request):
    return render(request, 'webblock/belives.html')

def join(request):
    return render(request, 'webblock/join.html')

def family(request):
    return render(request, 'webblock/families.html')

def service(request):
    posts = Post.objects.all()
    contex={'posts': posts}
    return render(request, 'webblock/what-we-do.html',contex)

def event(request):
    posts = Post.objects.all()
    events=Event.objects.all()
    contex={'posts': posts,"events":events}
    return render(request, 'webblock/event.html',contex)

def blog(request):
    posts = Post.objects.all()
    contex={'posts': posts}
    return render(request, 'webblock/blog.html',contex)