class Router(object):
    __instance = None

    def __new__(cls):
        if Router.__instance is None:
            Router.__instance = object.__new__(cls)
            Router.__instance.routes = {}

        return Router.__instance

    @classmethod
    def route(cls, route_str):
        def decorator(f):
            instance = cls()
            instance.routes[route_str] = f
            return f

        return decorator

    def serve(self, route, **kwargs):
        # TODO: Error handling
        # TODO: Logging
        self.routes.get(route)(**kwargs)
