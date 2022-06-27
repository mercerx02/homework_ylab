

from itertools import combinations

def bananas(s):
    word = "banana"
    out = []
    new_s = list(enumerate(s))

    for x in combinations(new_s, r=6):
        k = list(s)
        if ''.join(j[1] for j in x) == word:
            for i,ch in enumerate(s):
                if (i,ch) not in x:
                    k[i] = '-'
            out.append(''.join(k))
    return out

assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
