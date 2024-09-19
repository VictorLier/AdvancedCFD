import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('Assignment 1/Fixed Data/Upstream Lift.csv', delimiter=',', skip_header=1)

plt.plot(data[:,0], data[:,1])
plt.xlabel('Time (s)')
plt.ylabel('Upstream Lift (N)')
plt.show()

# FFT
y = data[:,1]
Fs = 10
n = len(y)
k = np.arange(n)
T = n/Fs
frq = k/T
frq = frq[range(n//2)]
Y = np.fft.fft(y)/n
Y = Y[range(n//2)]

plt.plot(frq,abs(Y))
plt.xlabel('Freq (Hz)')
plt.ylabel('|Y(freq)|')
plt.show()

np.savetxt('Assignment 1/Fixed Data/Upstream Lift.txt', np.column_stack((frq, abs(Y))), delimiter=' ', fmt='%s')


# Find the frequency with the highest amplitude
max_amplitude = np.max(abs(Y))
max_amplitude_index = np.where(abs(Y) == max_amplitude)
max_amplitude_freq = float(frq[max_amplitude_index])
print('Max amplitude:', max_amplitude)
print('Frequency with max amplitude:', max_amplitude_freq)

# Find spring stifness
import sympy as sp
# Define the variables
omega, k, m, k_0 = sp.symbols('omega k m k_0')

eq1 = sp.Eq(omega, sp.sqrt(k/m))
k_0 = sp.solve(eq1, k)[0]
print('k_0:', k_0)

print(k_0.subs({omega: max_amplitude_freq * 2 * np.pi, m: 4/np.pi}))