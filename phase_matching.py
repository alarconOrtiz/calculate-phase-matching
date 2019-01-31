# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 15:05:30 2019
calc of phase matching
@author: malarcon
"""
import numpy as np
import matplotlib.pyplot as plt
import math
import time
# create 2 signals of direct coupler

delta_phi = (1/3)*np.pi
frequency = 352.21 * 10 **6
N_cycles  = 10
t = np.linspace(0, 1/frequency,10000)
cav1_fwd = np.sin(2*np.pi*frequency * t * N_cycles)
cav2_fwd = np.sin(2*np.pi*frequency * t * N_cycles + delta_phi)

#here the algorithm
start_time = time.process_time()
signals_product = np.dot(cav1_fwd,cav2_fwd)
cav1_norm = np.linalg.norm(cav1_fwd)
cav2_norm = np.linalg.norm(cav2_fwd)

phase_matching = math.acos((signals_product)/(cav1_norm*cav2_norm))
elapsed_time = time.process_time() - start_time
print("Elapsed time: %0.10f seconds." % elapsed_time)
print('================================================')
print('=== phase matching ='+str(phase_matching)+" rad")
print('=== Error:'+str(abs(delta_phi-phase_matching)))
print('================================================')

plt.plot(t,cav1_fwd,t,cav2_fwd)
plt.ylabel('Cav1 fwd & Cav2 fwd')
plt.xlabel('N samples')
plt.show()