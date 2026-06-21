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


from ucimlrepo import fetch_ucirepo 
  
# # fetch dataset 
# cdc_diabetes_health_indicators = fetch_ucirepo(id=891) 
  
# # data (as pandas dataframes) 
# X = cdc_diabetes_health_indicators.data.features 
# y = cdc_diabetes_health_indicators.data.targets 

# X = X.values
# y = np.ravel(y)

# logistic = Pipeline(steps=[('scaler', StandardScaler()),
#                             ('model', LogisticRegression(max_iter=200))])

# params = {
#     "model__tol": np.logspace(-5, -2, 50),
#     "model__C": np.logspace(-4, 4, 50),
#     "model__l1_ratio": [0,1],
#     "model__solver": ['saga'],
#     "model__class_weight": ["balanced", {0:0.15, 1:0.85},{0: 0.2, 1: 0.8}, {0:0.3, 1:0.7}],
#     "model__max_iter": [100, 200, 500]
# }

# kf = StratifiedKFold(n_splits= 5, shuffle=True, random_state=12)

# logreg_cv = RandomizedSearchCV(logistic, params, cv=kf, random_state=12, n_iter=30, scoring='f1', n_jobs=-1, refit=True)

# X_train, X_test , y_train, y_test = train_test_split( X, y, test_size=0.3, random_state=12)

# logreg_cv.fit(X_train, y_train)

logreg_cv=joblib.load('logreg_cv.joblib')
