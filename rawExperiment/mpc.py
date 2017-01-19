import sys
sys.path.append('../../../sms-tools/software/models/')
from utilFunctions import wavread
from utilFunctions import wavwrite
from scipy.signal import get_window
import matplotlib.pyplot as plt
import numpy as np
import os
from pysndfx import AudioEffectsChain

destinationPath = os.path.join(os.path.dirname(os.path.realpath(__file__)),'finalSounds/')


def func():
	
	for file in os.listdir("."):
    		if file.endswith(".wav"):
        		(fs, x) = wavread(file)
			print file
			print fs
			
			filename = file.split('_')[0]			
			
			# Add or Modify window lengths here								
			timeLengths = np.array([8,16,32,64,128])
						

			windowLengths = fs*timeLengths/1000
			
			for i in range(timeLengths.size):
			
	
				length = windowLengths[i] 
				window = get_window('hamming', length) 
				fade_in = window[:length/2]
				fade_out = window[length/2:]
                        
				xA = [x[j]*fade_in[j] for j in range(length/2)]
                        	xA.extend(x[length/2:length])

                        	xD = x[:length/2].tolist()
                        	xD.extend([x[length/2 + j]*fade_out[j] for j in range(length/2)])
					
				#Linear Relation between Gain (dB) and Time Lengths			
				gain = AudioEffectsChain().gain(1)
				
				xA_Gain = AudioEffectsChain().gain(0.5*i + 0.5)
				xD_Gain = AudioEffectsChain().gain(0.5*i + 0.5)
				#xA_Gain = gain(np.asarray(xA))
				#xD_Gain = gain(np.asarray(xD))	

				#filename Handling of the format 'instrument_a|d_NNN_pitch.wav'
	                        filenameA = file.split('_')[0] + '_a_'+str(timeLengths[i])+'_'+ file.split('_')[1]
        	                filenameD = file.split('_')[0] + '_d_'+str(timeLengths[i])+'_'+ file.split('_')[1]	

        	                wavwrite(np.asarray(xA_Gain), fs, os.path.join(destinationPath,filenameA))
                	        wavwrite(np.asarray(xD_Gain), fs, os.path.join(destinationPath,filenameD))
			


func()	
