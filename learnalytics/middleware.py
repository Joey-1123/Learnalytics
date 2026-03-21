import logging
from django.http import HttpResponse
from django_ratelimit.core import is_ratelimited
from security.models import SecurityLog, BlockedIP
from django.contrib import messages
from django.shortcuts import render, redirect
logger = logging.getLogger('django.security')


class AdminRateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')

        #IP blocking check
        if BlockedIP.objects.filter(ip_address=ip).exists():
            return HttpResponse("Your IP is blocked.", status=403)

        
        if request.path.startswith('/admin/login') and request.method == "POST":

            limited = is_ratelimited(
                request,
                group='admin-login',
                key='ip',
                rate='5/m',
                method='POST',
                increment=True,
            )

            if limited:
                logger.warning(f"Admin login rate limit exceeded from IP: {ip}")

                # Save to DB
                SecurityLog.objects.create(
                    ip_address=ip,
                    path=request.path,
                    message="Admin login rate limit exceeded"
                )

                return HttpResponse(
                  "Too many login attempts. Please wait a minute and try again.",
                   status=429
                )   

        return self.get_response(request)