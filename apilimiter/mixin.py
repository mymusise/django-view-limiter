from .decorators import limiter


class LimiterMixin(object):
    limit_time = 0
    limit_key = ''
    limit_redirect = ''

    def __init__(self):
        for key in self.__dir__():
            if key in self.http_method_names:
                handle = getattr(self, key)
                setattr(self, key, limiter(
                    limit_key=self.limit_key,
                    limit_time=self.limit_time,
                    limit_redirect=self.limit_redirect)(handle))
        print("Limit", self.limit_time)
