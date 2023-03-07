"""
get, put:O(1)
delete: O(N)

get_random_val: O(1)

{
    'a': 5,
    'b': 5,
    'c': 6,
    'd': 5
}
"""

from random import randint


class OurDict():

    def __init__(self):
        self.keys = []
        self.values = []
        self.keys_dict = {}
        self.vals_dict = {}

    def __str__(self):
        return f"keys: {self.keys}\n" \
               f"values: {self.values}\n" \
               f"keys_dict: {self.keys_dict}\n" \
               f"vals_dict: {self.vals_dict}"

    def get(self, key: int):
        return self.keys_dict.get(key)

    def put(self, key, val):
        if not self.keys_dict.get(key):
            self.keys.append(key)
        self.keys_dict[key] = val

        if not self.vals_dict.get(val):
            self.values.append(val)
            self.vals_dict[val] = True

    def delete(self, key):
        val = self.keys_dict.get(key)
        if self.keys_dict.get(key):
            del self.keys_dict[key]
            self.keys.remove(key)
            self.values.remove(val)

    def get_random_val(self):
        l = len(self.values)
        index = randint(0, l - 1)
        val = self.values[index]
        return val

if __name__ == "__main__":
    ourDict = OurDict()
    ourDict.put('a', 5)
    print(ourDict)

    ourDict.put('b', 5)
    print(ourDict)

    ourDict.put('c', 6)
    print(ourDict)

    ourDict.put('d', 5)
    print(ourDict)

    for r in range(0, 10):
        print(ourDict.get_random_val())

    # ourDict.delete('a')
    # print(ourDict)
    #
    # ourDict.delete('e')
    # print(ourDict)
