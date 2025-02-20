from django.shortcuts import render

# Create your views here.
def create_webhook(request):
    return render(request, "test_api/create_webhook.html")