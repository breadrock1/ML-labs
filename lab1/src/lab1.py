"""
This database contains 76 attributes, but all published experiments refer to using a subset of 14 of them.
In particular, the Cleveland database is the only one that has been used by ML researchers to this date.
Dataset consists:
        > 1. age
        > 2. sex
        > 3. chest pain type (4 values)
        > 4. resting blood pressure
        > 5. serum cholestoral in mg/dl
        > 6. fasting blood sugar > 120 mg/dl
        > 7. resting electrocardiographic results (values 0,1,2)
        > 8. maximum heart rate achieved
        > 9. exercise induced angina
        > 10. oldpeak = ST depression induced by exercise relative to rest
        > 11. the slope of the peak exercise ST segment
        > 12. number of major vessels (0-3) colored by flourosopy
        > 13. thal: 3 = normal; 6 = fixed defect; 7 = reversable defect

    The goal: Trying to predict heart disease in the patient by thic dataset.
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


# No warnings about setting value on copy of slice
pd.options.mode.chained_assignment = None
# Display up to 14 columns of a dataframe
pd.set_option('display.max_columns', 14)
# Set default font size
plt.rcParams['font.size'] = 24
sns.set(font_scale=2)


def terminator_training(data):
    X = data[data.columns[:-1]]
    y = data['G3']
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    clf = KNeighborsClassifier(n_neighbors=5)
    clf.fit(X_train, y_train)
    clf.score(X_test, y_test)

    train_scores = {}
    test_scores = {}

    for n in range(1, 41):
        clf = KNeighborsClassifier(n_neighbors=n)
        clf.fit(X_train, y_train)
        current_train_score = clf.score(X_train, y_train)
        current_test_score = clf.score(X_test, y_test)
        train_scores[n] = current_train_score
        test_scores[n] = current_test_score

    # TODO: needs fix TypeError!!!
    plt.plot(train_scores.keys(), train_scores.values(), label='Обучающая выборка')
    plt.plot(test_scores.keys(), test_scores.values(), label='Тестовая выборка')
    plt.xlabel('Количество соседей')
    plt.ylabel('Доля верных ответов')
    plt.legend()
    plt.show()


# # Trying find relationships
# def building_categories(data):
#     types = data.dropna(subset=['G3'])
#     types = types['studytime'].value_counts()
#     types = list(types[types.values > 10].index)
#
#     figsize(20, 12)
#
#     for b_type in types:
#         subset = data[data['studytime'] == b_type]
#         sns.kdeplot(subset['G3'].dropna(), label=b_type, snade=False, alpha=0.8)
#
#     plt.xlabel('Final grade', size=20)
#     plt.ylabel('Study', size=12)
#     plt.title('Check relationships between study time and grades', size=20)
#
#
# # Trying delete defects
# def del_outlying_points(data):
#     bottom_boundary = data['G3'].describe()['25%']
#     # upper_boundary = data['G3'].describe()['max']
#     # iqr = upper_boundary - upper_boundary
#     data = data[(data['G3'] > bottom_boundary)]
#
#     return data


# Construct histograms for src data
def visual_histograms(column, bins, xlab, title):
    plt.style.use('mpl20')
    plt.hist(column.dropna(), bins=bins, color='skyblue')
    plt.xlabel(xlab)
    plt.ylabel('Num of students')
    plt.title(title)


# Drop selected tables which play no role
def drop_extra_columns(data):
    extra_columns = ['sex', 'thalach', 'exang', 'oldpeak', 'ca']
    data = data.drop(columns=list(extra_columns))

    return data


# Select columns that should be numeric and
# convert the data to specified type
def set_correct_types(data):
    booles = {'no': 0, 'yes': 1}

    for col in list(data.columns):
        if ('Medu' in col or 'Fedu' in col or 'traveltime' in col or 'studytime' in col
                or 'failures' in col or 'famrel' in col or 'freetime' in col or 'goout' in col
                or 'Dalc' in col or 'Walc' in col or 'G1' in col or 'G2' in col or 'G3' in col
                or 'health' in col):
            data[col] = data[col].astype(int)

        elif ('schoolsup' in col or 'famsup' in col or 'paid' in col or 'activities' in col
              or 'nursery' in col or 'higher' in col or 'internet' in col or 'romantic' in col):
            data[col].replace(booles, inplace=True)
            data[col] = data[col].astype(int)

        else:
            continue

    return data


def main():
    data = pd.read_csv("/home/akimg/Myprojects/ML_NeighborsClassifier-master/lab1/src/dataset/student-mat.csv")
    data = drop_extra_columns(data)
    data = set_correct_types(data)

    visual_histograms(data['studytime'], 12, 'Study time', 'Time of study')
    visual_histograms(data['G3'], 20, 'Grades', 'Final grade')

    # data = del_outlying_points(data)
    # visual_histograms(data['G3'], 19, 'Grades', 'Final grade')
    # building_categories(data)

    terminator_training(data)


if __name__ == '__main__':
    main()