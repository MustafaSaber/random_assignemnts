import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def read_process_data(file):
    col_names = ['x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'y']
    dataset = pd.read_csv(file, header=None, names=col_names)
    x, y = np.array([dataset['x' + str(i)] for i in range(0, 8)]).T, np.array(dataset['y'])
    return x, y


def get_val(data, current, k):
    def euclidean(var):
        return np.sum(np.sqrt(np.power(var[0] - current, 2)))

    data_sorted = sorted(data, key=euclidean)
    k_eighbours_output = [val[1] for val in data_sorted[:k]]
    return max(k_eighbours_output, key=k_eighbours_output.count)


def predict(x, y, x_test, y_test, k):
    data = list(zip(x, y))
    output = [get_val(data, current_data, k) for current_data in x_test]
    return np.count_nonzero(output == y_test)


def main():
    x_train, y_train = read_process_data('KnnData/TrainData.txt')
    x_test, y_test = read_process_data('KnnData/TestData.txt')
    accuracies_to_print = []
    for k in range(1, 10):
        current_accuracy = predict(x_train, y_train, x_test, y_test, k)
        percentage = current_accuracy / len(y_test)
        accuracies_to_print.append(percentage)
        print("K value: " + str(k))
        print("Number of correctly classified instances: ", current_accuracy)
        print("Instances: ", len(x_test))
        print("Accuracy: ", percentage)
        print("\n")
    plt.plot(accuracies_to_print)
    plt.show()


if __name__ == '__main__':
    main()
