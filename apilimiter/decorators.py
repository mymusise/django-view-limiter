from django.http import HttpResponseForbidden, HttpResponseRedirect
from functools import wraps
from functools import reduce
from .models import *
import time


def get_key_value(k, key):
    return key.get(k) if type(key) == dict else getattr(key, k)


def get_instance_value(instance, key):
    if not key:
        return key
    keys = key.split('.')
    value = instance
    value = reduce(lambda v, k: get_key_value(k, v), keys, value)
    return value


def limiter(key='', times=0, redirect='', rate=(24 * 60 * 60)):
    """
    @key: is a key for user which will find in <request>
    @time: max time before limit it
    @redirect: the redirect url of redirect view function
    """
    def func_warpper(func):
        @wraps(func)
        def warpper(request, *args, **kwargs):
            function_name = func.__module__ + '.' + func.__name__
            value = "%s-%s" % (function_name,
                               get_instance_value(request, key))
            limiter = DailyLimits.objects.filter(key=value).first()
            if not limiter:
                DailyLimits.objects.create(
                    key=value,
                    times=1,
                    time_left=time.time() + rate,
                )
            else:
                now = time.time()
                if limiter.time_left <= now:
                    limiter.time_left = now + rate
                    limiter.times = 0
                if limiter.times >= times > 0 and now < limiter.time_left:
                    if redirect:
                        if hasattr(redirect, '__call__'):
                            return redirect(request, *args, **kwargs)
                        return HttpResponseRedirect(redirect)
                    return HttpResponseForbidden()
                limiter.times += 1
                limiter.save()
            return func(request, *args, **kwargs)
        return warpper
    return func_warpper
