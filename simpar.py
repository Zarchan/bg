# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 23:55:51 2019

@author: chandlerzach
"""

import os
import sim
from datetime import datetime
import string
from joblib import Parallel, delayed
import multiprocessing

def mkdir(dir_in_quest):
  if not os.path.isdir(dir_in_quest):
    os.makedirs(dir_in_quest)

def auto_standard(list_lg=None, list_le=None, trials=4, sim_time=6):
  lg, le = list_lg, list_le
  if list_lg is None:
    lg = [x/100.0 for x in range(20,-2,-2)]
  if list_le is None:
    le = [x/100.0 for x in range(20,-2,-2)]
  trial_names = string.ascii_letters[:trials]
  for i in lg:
    for j in le:
      dir_string = str(int(i*100)).zfill(2) + str(int(j*100)).zfill(2)
      mkdir(dir_string)
      for k in trial_names:
        file_name = dir_string + k
        sim.simulate(lg=i, le=j, save_dir=f"{dir_string +'/'+ file_name}", sim_time=sim_time)

def auto_test():
  start = datetime.now()
  lg = [x/100.0 for x in range(20,16,-2)]
  le = [x/100.0 for x in range(20,16,-2)]
  auto_standard(lg,le,4,3)
  print(datetime.now() - start)

def parallel_sim(list_lg=None, list_le=None, trials=4, sim_time=6):
  lg, le = list_lg, list_le
  if list_lg is None:
    lg = [x/100.0 for x in range(20,-2,-2)]
  if list_le is None:
    le = [x/100.0 for x in range(20,-2,-2)]
  trial_names = string.ascii_letters[:trials]

  num_cores = multiprocessing.cpu_count()
  jobs = []
  for i in lg:
    for j in le:
      dir_string = str(int(i*100)).zfill(2) + str(int(j*100)).zfill(2)
      mkdir(dir_string)
      for k in trial_names:
        file_name = dir_string + k
        jobs.append({"lg":i, "le":j, "save_dir":f"{dir_string +'/'+ file_name}", "sim_time": sim_time})

  Parallel(n_jobs=num_cores)(delayed(sim.simulate)(**i) for i in jobs)

def parallel_test():
  start = datetime.now()
  lg = [x/100.0 for x in range(20,16,-2)]
  le = [x/100.0 for x in range(20,16,-2)]
  parallel_sim(lg,le,2,2)
  print(datetime.now() - start)


if __name__ == "__main__":
  start = datetime.now()
  parallel_sim()
  print(f"Time elapsed for full simulation {datetime.now() - start}")













