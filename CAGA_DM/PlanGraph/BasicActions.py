#!/usr/bin/env python
# encoding: utf-8
"""
Basic actions that the system can perform

"""
__author__ = 'byu@ist.psu.edu (Bo Yu)'

import arcpy

import os
              
def remove_files(file_name):
    file_path = os.path.abspath(os.path.dirname(file_name))
    
    base_name = os.path.basename(file_name).rsplit(".", 1)[0]
    for f in os.listdir(file_path):
        if f.startswith(base_name):
            try:
                os.remove(os.path.join(file_path, f))
            except Exception,e:
                print e
    
    
def buffer(input, output, distance):
    remove_files(output)
    arcpy.Buffer_analysis(input, output, distance)