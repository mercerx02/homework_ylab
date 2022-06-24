from math import prod


def count_find_num(factors: list, limit: int) -> list:
    products = [prod(factors)]
    for f in factors:
        for p in products:
            p *= f
            while p <= limit and p not in products:
                products.append(p)
                p *= f
    return [len(products), max(products)] if products[0] <= limit else []



primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []