# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:28:11 2019
Testing change, adding zfill(2) to improve file naming scheme
@author: chandlerzach
"""

import os
import matplotlib.pyplot as plt


def mkdir(dir_in_quest):
  if not os.path.isdir(dir_in_quest):
    os.makedirs(dir_in_quest)

lg = [x/100.0 for x in range(20,-2,-2)]
le = [x/100.0 for x in range(20,-2,-2)]

for i in lg:
  for j in le:
    dir_string = str(int(i*100)).zfill(2) + str(int(j*100)).zfill(2)
    mkdir(dir_string)
    for k in ["a","b","c","d","e"]:
      file_name = dir_string + k
      input_args = f"{i} {j} {dir_string +'/'+ file_name}"
      runfile('C:/Users/chandlerzach/BGModel/syllable_sequencing_altered.py',
              args=input_args,
              wdir='C:/Users/chandlerzach/BGModel')



