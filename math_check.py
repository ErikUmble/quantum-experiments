from sympy import symbols, Matrix, sqrt, I, exp, simplify, conjugate, cos, sin

# Step 1: Define symbols
q, n, t, theta, m = symbols('q n t theta m', real=True, positive=True)
x_t, y_t = symbols('x_t y_t', complex=True)

# Eigenvalues and eigenvectors of A
lambda_plus = (1 - q) + I * sqrt(q * (2 - q))
lambda_minus = (1 - q) - I * sqrt(q * (2 - q))

v_plus = Matrix([[q - 2], [-I * sqrt(q * (2 - q))]])
v_minus = Matrix([[q - 2], [I * sqrt(q * (2 - q))]])

# Step 2: Initial state z_0
z_0 = Matrix([[1 / sqrt(2**n)], [1 / sqrt(2**n)]])

# Step 3: Express z_0 in the eigenbasis of A
v_matrix = Matrix.hstack(v_plus, v_minus)
v_matrix_inv = simplify(v_matrix.inv())
a_coeffs = simplify(v_matrix_inv * z_0)

a_plus = a_coeffs[0]
a_minus = a_coeffs[1]

# Step 4: Compute z_t after t iterations
z_t = simplify(a_plus * exp(I * theta * t) * v_plus + a_minus * exp(-I * theta * t) * v_minus)

# Step 5: Calculate success probability
x_t = z_t[0]  # Successful amplitude
P_success = simplify(m * conjugate(x_t) * x_t)

# Output key results
print("Eigenvalues of A:")
print(f"lambda_+ = {lambda_plus}")
print(f"lambda_- = {lambda_minus}\n")

print("Coefficients in eigenbasis:")
print(f"a_+ = {a_plus}")
print(f"a_- = {a_minus}\n")

print("Amplitude after t iterations:")
print(f"x_t = {x_t}\n")

print("Success probability:")
print(f"P[success] = {P_success}")

P_success = m * conjugate(x_t) * x_t

# Step-by-step simplifications
steps = [
    ("Step 1", m * conjugate(x_t) * x_t),
    ("Step 2", m * (a_plus * exp(I * theta * t) * (q - 2) +
                    a_minus * exp(-I * theta * t) * (q - 2)) *
                  conjugate(a_plus * exp(I * theta * t) * (q - 2) +
                            a_minus * exp(-I * theta * t) * (q - 2))),
    ("Step 3", m * (q - 2)**2 *
                 (a_plus * conjugate(a_plus) +
                  a_plus * conjugate(a_minus) * exp(I * 2 * theta * t) +
                  a_minus * conjugate(a_plus) * exp(-I * 2 * theta * t) +
                  a_minus * conjugate(a_minus))),
    ("Step 4", m * (q - 2)**2 *
                 (abs(a_plus)**2 + abs(a_minus)**2 +
                  a_plus**2 * exp(I * 2 * theta * t) +
                  a_minus**2 * exp(-I * 2 * theta * t))),
    ("Step 5", m * (q - 2)**2 *
                 (abs(a_plus)**2 + abs(a_minus)**2 +
                  (4 * (q - 1) * cos(2 * theta * t) +
                   4 * sqrt(q * (2 - q)) * sin(2 * theta * t)) /
                  (4 * 2**n * q * (q - 2)**2))),
    ("Step 6", m * (q - 2)**2 *
                 (abs(a_plus)**2 + abs(a_minus)**2 +
                  2 * a_plus * conjugate(a_minus) *
                  (cos(theta * t)**2 - sin(theta * t)**2))),
]

# Compare each step
results = []
for name, step in steps:
    is_equal = simplify(P_success - step) == 0
    results.append((name, is_equal))

# Output results
for name, is_equal in results:
    print(f"{name}: {'Correct' if is_equal else 'Incorrect'}")
