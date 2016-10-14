from .models import *
from django.http import HttpResponseForbidden, HttpResponseRedirect
from functools import wraps


def get_value(instance, key):
    if not key:
        return key
    keys = key.split('.')
    value = instance
    for k in keys:
        value = getattr(value, k)
    return value


def limiter(limit_key='', limit_time=0, limit_redirect=''):
    """
    limit_key: is a key for user which will find in <request>
    limit_time: max time before limit it
    limit_redirect: the redirect url of redirect view function
    """
    def func_warpper(func):
        @wraps(func)
        def warpper(request, *args, **kwargs):
            if limit_time > 0:
                function_name = func.__module__ + '.' + func.__name__
                value = "%s-%s" % (function_name,
                                   get_value(request, limit_key))
                limiter = DailyLimits.objects.filter(key=value).first()
                if not limiter:
                    DailyLimits.objects.create(
                        key=value,
                        times=0,
                    )
                else:
                    if limiter.times >= limit_time:
                        if limit_redirect:
                            if hasattr(limit_redirect, '__call__'):
                                return limit_redirect(request, *args, **kwargs)
                            return HttpResponseRedirect(limit_redirect)
                        return HttpResponseForbidden()
                    limiter.times += 1
                    limiter.save()
            return func(request, *args, **kwargs)
        return warpper
    return func_warpper
