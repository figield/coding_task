from collections import defaultdict


def solution(s):
    max_distance = -1
    digrams = defaultdict(list)
    for i in range(len(s) - 1):
        digram = s[i:i + 2]
        digrams[digram].append(i)
        if len(digrams[digram]) > 1:
            distance = digrams[digram][-1] - digrams[digram][0]
            if distance > max_distance:
                max_distance = distance
    return max_distance

def solution2(s):
    max_distance = -1
    digrams = defaultdict(list)
    for i in range(len(s) - 1):
        digram = s[i:i + 2]
        if digrams.get(digram) is None:
            digrams[digram] = i
        else:
            distance = i - digrams[digram]
            if distance > max_distance:
                max_distance = distance
    return max_distance

if __name__ == "__main__":
    assert solution("aakmaakmakda") == 7
    assert solution("aaa") == 1
    assert solution("codility") == -1

    assert solution2("aakmaakmakda") == 7
    assert solution2("aaa") == 1
    assert solution2("codility") == -1