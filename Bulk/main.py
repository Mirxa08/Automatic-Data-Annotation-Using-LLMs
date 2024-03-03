def water_jug_problem():
    initial_state = (0, 0)
    goal_quantity = 2
    goal_states = [(goal_quantity, y) for y in range(4)]

    current_level = [initial_state]
    visited = set()

    while current_level:
        next_level = []
        for state in current_level:
            x, y = state

            if x == goal_quantity:
                return state

            operations = [(4, y), (x, 3), (0, y), (x, 0),
                          (min(x + y, 4), max(0, x + y - 4)),
                          (max(0, x + y - 3), min(x + y, 3))]

            for operation in operations:
                if operation not in visited:
                    next_level.append(operation)
                    visited.add(operation)

        current_level = next_level

    return None

result = water_jug_problem()

if result:
    print("Goal state reached:", result)
else:
    print("Goal state not reachable.")
a={(0,0):[(4,0)(0,3)]}
print(a)
