import math
import matplotlib.pyplot as plt

def probability_of_success(t, theta, phi):
    return math.sin(t*theta + phi)**2


def plot(n, m, num_iterations=10**4):
    q = m / (2 ** (n-1))
    theta = math.atan(math.sqrt(q * (2-q)) / (1-q))
    phi = math.atan(math.sqrt(1 / (2-q)))

    x_values = range(1, num_iterations + 1)

    # Compute corresponding outputs
    y_values = [probability_of_success(x, theta, phi) for x in x_values]

    max_value = max(y_values)
    max_index = 1956
    print(f"Max value: {y_values[max_index]} at index {max_index}")

    # Plot the function
    plt.figure(figsize=(12, 8))
    plt.plot(x_values, y_values, color='blue', marker='.')
    plt.title('P[success] for k Grover Iterations')
    plt.xlabel('k')
    plt.ylabel('P[success]')
    plt.legend()
    plt.grid(True)
    plt.show()
if __name__ == "__main__":
    plot(25, 2)