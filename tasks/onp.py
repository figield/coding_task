# ONP Input: 5 1 2 + 4 * + 3 -
# Output: 14


def operations(sym):
    if sym == "+":
        return lambda a, b: a + b
    if sym == "*":
        return lambda a, b: a * b
    if sym == "-":
        return lambda a, b: a - b


def op(arg1, arg2, operation) -> int:
    return operation(arg1, arg2)


def calculate_onp(cal: str) -> float:
    tokens = cal.split()
    stos = []
    for ch in tokens:
        if ch.isnumeric():
            stos.append(int(ch))
        else:
            r = op(stos[-2], stos[-1], operations(ch))
            stos = stos[:-2]
            stos.append(r)
    return stos[0]


def test_calculate_onp():
    assert calculate_onp("2 3 +") == 5
    assert calculate_onp("4 2 3 + *") == 20
    assert calculate_onp("5 1 2 + 4 * + 3 -") == 14


if __name__ == "__main__":
    test_calculate_onp()
