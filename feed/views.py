from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
# Create your views here.
class Homepage(ListView):
    http_method_names = ['get']
    template_name = 'feed/homepage.html'
    model = Post  #โมเดลที่ลิสคือโมเดลนี้
    context_object_name = "Posts"
    queryset = Post.objects.all().order_by('-id')[0:30]
