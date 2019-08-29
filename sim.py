# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 23:55:51 2019

@author: chandlerzach
"""

import matplotlib.pyplot as plt
import numpy as np
from sys import argv
import nengo
from nengo import spa

class Delay(object):
    def __init__(self, dimensions, timesteps=50):
        self.timesteps = timesteps
        self.dimensions = dimensions
        self.history = None
        self.reset()
    def step(self, t, x):
        self.history = np.roll(self.history, -self.dimensions)
        self.history[-1] = x
        return self.history[0]
    def reset(self):
        self.history = np.zeros((self.timesteps, self.dimensions))

def simulate(lg = .2, le = .2, save_dir = None, sim_time = 6):
  nengo.rc.set('progress', 'progress_bar',
              'nengo.utils.progress.TerminalProgressBar')
  d = 64
  n = 50*d

  # class for delayed connection
  delay_t = 0.2   # 200 ms pro Silbe


  dt = 0.001
  delay = Delay(dimensions=d, timesteps=int(delay_t / dt))
  
  # SPA-Model:
  model = spa.SPA()
  with model:
      # --------------------- SPA representations ----------------
  
      # High level SPs
      model.visual   = spa.Buffer(dimensions=d)
      model.phonemic = spa.Buffer(dimensions=d)
      model.premotor = spa.Buffer(dimensions=d)
      model.audiexpect = spa.Buffer(dimensions=d)
      model.motor  = spa.Buffer(dimensions=d)
      model.motor1 = nengo.Ensemble(n, dimensions=d)
      model.motor2 = nengo.Ensemble(n, dimensions=d)
      model.somato = spa.Buffer(dimensions=d)
  
      model.delaynode = nengo.Node(delay.step, size_in=d, size_out=d)
  
      # High level routing
      actions = spa.Actions(
          'dot(visual, BA) --> phonemic=BA',
          '0.2 --> phonemic=NEUTRAL, premotor=NEUTRAL, audiexpect=NEUTRAL, motor=NEUTRAL',
          'dot(phonemic, BA) --> premotor=BA, motor=BA_EXEC, audiexpect=BA',
          'dot(phonemic, DA) --> premotor=DA, motor=DA_EXEC, audiexpect=DA',
          'dot(phonemic, GA) --> premotor=GA, motor=GA_EXEC, audiexpect=GA',
          'dot(phonemic, PA) --> premotor=PA, motor=PA_EXEC, audiexpect=PA',
          'dot(phonemic, TA) --> premotor=TA, motor=TA_EXEC, audiexpect=TA',
          'dot(phonemic, KA) --> premotor=KA, motor=KA_EXEC, audiexpect=KA',
          'dot(somato, BA_EXEC) --> phonemic=DA',
          'dot(somato, DA_EXEC) --> phonemic=GA',
          'dot(somato, GA_EXEC) --> phonemic=PA',
          'dot(somato, PA_EXEC) --> phonemic=TA',
          'dot(somato, TA_EXEC) --> phonemic=KA',
          'dot(somato, KA_EXEC) --> phonemic=BA',
  
      )
      nengo.networks.actionselection.Weights.lg = lg
      nengo.networks.actionselection.Weights.le = le
      nengo.networks.actionselection.Weights.wt = 1.0
      nengo.networks.actionselection.Weights.wp = 0.9
      nengo.networks.actionselection.Weights.wp_snr = 0.9 # not used yet
  
      model.bg = spa.BasalGanglia(actions)
      model.thalamus = spa.Thalamus(model.bg)
  
      # model delay:
      nengo.Connection(model.motor.state.output, model.motor1, synapse=0.01)
  
      # no delay:
      #nengo.Connection(model.motor1, model.motor2, synapse=0.01)
  
      # delay:
      nengo.Connection(model.motor1, model.delaynode)
      nengo.Connection(model.delaynode, model.motor2)
  
      nengo.Connection(model.motor2, model.somato.state.input, synapse=0.01)
  
      # Provide input to high-level
      def start(t):
          if t < 0.25:
              return 'ZERO'
          elif t < 0.45:
              return 'BA'
          else:
              return 'ZERO'
  
      model.input = spa.Input(visual=start)
  
      # set up probes
      visual   = nengo.Probe(model.visual.state.output, synapse=0.03)
      phonemic = nengo.Probe(model.phonemic.state.output, synapse=0.03)
      premotor = nengo.Probe(model.premotor.state.output, synapse=0.03)
      audiexpect = nengo.Probe(model.audiexpect.state.output, synapse=0.03)
      motor = nengo.Probe(model.motor.state.output, synapse=0.03)
      somato = nengo.Probe(model.somato.state.output, synapse=0.03)
  
  
  
  with nengo.Simulator(model) as sim:
    sim.run(sim_time)
  
  plt.figure(figsize=(18, 16))
  plt.subplot(6, 1, 1)
  plt.plot(sim.trange(), model.similarity(sim.data, visual))
  plt.legend(model.get_input_vocab('visual').keys, fontsize='x-small')
  plt.ylabel('Visual')
  plt.subplot(6, 1, 2)
  plt.plot(sim.trange(), model.similarity(sim.data, phonemic))
  plt.legend(model.get_input_vocab('phonemic').keys, fontsize='x-small')
  plt.ylabel('Phonemic')
  plt.subplot(6, 1, 3)
  plt.plot(sim.trange(), model.similarity(sim.data, audiexpect))
  plt.legend(model.get_input_vocab('audiexpect').keys, fontsize='x-small')
  plt.ylabel('Audi_expect')
  plt.subplot(6, 1, 4)
  plt.plot(sim.trange(), model.similarity(sim.data, premotor))
  plt.legend(model.get_input_vocab('premotor').keys, fontsize='x-small')
  plt.ylabel('Premotor')
  plt.subplot(6, 1, 5)
  plt.plot(sim.trange(), model.similarity(sim.data, motor))
  plt.legend(model.get_input_vocab('motor').keys, fontsize='x-small')
  plt.ylabel('Motor')
  plt.subplot(6, 1, 6)
  plt.plot(sim.trange(), model.similarity(sim.data, somato))
  plt.legend(model.get_input_vocab('somato').keys, fontsize='x-small')
  plt.ylabel('Somato')

  if save_dir is not None:
    plt.savefig(save_dir)

  plt.close()



if __name__ == "__main__":
  simulate()