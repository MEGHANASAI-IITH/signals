import matplotlib.pyplot as plt
import numpy as np

# Function |H(jω)|
def magnitude_H(omega, R, L, C):
    return np.sqrt(R**2 + (omega * L - 1/(omega * C))**2)

R_value = 15
L_value = 0.08
C_value = 0.00006

omega_values = np.linspace(1, 1000, 10000)

magnitude_values = magnitude_H(omega_values, R_value, L_value, C_value)

plt.plot(omega_values, magnitude_values, label='|H(jω)|')

plt.xlabel('Angular Frequency ($\omega$)')
plt.ylabel('|H(j$\omega$)|')
plt.title('Magnitude Plot of H(j$\omega$) for an RLC Circuit')

plt.legend()
plt.grid(True)

plt.savefig('magnitude_plot.pdf', bbox_inches='tight')
plt.show()
