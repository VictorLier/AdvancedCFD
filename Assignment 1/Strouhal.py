import sympy as sp

# Define the variables
St, f, L, U = sp.symbols('St f L U')

#Strouhal number
eq1 = sp.Eq(St, f*L/U)

# Solve the equation
f = sp.solve(eq1, f)

# Values
L_val = 1
U_val = 1
St_val = 0.2

print(f[0].subs({L: L_val, U: U_val, St: St_val}))