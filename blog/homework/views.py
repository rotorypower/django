import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)

def homework_index(request):
    value = request.GET.get('get-key-1')
    value and logger.info(f'get-key-1 = {value}')

    value = request.POST.get('post-key-1')
    value and logger.info(f'post-key-1 = {value}')

    return HttpResponse('HOMEWORK')


