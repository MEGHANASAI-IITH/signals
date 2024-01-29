import matplotlib.pyplot as plt
import numpy as np

# Function |H(jω)|
def magnitude_H(omega, R, L, C):
    return np.sqrt(R**2 + (omega * L - 1/(omega * C))**2)

# Circuit parameters
R_value = 15
L_value = 0.08
C_value = 0.00006

# Generate a range of angular frequencies up to 3000
omega_values = np.linspace(1, 10000, 10000)

# Calculate magnitude values for each angular frequency
magnitude_values = magnitude_H(omega_values, R_value, L_value, C_value)

# Plotting
plt.plot(omega_values, magnitude_values, label='$|H(j\omega)|$')
plt.xlabel('Angular Frequency ($\omega$)')
plt.ylabel('$|H(j\omega)|$')
plt.title('Magnitude Plot of $H(j\omega)$ for an RLC Circuit')
plt.legend()
plt.grid(True)

# Save the plot as a PDF file
plt.savefig('h_plot.pdf', bbox_inches='tight')
plt.show()

