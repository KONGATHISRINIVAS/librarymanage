from django.shortcuts import render,redirect

from .models import *
from .forms import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
import datetime

def index(request):
    return render(request,'index.html')

def BooklistView(request):
    forms=Book.objects.all()
    context={
    'Form':forms,
    }
    return render(request,'registration/book_list.html',context)

@login_required
def BookDetailView(request,pk):
    book=get_object_or_404(Book,id=pk)
    return render(request,'book_detail.html',locals())
@login_required
def BookCreate(request):
    if not request.user.is_superuser:
        return redirect('index')
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(index)
    return render(request, 'form.html', locals())

@login_required
def BookUpdate(request, pk):
    if not request.user.is_superuser:
        return redirect('index')
    obj = Book.objects.get(id=pk)
    form = BookForm(instance=obj)
    if request.method == 'POST':
        form = BookForm(data=request.POST, files=request.FILES, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect(index)
    return render(request, 'form.html', locals())

@login_required
def BookDelete(request, pk):
    if not request.user.is_superuser:
        return redirect('index')
    obj = get_object_or_404(Book, pk=pk)
    obj.delete()
    return redirect('index')

# Create your views here.
