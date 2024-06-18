# custom_middleware.py

from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect

class AutoLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request is for the admin panel
        if request.path.startswith(reverse('admin:index')):
            # Check if the user is not authenticated
            if not request.user.is_authenticated:
                try:
                    # Try to get the 'admin' user
                    user = User.objects.get(username='pritesh')
                    request.user = user  # Set the user for the request
                except User.DoesNotExist:
                    pass  # Handle the case if 'admin' user doesn't exist

        response = self.get_response(request)
        return response
