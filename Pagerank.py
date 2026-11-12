
import math


# ==========================================
# V1: NORMALIZED IN-DEGREE CITATION RANKING
# ==========================================

def v1_indegree_rank(V, edges):
    """
    Stage 1: Normalized in-degree citation ranking.
    """

    # Step 1: Initialize in-degree of every page to zero
    in_degree = [0] * V

    # Step 2: Count incoming links
    for source, destination in edges:
        if not (1 <= source <= V and 1 <= destination <= V):
            raise ValueError("Invalid page number")

        in_degree[destination - 1] += 1

    # Step 3: Normalize the scores
    total_links = sum(in_degree)

    if total_links == 0:
        return [0.0] * V

    normalized_scores = [
        degree / total_links for degree in in_degree
    ]

    return normalized_scores


# Test V1
V = 4

edges = [
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 1),
    (3, 4),
    (4, 4)
]

scores = v1_indegree_rank(V, edges)

print("V1: Normalized In-Degree Ranking")

for page, score in enumerate(scores, start=1):
    print(f"Page {page}: {score:.4f}")


# ==========================================
# V2: RAW MARKOV POWER ITERATION
# ==========================================

def v2_raw_markov_power(V, edges, num_iters):
    """
    Stage 2: Calculate page ranking using raw
    Markov power iteration.
    """

    # Step 1: Create adjacency list
    adjacency = {v: [] for v in V}

    # Step 2: Add outgoing links
    for source, destination in edges:
        if source not in adjacency or destination not in adjacency:
            raise ValueError("Invalid page number")

        adjacency[source].append(destination)

    # Step 3: Initialize equal probability
    n = len(V)
    pi = {v: 1 / n for v in V}

    # Step 4: Perform power iterations
    for iteration in range(num_iters):

        new_pi = {v: 0.0 for v in V}

        for page in V:

            outgoing = adjacency[page]

            if len(outgoing) > 0:

                probability = pi[page] / len(outgoing)

                for destination in outgoing:
                    new_pi[destination] += probability

        pi = new_pi

    return pi


# Test V2
V = [1, 2, 3, 4]

edges = [
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 1),
    (3, 4),
    (4, 4)
]

result = v2_raw_markov_power(V, edges, 1)

print("\nV2: PageRank After 1 Iteration")

for page, probability in result.items():
    print(f"Page {page}: {probability:.4f}")

print("Total probability:", sum(result.values()))


# ==========================================
# PART 3: ITERATION COMPLEXITY
# ==========================================

epsilon = 0.000001

print("\nIteration Complexity")

for alpha in [0.85, 0.99]:

    k = math.log(2 / epsilon) / -math.log(alpha)

    print("Alpha:", alpha)
    print("Iterations:", math.ceil(k))


# ==========================================
# PART 4: MEMORY USAGE COMPARISON
# ==========================================

V = 100000
E = 500000

# Dense adjacency matrix
dense = V * V

# Sparse adjacency list
sparse = E

ratio = dense / sparse

print("\nMemory Usage Comparison")

print("Dense matrix entries:", dense)
print("Sparse link entries:", sparse)
print("Memory ratio:", ratio, ": 1")