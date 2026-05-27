"""
Assignment 5 - Part 4
Different Implementation of Bayesian Network

Example Used: Medical Diagnosis Network

Variables:
Flu
Cold
Fever
Cough
Fatigue

Query Example:
P(Flu | Fever=True, Cough=True, Fatigue=True)

Run:
    python medical_bayesian_network.py
"""


class BayesianNetwork:
    def __init__(self):
        self.variables = []
        self.parents = {}
        self.cpt = {}

    def add_variable(self, variable, parents, cpt):
        self.variables.append(variable)
        self.parents[variable] = parents
        self.cpt[variable] = cpt

    def probability(self, variable, value, evidence):
        parent_list = self.parents[variable]

        if len(parent_list) == 0:
            true_probability = self.cpt[variable][()]
        else:
            key = tuple(evidence[parent] for parent in parent_list)
            true_probability = self.cpt[variable][key]

        if value is True:
            return true_probability

        return 1 - true_probability


def enumerate_all(variables, evidence, network):
    if len(variables) == 0:
        return 1.0

    first = variables[0]
    remaining = variables[1:]

    if first in evidence:
        probability = network.probability(first, evidence[first], evidence)
        return probability * enumerate_all(remaining, evidence, network)

    total = 0

    for value in [True, False]:
        new_evidence = evidence.copy()
        new_evidence[first] = value

        probability = network.probability(first, value, new_evidence)
        total += probability * enumerate_all(remaining, new_evidence, network)

    return total


def inference(query_variable, evidence, network):
    distribution = {}

    for value in [True, False]:
        new_evidence = evidence.copy()
        new_evidence[query_variable] = value

        distribution[value] = enumerate_all(network.variables, new_evidence, network)

    total = distribution[True] + distribution[False]

    distribution[True] = distribution[True] / total
    distribution[False] = distribution[False] / total

    return distribution


def build_medical_network():
    network = BayesianNetwork()

    network.add_variable(
        "Flu",
        [],
        {
            (): 0.08
        }
    )

    network.add_variable(
        "Cold",
        [],
        {
            (): 0.20
        }
    )

    network.add_variable(
        "Fever",
        ["Flu", "Cold"],
        {
            (True, True): 0.95,
            (True, False): 0.90,
            (False, True): 0.40,
            (False, False): 0.05
        }
    )

    network.add_variable(
        "Cough",
        ["Flu", "Cold"],
        {
            (True, True): 0.90,
            (True, False): 0.70,
            (False, True): 0.80,
            (False, False): 0.10
        }
    )

    network.add_variable(
        "Fatigue",
        ["Flu"],
        {
            (True,): 0.85,
            (False,): 0.20
        }
    )

    return network


def main():
    network = build_medical_network()

    evidence = {
        "Fever": True,
        "Cough": True,
        "Fatigue": True
    }

    result = inference("Flu", evidence, network)

    print("MEDICAL BAYESIAN NETWORK")
    print("Query: P(Flu | Fever=True, Cough=True, Fatigue=True)")
    print("P(Flu=True):", round(result[True], 5))
    print("P(Flu=False):", round(result[False], 5))


if __name__ == "__main__":
    main()
