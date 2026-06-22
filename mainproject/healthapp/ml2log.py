import pandas as pd
import numpy as np
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import cross_val_score, KFold, StratifiedKFold
from sklearn.pipeline import Pipeline

# url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"

# columns = [
#     'Pregnancies', 'Glucose', 'BloodPressure',
#     'SkinThickness', 'Insulin', 'BMI',
#     'DiabetesPedigreeFunction', 'Age', 'Outcome'
# ]

# df = pd.read_csv(url, header=None, names=columns)

# cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','BMI']

# df[cols] = df[cols].replace(0, np.nan)

# df.dropna(inplace=True)

# df = df.reset_index(drop=True)

# X = df.drop(columns=['Outcome']).values
# y = df['Outcome'].values

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=12, stratify=y)

# params = {
#     "model__tol": np.logspace(-5, -1, 50),
#     "model__C": np.logspace(-4, 4, 50),
#     "model__penalty": ['l1', 'l2'],
#     "model__solver": ['lbfgs', 'saga', 'liblinear'],
#     "model__class_weight": ["balanced", {0: 0.2, 1: 0.8}]
# }

# logistic = Pipeline(steps=[('scaler', StandardScaler()), ('model', LogisticRegression())])


# skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=12)

# logistreg_cv = RandomizedSearchCV(logistic, params, cv=skf, random_state=12)

# logistreg_cv.fit(X_train, y_train)

# joblib.dump(logistreg_cv, 'logistreg_Pima_cv.joblib')

logistreg_cv = joblib.load('logistreg_Pima_cv.joblib')


