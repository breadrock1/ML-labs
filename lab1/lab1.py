"""
Буду предсказывать оценки G4 студентов, из представленных характеристик в данной таблице:
    Medu - mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)
    Fedu - father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)
    studytime - weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)
    paid - extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)
    higher - wants to take higher education (binary: yes or no)
    internet - Internet access at home (binary: yes or no)
    G1 - first period grade (numeric: from 0 to 20)
    G2 - second period grade (numeric: from 0 to 20)
    G3 - final grade (numeric: from 0 to 20, output target)

    Цель работы: Найти закономерность между данными характеристиками, чтобы прогнозировать оценки студента

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
# Display up to 60 columns of a dataframe
pd.set_option('display.max_columns', 30)
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

    plt.plot(train_scores.keys(), train_scores.values(), label='Обучающая выборка')
    plt.plot(test_scores.keys(), test_scores.values(), label='Тестовая выборка')
    plt.xlabel('Количество соседей')
    plt.ylabel('Доля верных ответов')
    plt.legend()
    plt.show()


# Trying find relationships
def building_categories(data):
    types = data.dropna(subset=['G3'])
    types = types['studytime'].value_counts()
    types = list(types[types.values > 10].index)

    figsize(20, 12)

    for b_type in types:
        subset = data[data['studytime'] == b_type]
        sns.kdeplot(subset['G3'].dropna(), label=b_type, snade=False, alpha=0.8)

    plt.xlabel('Final grade', size=20)
    plt.ylabel('Study', size=12)
    plt.title('Check relationships between study time and grades', size=20)


# Trying delete defects
def del_outlying_points(data):
    bottom_boundary = data['G3'].describe()['25%']
    # upper_boundary = data['G3'].describe()['max']
    # iqr = upper_boundary - upper_boundary
    data = data[(data['G3'] > bottom_boundary)]

    return data


# Construct histograms for src data
def visual_histograms(column, bins, xlab, title):
    plt.style.use('mpl20')
    plt.hist(column.dropna(), bins=bins, color='skyblue')
    plt.xlabel(xlab)
    plt.ylabel('Num of students')
    plt.title(title)


# Drop selected tables which play no role
def drop_extra_columns(data):
    extra_columns = ['school', 'sex', 'age', 'address', 'famsize', 'Pstatus', 'Mjob',
                     'Fjob', 'guardian', 'reason', 'guardian', 'traveltime', 'failures',
                     'schoolsup', 'famsup', 'activities', 'nursery', 'romantic',
                     'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences']
    data = data.drop(columns=list(extra_columns))

    return data


# Select columns that should be numeric and
# convert the data to specified type
def set_correct_types(data):
    str_columns = ['paid', 'higher', 'internet']
    for col in str_columns:
        for elem in data[col]:
            if str(elem) == 'no': elem = 0
            elif str(elem) == 'yes': elem = 1
            else: elem = 0

    for col in list(data.columns):
        if ('Medu' in col or 'Fedu' in col or 'studytime' in col
                or 'G1' in col or 'G2' in col or 'G3' in col):
            data[col] = data[col].astype(int)

        # TODO: Overflow all values into columns, why?
        # elif 'paid' in col or 'higher' in col or 'internet' in col:
        #     data[col] = data[col].astype(str)
        else: continue

    return data


def main():
    data = pd.read_csv("/home/akimg/Myprojects/ML_NeighborsClassifier-master/lab1/dataset/student-mat.csv")
    data = set_correct_types(data)
    data = drop_extra_columns(data)

    visual_histograms(data['studytime'], 12, 'Study time', 'Time of study')
    visual_histograms(data['G3'], 20, 'Grades', 'Final grade')

    # data = del_outlying_points(data)
    # visual_histograms(data['G3'], 19, 'Grades', 'Final grade')
    #
    # building_categories(data)

    terminator_training(data)


if __name__ == '__main__':
    main()
