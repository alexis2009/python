# -*- coding: utf-8 -*-


class IPlugin(object):
    def __init__(self):
        self.is_activated = True

    def activate(self):
        self.is_activated = True

    def deactivate(self):
        self.is_activated = False

    def decorate(self, func):
        def _wrapper(*args, **kwargs):
            if self.is_activated:
                return self._plugin_work(func, *args, **kwargs)
            else:
                return func(*args, **kwargs)
        return _wrapper

    def _plugin_work(self, func, *args, **kwargs):
        raise RuntimeError("_plugin_work must be implemented in {}".format(
            self.__class__.__name__))