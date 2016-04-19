#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from func.function import work_function, plugin_manager


print(work_function(1, 2, 3))

manager = plugin_manager.set_plugin_state("plugin1", False)
print(work_function(1, 2, 3))

manager = plugin_manager.set_plugin_state("plugin2", False)
print(work_function(1, 2, 3))

manager = plugin_manager.set_plugin_state("plugin1", True)
print(work_function(1, 2, 3))
