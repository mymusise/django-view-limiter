Django-View-Limiter
===

Django-View-Limiter is a django app, which limit the time of every user to visit apis mainly.
Also you can limit the page view of apis directly.


Install
===

Django-View-Limiter is best installed via PyPI. To install the latest version, run:

	pip install apilimiter
or Install from github source:

	pip install git+git://github.com/mymusise/django-view-limiter


Install Requires
===
- django >=1.9


Examples
===

### Limit directly

You can call the limiter decorator directly to wrap your view function like that.
**myapp/views.py**

    from django.shortcuts import HttpResponse
    from apilimiter.decorators import limiter

    @limiter(limit_key='',limit_time=5)
    def index(request):
        return HttpResponse("decorators test")

If you view this api more than 5 times, it will return the 403 page.

### Limit directly with (...,limit_redirect='')

Also you can define the * limit_redirect='' * to return a special url.
**limit_redirect** can be a view

**myapp/views.py**

    from django.shortcuts import HttpResponse
    from apilimiter.decorators import limiter

    @limiter(limit_key='',limit_time=5, limit_redirect='/myapp/wrong')
    def index(request):
        return HttpResponse("decorators test")

    def wrong(request):
        return HttpResponse("You can view the page any more!")

**myapp/urls.py**

    from django.conf.urls import url, include
    from myapp import views

    urlpatterns = [
        url(r'^$', views.index),
        url(r'^wrong$', views.wrong),
        url(r'^mixin$', views.MyView.as_view()),
    ]

### Limit with Mixin

    from django.views.generic import View
    from apilimiter.mixin import LimiterMixin
    from django.shortcuts import HttpResponse

    class MyView(LimiterMixin, View):
        limit_time = 5
        limit_key = ''
        limit_redirect = ''

        def get(self, request):
            return HttpResponse('Mixin test')