# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 09:22:57 2019

@author: chandlerzach
"""

from shutil import copy

output_dir = "sim1/"

lg = [x/100.0 for x in range(20,-2,-2)]
le = [x/100.0 for x in range(20,-2,-2)]

for i in lg:
  for j in le:
    source_dir_string = str(int(i*100)).zfill(2) + str(int(j*100)).zfill(2)
    for k in ["a","b","c","d","e"]:
      source_file = f"{source_dir_string}/{source_dir_string}{k}.png"
      copy(source_file, output_dir)



