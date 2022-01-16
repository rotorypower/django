from django.http import HttpResponse

import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def posts_index(request):
   value = request.GET.get("key")
   logger.info(value)
   return HttpResponse("Posts index view")

def news_city(request):
   value = request.GET.get("key")
   logger.info(value)
   return HttpResponse('NEWS MY CITY')

def city(request):
   value = request.POST.get("city")
   logger.info(value)
   return HttpResponse('CITY')


# Create your views here.
