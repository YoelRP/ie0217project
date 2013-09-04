import numpy
import cmath
import scikits.audiolab as audio
import matplotlib.pyplot as plt


# messing with audio


def processWithNumpy(signal):
   transformedSignal = numpy.fft.fft(signal)

   #cleanedSignal = numpy.fft.ifft(transformedSignal)
   #return numpy.array(cleanedSignal, dtype=numpy.float64)


# put this code in one of the two functions above to graph the transformed signal
# plt.plot([norm(x) for x in transformedSignal])
# plt.show() # blocks the program execution until the window is closed

norm = lambda x: cmath.polar(x)[0]

(inputSignal, samplingRate, bits) = audio.wavread('no_tree_ent.wav')


noisyFile = audio.Sndfile('no_tree_noisy.wav', 'w', audio.Format('wav'), 1, samplingRate)
noisyFile.write_frames(inputSignal)
noisyFile.close()

outputSignal = processWithNumpy(inputSignal)

outputFile = audio.Sndfile('no_tree_transformed.wav', 'w', audio.Format('wav'), 1, samplingRate)
outputFile.write_frames(outputSignal)
outputFile.close()

