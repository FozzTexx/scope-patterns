#!/usr/bin/env python
# Copyright 2016 by Chris Osborn <fozztexx@fozztexx.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2.1 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License at <http://www.gnu.org/licenses/> for
# more details.

import pyaudio
import numpy as np
from random import randint

p = pyaudio.PyAudio()

volume = 0.5     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 2.0   # in seconds, may be float
f = 440.0        # sine frequency, Hz, may be float

# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
                channels=2,
                rate=fs,
                output=True)

# generate samples, note conversion to float32 array
samples440 = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)

f = 660.0        # sine frequency, Hz, may be float
samples660 = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)

f = 220.0        # sine frequency, Hz, may be float
samples220 = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)

f = 880.0        # sine frequency, Hz, may be float
samples880 = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)

samples = [samples220, samples440, samples660, samples880]

# play. May repeat with different volume values (if done interactively)
try:
  while True:
    a = samples[randint(0,3)]
    b = samples[randint(0,3)]
    c = np.empty((a.size + b.size,), dtype=a.dtype)
    c[0::2] = a
    c[1::2] = b

    stream.write(volume*c)
except KeyboardInterrupt:
  stream.stop_stream()
  stream.close()

  p.terminate()
