from django.shortcuts import render

def form_view(request):
    return render(request, 'greeting/form.html')

def result_view(request):
    username = request.GET.get('username')
    data = request.GET

    return render(request, 'greeting/result.html', {
        'username': username,
        'data': data
    })
# Create your views here.
