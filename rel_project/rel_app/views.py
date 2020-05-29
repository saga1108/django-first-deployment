from django.shortcuts import render

# Create your views here.

def index(request):
    index_dict = {'text':'hello world','number':100}
    return render(request,'rel_app/index.html',index_dict)

def relative(request):
    return render(request,'rel_app/relative.html')


def another(request):
    return render(request,'rel_app/another.html')
