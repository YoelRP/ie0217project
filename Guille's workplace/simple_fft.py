import numpy
import cmath
import scikits.audiolab as audio
import matplotlib.pyplot as plt

norm = lambda x: cmath.polar(x)[0]
(inputSignal, samplingRate, bits) = audio.oggread('Free_as_a_Bird.ogg')

norm = lambda x: cmath.polar(x)[0]

transformedSignal = numpy.fft.fft(signal)

plt.plot([norm(x) for x in transformedSignal])
plt.show()

#source http://jeremykun.com/2012/07/18/the-fast-fourier-transform/
