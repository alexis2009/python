#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from collections import OrderedDict
from iplugin import IPlugin
from plugins import *
from plugins import plugins_order_list


class PluginManager(object):
    def __init__(self):
        subclasses = {subclass.__name__.lower(): subclass for subclass
                      in IPlugin.__subclasses__()}

        self.plugins = OrderedDict(
            (plugin_name, subclasses[plugin_name]())
            for plugin_name in plugins_order_list
            if plugin_name in subclasses
        )

    def set_plugin_state(self, name, state):
        if state:
            self.plugins[name].activate()
        else:
            self.plugins[name].deactivate()

    def decorator(self, func):
        for plugin in reversed(self.plugins.values()):
            func = plugin.decorate(func)

        return func


plugin_manager = PluginManager()
