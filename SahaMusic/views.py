from django.http import JsonResponse

def simple_api_view(request):
    data = {
        "message": "Hello from Django!",
        "status": "success"
    }
    return JsonResponse(data)
