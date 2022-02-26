from django.shortcuts import render
from . import models

def articles_list(request):
    articl=models.Article.objects.all().order_by('date')
    arqs={'Article1':articl}
    return render(request,'articles/articleslist.html',arqs)