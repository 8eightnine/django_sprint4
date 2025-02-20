from django.shortcuts import render

def error_403(request, exception):
    return render(request, 'pages/403.html', status=403)

def error_404(request, exception):
    return render(request, 'pages/404.html', status=404)

def error_500(request):
    return render(request, 'pages/500.html', status=500)
