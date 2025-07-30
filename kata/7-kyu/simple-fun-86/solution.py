def is_information_consistent(evidences):
    return all(
        not any(witness[d] == 1 for witness in evidences) or
        not any(witness[d] == -1 for witness in evidences)
        for d in range(len(evidences[0]))
    )
