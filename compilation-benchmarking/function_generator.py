import random

operators = ("and", "or", "not", "^")

def random_statement(num_vars, complexity):
    if num_vars < 2:
        raise ValueError("num_vars must be at least 2")

    if complexity < 1:
        raise ValueError("complexity must be at least 1")

    variables = ["x" + str(i) for i in range(num_vars)]
    statements = list(variables)

    for i in range(complexity):
        operator = random.choice(operators)
        s1 = statements[-1]
        s2 = random.choice(statements)
        if operator == "not":
            statements.append(f"not ({s1})")
        else:
            statements.append(f"({s1}) {operator} ({s2})")

    return statements[-1], variables

def random_classical_function(num_vars, complexity, name="f"):
    statement, variables = random_statement(num_vars, complexity)
    return f"""
@classical_function
def {name}({", ".join([f"{var} : Int1" for var in variables])}) -> Int1:
    return {statement}
    """

def generate_benchmark_functions(filename="benchmark_functions.py"):
    with open(filename, "w") as f:
        f.write("from qiskit.circuit.classicalfunction import classical_function\n")
        f.write("from qiskit.circuit.classicalfunction.types import Int1\n")
        for num_vars in range(2, 20):
            for complexity in range(num_vars - 1, num_vars + 15):
                f.write(random_classical_function(num_vars, complexity, name=f"f_v{num_vars}_c{complexity}"))
                f.write("\n")

if __name__ == "__main__":
    generate_benchmark_functions()