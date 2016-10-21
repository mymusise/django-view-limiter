Django-View-Limiter
===

Django-View-Limiter is a django app, which limit the time of every user to visit apis mainly.
Also you can limit the page view of apis directly.


Install Requires
===
- django >=1.9


Install
===

Django-View-Limiter is best installed via PyPI. To install the latest version, run:

	pip install apilimiter

or Install from github source:

	pip install git+git://github.com/mymusise/django-view-limiter


Starting
===

Adding apilimiter in you **your_project/settings.py**

    INSTALLED_APPS = (
            '...',
            'apilimiter',
        )

Then run migrate

    python manage.py migrate apilimiter

If you want to save the result every day, you should install a crontab like this:

	>crontab -e
	0 1 * * * cd /path/of/your/project/ && python manage.py collectlimiter >> limiter.log



Examples
===

Example is the best and fastest way to start.

## 1.Limit directly

You can call the limiter decorator directly to wrap your view function like that.
**myapp/views.py**

    from django.shortcuts import HttpResponse
    from apilimiter.decorators import limiter

    @limiter(key='',times=5)
    def index(request):
        return HttpResponse("decorators test")

If you view this api more than 5 times in a day, it will return the 403 page.


## 2.Limit with a key

* key  - The **key** parameter should be part of attribute or sub-attribute for the **request**.

If you want to limit the IP address in request(*request.META['REMOTE_ADDR']*), write like this.

**myapp/views.py**

    from django.shortcuts import HttpResponse
    from apilimiter.decorators import limiter

    @limiter(key="META['REMOTE_ADDR']",times=5, redirect='/myapp/wrong')
    def index(request):
        return HttpResponse("decorators test")

### Limit by user

What I want to limit first! But if you want to do this, you should call some authentication first.
Let's take an example of **django.contrib.auth**.

**myapp/views.py**

    from django.shortcuts import HttpResponse
    from apilimiter.decorators import limiter
    from django.contrib.auth.decorators import login_required

    @login_required(login_url="/admin/login/")
    @limiter(key='user.id',times=5, redirect='/myapp/wrong')
    def index(request):
        return HttpResponse("decorators test")



## 3.Limit with a redirect

Also you can define ** redirect='/...' ** to return a special url to replace the 403 page.

**myapp/views.py**

    from django.shortcuts import HttpResponse
    from apilimiter.decorators import limiter

    @limiter(key='',times=5, redirect='/myapp/wrong')
    def index(request):
        return HttpResponse("decorators test")

**myapp/urls.py**

    from django.conf.urls import url, include
    from myapp import views

    urlpatterns = [
        url(r'^$', views.index),
        url(r'^wrong$', views.wrong),
    ]

### **redirect** also can be a view

**myapp/views.py**

    @limiter(key='',times=5, redirect=wrong)
    def index(request):
        return HttpResponse("decorators test")

    def wrong(request):
        return HttpResponse("You can view the page any more!")


## 4.Limit with rate

You can control the rate with define **rate = 24 \* 60 \* 60** (s)
Here's the example which limit the index view 30 times per minute.

    @limiter(key='',times=30, rate=60)
    def index(request):
        return HttpResponse("decorators test")


## 5.Limit with Mixin

    from django.views.generic import View
    from apilimiter.mixin import LimiterMixin
    from django.shortcuts import HttpResponse

    class MyView(LimiterMixin, View):
        times = 5
        key = 'user.id'
        redirect = ''
        rate = 60

        def get(self, request):
            return HttpResponse('Mixin test')
