# -*- coding: utf-8 -*-

from django.http import JsonResponse
import json, datetime

from django.views.decorators.csrf import csrf_exempt





# Create your views here.
@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    cafeteria_name = received_json_data['content']
    today_date = datetime.date.today().strftime("%m월 %d일")
# def keyboard(request):
    return JsonResponse({
            'message': {
                'text': today_date + '의 ' + cafeteria_name + '메뉴입니다.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['한식', '중식', '일식', '뷔페']
            }})

