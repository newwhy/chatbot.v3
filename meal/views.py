from django.http import JsonResponse


# Create your views here.


def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons': ['한식', '중식', '일식', '양식', '뷔페']})
