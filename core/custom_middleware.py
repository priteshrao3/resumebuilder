from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect

class AutoLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith(reverse('admin:index')):
            if not request.user.is_authenticated:
                try:
                    user = User.objects.get(username='Pritesh')
                    request.user = user
                except User.DoesNotExist:
                    pass

        response = self.get_response(request)
        return response
