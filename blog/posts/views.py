import logging
from django.http import HttpResponse

from posts.models import Post

logger = logging.getLogger(__name__)


def posts_index(request):
   posts = Post.objects.all()
   return HttpResponse([', '.join([x.slug for x in posts])])
