import numpy as np
import random
import string

sets = ["set 1", "set 2", "set 3", "set 4", "set 5", "set 6"]


def createDataTable(max):
    data = []
    letters = string.punctuation
    for i in range(0, max):
        row = [i + np.random.normal(0, 0.35), i + 1 + np.random.normal(0, 0.35), i + 2 + np.random.normal(0, 0.35),
               random.choice(sets), ''.join(random.choice(letters) for i in range(10)), i + 4]
        data.append(row)
    return data


if __name__ == '__main__':
    data = createDataTable(1500)
    for set in data:
        print(set)

    data_to_write = ""
    for set in data:
        data_to_write += str(set) + "\n"

    with open("result.txt", "w+") as file:
        file.write(data_to_write)