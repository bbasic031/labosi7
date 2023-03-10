from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Image, Comment
from django.utils import timezone
from django.urls import reverse

# Create your views here.
def home(request):
    context = {}
    return render(request, 'app/home.html', context)

def index(request):
    images = Image.objects.all()
    context = {
        'image_list': images
    }
    return render(request, 'app/index.html', context)

def detail(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    comments=image.comment_set.all()
    context = {
        'image': image,
        'comments': comments,
    }
    return render(request, 'app/detail.html', context)  

def post_comment(request, image_id):
    image=get_object_or_404(Image, pk=image_id)
    comment=Comment(nick=request.POST['nick'], text=request.POST['text'],image=image,pub_date=timezone.now())
    comment.save()
    return HttpResponseRedirect(reverse('app:detail', args=[image_id]))

def approve_comment(request, comment_id):
        comment=get_object_or_404(Comment, pk=comment_id)
        comment.approved=True
        comment.save()
        return HttpResponseRedirect(reverse('app:detail',args=[comment.image.id]))