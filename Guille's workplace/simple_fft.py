import numpy
import cmath
import scikits.audiolab as audio
import matplotlib.pyplot as plt

#from music to array
(inputsignal, samplingrate, bits) = audio.oggread('Free_as_a_Bird.ogg')

#fast furier transform using numpy
transformedsignal = numpy.fft.fft(inputsignal)

#plot using matlibplot
norm = lambda x: cmath.polar(x)[0]
plt.plot([norm(x) for x in transformedsignal])
plt.show()

#source http://jeremykun.com/2012/07/18/the-fast-fourier-transform/
