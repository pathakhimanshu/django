from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'Hello!','number':10}
    return render(request,'appone/index.html',context_dict)

def other(request):
    return render(request,'appone/other.html')

def relative(request):
    return render(request,'appone/relative_url.html')
