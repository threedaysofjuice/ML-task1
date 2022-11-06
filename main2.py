import numpy as np
import random

sets = ["set1", "set2", "set3"]


def create_data(number):
    dataset = []
    for i in range(0, number):
        set = [i + np.random.normal(0, 0.2), i + np.random.normal(0, 0.2), random.choice(sets),
               i + np.random.normal(0, 0.2), np.random.random_sample() * 20000 - 10000, i]
        dataset.append(set)
    random.shuffle(dataset)
    return dataset


def write_data(dataset):
    data_str = ""
    for set in dataset:
        data_str += str(set) + "\n"

    with open("dataset.txt", "w+") as file:
        file.write(data_str)


if __name__ == '__main__':
    dataset = create_data(1500)
    for set in dataset:
        print(set)

    write_data(dataset)