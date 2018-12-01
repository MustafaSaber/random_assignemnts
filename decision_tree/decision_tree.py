import math
from collections import Counter
import numpy as np
import pandas
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def fill_strings(column, dataset):
    return dataset[column].fillna(dataset[column].value_counts().idxmax(), inplace=True)


def fill_numbers(column, dataset):
    return dataset[column].fillna(dataset[column].mean(skipna=True), inplace=True)


def digitalize(column,dataset):
    label, uniques = pandas.factorize(dataset[column], sort=True)
    dataset[column] = label
    return label


def process_data(dataset):
    fill_numbers("Age", dataset)
    fill_strings("Cabin", dataset)
    digitalize("Pclass", dataset)
    digitalize("Sex", dataset)
    digitalize("Age", dataset)
    digitalize("SibSp", dataset)
    digitalize("Parch", dataset)
    digitalize("Ticket", dataset)
    digitalize("Fare", dataset)
    digitalize("Cabin", dataset)
    digitalize("Embarked", dataset)
    return dataset.iloc[:, :]


def main():
    train_dataset = pandas.read_csv('~/PycharmProjects/ML/assignment1/Data/train.csv')
    test_dataset = pandas.read_csv('~/PycharmProjects/ML/assignment1/Data/test.csv')
    y = train_dataset['Survived']
    ids = np.array(test_dataset['PassengerId'])
    drop_ele = ['PassengerId', 'Name', 'Survived']
    train_dataset.drop(drop_ele, axis=1, inplace=True)
    drop_ele = ['PassengerId', 'Name']
    test_dataset.drop(drop_ele, axis=1, inplace=True)
    x = process_data(train_dataset)
    x_test = process_data(test_dataset)
    y_test = pandas.read_csv('~/PycharmProjects/ML/assignment1/Data/gender_submission.csv')['Survived']

    clf_entropy = DecisionTreeClassifier(criterion="entropy", random_state=0, max_depth=3)
    clf_entropy.fit(x, y)
    y_pred = clf_entropy.predict(x_test)

    with open('output.csv', 'w') as f:
        f.write('PassengerId' + ',' + 'Survived' + '\n')
        for i in range(len(y_pred)):
            f.write(str(ids[i]) + ',' + str(int(y_pred[i])) + '\n')
    print("Accuracy is ", accuracy_score(y_test, y_pred) * 100)


if __name__ == '__main__':
    main()
