from .decorators import limiter


class LimiterMixin(object):
    limit_time = 0
    limit_key = ''
    limit_redirect = ''

    def check_view_method(self, key):
        return hasattr(self, key)

    def set_limmiter(self, key):
        handle = getattr(self, key)
        setattr(self, key, limiter(
            limit_key=self.limit_key,
            limit_time=self.limit_time,
            limit_redirect=self.limit_redirect)(handle))

    def __init__(self, *args, **kwargs):
        map(self.set_limmiter, filter(self.check_view_method, self.http_method_names))
        return super(LimiterMixin, self).__init__(*args, **kwargs)
