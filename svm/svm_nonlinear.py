import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import pickle


def read_data(url):
    colnames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']
    irisdata = pd.read_csv(url, names=colnames)
    return irisdata


def process_data(data):
    x = data.drop('Class', axis=1)
    y = data['Class']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)
    return x_train, x_test, y_train, y_test


def train(model, xtrain, ytrain):
    model.fit(xtrain, ytrain)
    filename = 'finalized_model.pkl'
    pickle.dump(model, open(filename, 'wb'))


def predict(xtest, ytest):
    try:
        loaded_model = pickle.load(open('finalized_model.pkl', 'rb'))
        y_predicted = loaded_model.predict(xtest)
        print(confusion_matrix(ytest, y_predicted))
        print(classification_report(ytest, y_predicted))
        return np.count_nonzero(y_predicted == ytest)
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    data = read_data("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
    x_t, xt, y_t, yt = process_data(data)
    svclassifier = SVC(kernel='poly', degree=8)
    # svclassifier = SVC(kernel='rbf')
    # svclassifier = SVC(kernel='sigmoid')
    try:
        open('finalized_model.pkl')
        valid = predict(xt, yt)
        print((valid / len(yt)) * 100)
    except FileNotFoundError:
        print("File Not Found")
        train(svclassifier, x_t, y_t)
        valid = predict(xt, yt)
        print((valid / len(yt)) * 100)

