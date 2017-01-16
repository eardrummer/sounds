import sys
sys.path.append('../../software/models/')
from utilFunctions import wavread
from scipy.signal import get_window
import matplotlib.pyplot as plt
import numpy as np
import os

def func():
	for file in os.listdir("."):
    		if file.endswith(".wav"):
        		(fs, x) = wavread(file)
			print file
			print fs
	_80ms = int(fs*.08)
	_1ms = int(fs*.001)
	_8ms = int(fs*.008)
	_16ms = int(fs*.016)
	_32ms = int(fs*.032)
	_64ms = int(fs*.064)
	_125ms = int(fs*.125)
	_250ms = int(fs*.25)
	_500ms = int(fs*.5)
	w = get_window('hamming', _80ms)
	fade_in = w[:_80ms/2]
	fade_out = w[_80ms/2:]


func()		




