import math


def displacements(supports: list[tuple]) -> list[dict]:
    nodes = []

    for node in supports:
        if not node:
            continue
        name = node[0]
        drift = math.ceil((float(node[1]) - 10300) / 250)
        drift = max(0, drift)
        nodes.append({"node": name, "drift": drift})

    return nodes
