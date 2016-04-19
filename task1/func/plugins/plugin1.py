# -*- coding: utf-8 -*-

import collections
from ..iplugin import IPlugin


class Plugin1(IPlugin):
    def _plugin_work(self, f, *args, **kwargs):
        print 'Arguments: {}'.format(args)
        print 'Keyword arguments: {}'.format(kwargs)

        results = f(*args)

        if not isinstance(results, collections.Sequence):
            results = (results,)
        return ', '.join([str(result) for result in results])
