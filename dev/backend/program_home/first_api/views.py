from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    return JsonResponse({'message': 'Hello this is a python api message'})
