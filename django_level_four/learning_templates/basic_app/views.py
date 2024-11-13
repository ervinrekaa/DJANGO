from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'Hello World!', 'number':100}
    return render(request, 'basic_app/index.html', context=context_dict)

def profile(request):
    return render(request, 'basic_app/profile.html')

def contact(request):
    return render(request, 'basic_app/contact.html')