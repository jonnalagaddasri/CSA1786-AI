class MapColoringCSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def is_consistent(self, assignment, var, color):
        for constraint in self.constraints.get(var, []):
            if assignment.get(constraint) == color:
                return False
        return True

    def backtracking_search(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment

        unassigned_vars = [var for var in self.variables if var not in assignment]

        first_unassigned_var = unassigned_vars[0]
        for color in self.domains[first_unassigned_var]:
            if self.is_consistent(assignment, first_unassigned_var, color):
                assignment[first_unassigned_var] = color
                result = self.backtracking_search(assignment)
                if result is not None:
                    return result
                del assignment[first_unassigned_var]
        return None

    def solve(self):
        assignment = {}
        return self.backtracking_search(assignment)


if __name__ == "__main__":
    variables = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
    domains = {
        "WA": ["red", "green", "blue"],
        "NT": ["red", "green", "blue"],
        "SA": ["red", "green", "blue"],
        "Q": ["red", "green", "blue"],
        "NSW": ["red", "green", "blue"],
        "V": ["red", "green", "blue"],
        "T": ["red", "green", "blue"],
    }
    constraints = {
        "WA": ["NT", "SA"],
        "NT": ["WA", "SA", "Q"],
        "SA": ["WA", "NT", "Q", "NSW", "V"],
        "Q": ["NT", "SA", "NSW"],
        "NSW": ["Q", "SA", "V"],
        "V": ["SA", "NSW"],
    }

    csp = MapColoringCSP(variables, domains, constraints)
    solution = csp.solve()

    if solution is not None:
        print("Solution found:")
        for var, color in solution.items():
            print(f"{var}: {color}")
    else:
        print("No solution found.")
