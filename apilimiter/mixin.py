from .decorators import limiter


class LimiterMixin(object):
    key = ''
    rate = 24 * 60 * 60
    times = 0
    redirect = ''

    def check_view_method(self, key):
        return hasattr(self, key)

    def set_limmiter(self, key):
        handle = getattr(self, key)
        setattr(self, key, limiter(
            rate=self.rate,
            key=self.key,
            times=self.times,
            redirect=self.redirect)(handle))

    def __init__(self, *args, **kwargs):
        list(map(self.set_limmiter, filter(self.check_view_method, self.http_method_names)))
        return super(LimiterMixin, self).__init__(*args, **kwargs)
