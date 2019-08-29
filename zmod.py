
import nengo
import os
from datetime import datetime

def time_it():
  start = datetime.now()
  #some fun functino
  print(f"{datetime.now()-start}")


def mkdir(dir_in_quest):
  if not os.path.isdir(dir_in_quest):
    os.makedirs(dir_in_quest)

from shutil import copy
def aggregator():
  output_dir = "sim1/"
  lg = [x/100.0 for x in range(20,-2,-2)]
  le = [x/100.0 for x in range(20,-2,-2)]
  for i in lg:
    for j in le:
      source_dir_string = str(int(i*100)).zfill(2) + str(int(j*100)).zfill(2)
      for k in ["a","b","c","d","e"]:
        source_file = f"{source_dir_string}/{source_dir_string}{k}.png"
        copy(source_file, output_dir)


if __name__ == "__main__"
  # intrinsically_bursting
  n_ib = nengo.Izhikevich(reset_voltage=-55, reset_recovery=4)
  # chattering
  n_ch = nengo.Izhikevich(reset_voltage=-50, reset_recovery=2)
  # fast_spiking
  n_fs = nengo.Izhikevich(tau_recovery=0.1)
  # low_threshold_spiking
  n_lts = nengo.Izhikevich(coupling=0.25)
  # resonator
  n_rz = nengo.Izhikevich(tau_recovery=0.1, coupling=0.26)