import json
from datetime import datetime

from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
import logging
from django.views.decorators.csrf import csrf_exempt

from .models import Message
log = logging.getLogger(__name__)


# Create your views here.
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def messages(request):
    if request.method == 'POST':
        current_msg = json.loads(request.body)
        msg = Message(bearId=current_msg['bearId'],
                      message=current_msg['message'],
                      timestamp=datetime.now())
        msg.save()

    msgs = Message.objects.all()
    jsony = [model_to_dict(msg) for msg in msgs]
    jsony = sorted(jsony, key=lambda x: x['timestamp'], reverse=True)

    if not jsony:
        return JsonResponse([], safe=False)

    return JsonResponse(jsony, safe=False)
