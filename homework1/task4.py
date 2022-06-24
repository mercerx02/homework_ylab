from itertools import combinations


def bananas(s):
    output = []
    dashes = len(s) - 6
    indices = combinations(range(len(s)), dashes)
    for ind in indices:
        word = "".join([x if i not in ind else "-" for i, x in enumerate(s)])
        if word.replace("-", "") == "banana":
            output.append(word)
    return output


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
