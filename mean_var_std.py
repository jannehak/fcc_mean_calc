import numpy as np

def calculate(list):

    array = np.array(list).reshape(3, 3)

    calculations = {
        'mean': [np.mean(array, axis = 0).tolist(), np.mean(array, axis = 1).tolist(), np.mean(array).tolist()]
    }


    return calculations