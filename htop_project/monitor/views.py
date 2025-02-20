import psutil
from django.http import JsonResponse

def system_info(request):
    data = {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage('/').percent,
    }
    return JsonResponse(data)
