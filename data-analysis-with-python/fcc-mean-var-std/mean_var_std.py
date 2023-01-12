import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
        return list

    list = np.array([
        [list[0], list[1], list[2]],
        [list[3], list[4], list[5]],
        [list[6], list[7], list[8]]
    ])

    calculations = {
        "mean": [list.mean(axis = 0).tolist(), list.mean(axis = 1).tolist(), list.mean()],
        "variance": [list.var(axis = 0).tolist(), list.var(axis = 1).tolist(), list.var()],
        "standard deviation": [list.std(axis = 0).tolist(), list.std(axis = 1).tolist(), list.std()],
        "max": [list.max(axis = 0).tolist(), list.max(axis = 1).tolist(), list.max()],
        "min": [list.min(axis = 0).tolist(), list.min(axis = 1).tolist(), list.min()],
        "sum": [list.sum(axis = 0).tolist(), list.sum(axis = 1).tolist(), list.sum()]
    }

    return calculations