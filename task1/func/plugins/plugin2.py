# -*- coding: utf-8 -*-

from ..iplugin import IPlugin


class Plugin2(IPlugin):
    def _plugin_work(self, f, *args, **kwargs):
        a, b, c = args

        res = f(3*a, 3*b, 3*c)

        return 3*res
