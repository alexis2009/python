#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from pluginmanager import plugin_manager


@plugin_manager.decorator
def work_function(a, b, c):
    return a + b + c
