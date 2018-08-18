from django.shortcuts import render
from .models import Detail
from .forms import PostForm
# Create your views here.

def index(request):
    form=PostForm(request.POST or None)
    instance=form.save(commit=False)
    instance.save()
    context={
        "form":form
    }
    return render(request,'index.html',context)