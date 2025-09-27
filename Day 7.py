def find_combinations(limit=20):
    solutions = []
    for M in range(limit):
        for S in range(limit):
            for P in range(limit):
                G = 4*M + 2*S - 4*P
                if G < 0:
                    continue
                total_cost = 50*M + 40*S + 25*G + 10*P
                total_animals = M + S + G + P
                if total_animals > 0 and total_cost / total_animals == 30:
                    solutions.append((M, S, G, P))
    return solutions

sols = find_combinations(limit=10)
for sol in sols:
    print(f"Mules={sol[0]}, Sheep={sol[1]}, Goats={sol[2]}, Pigs={sol[3]}")
