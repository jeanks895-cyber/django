from django.shortcuts import render

def form_view(request):
    return render(request, 'loginapp/form.html')

def result_view(request):
    username = request.GET.get('username')
    data = request.GET

    return render(request, 'loginapp/result.html', {
        'username': username,
        'data': data
    })
# Create your views here.
