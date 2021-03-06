from sklearn.datasets import load_breast_cancer

from learn_ml.linear_model.logistics import LogisticsRegression


def test_predict_proba():
    X, y = load_breast_cancer(return_X_y=True)
    clf = LogisticsRegression()
    clf.fit(X, y)
    y_prob = clf.predict_proba(X)
    print(y_prob.shape)


def test_predict():
    X, y = load_breast_cancer(return_X_y=True)
    clf = LogisticsRegression()
    clf.fit(X, y)
    y_pred = clf.predict(X)
    print(y_pred.shape)


def test_fit():
    X, y = load_breast_cancer(return_X_y=True)
    clf = LogisticsRegression(optimizer='gd', alpha=1)
    clf.fit(X, y)
    print(clf.n_iter)
    print(clf.coef)
