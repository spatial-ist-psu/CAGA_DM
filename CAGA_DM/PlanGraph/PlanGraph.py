#!/usr/bin/env python
# encoding: utf-8
"""
Plan Graph Model

"""
__author__ = 'byu@ist.psu.edu (Bo Yu)'


class PlanGraph():
    """model the plan graph"""
    def __init__(self):
        self.root = None
        self.focus = []
        self.agenda = []
        self.new_id = 0