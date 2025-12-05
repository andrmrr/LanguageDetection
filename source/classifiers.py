from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder

# You may add more classifier methods replicating this function
def applyNaiveBayes(X_train, y_train, X_test):
    clf = MultinomialNB()
    clf.fit(X_train, y_train)
    y_predict = clf.predict(X_test)
    return y_predict

def applySVM(X_train, y_train, X_test):
    clf = SVC()
    clf.fit(X_train, y_train)
    y_predict = clf.predict(X_test)
    return y_predict

def applyXGBoost(X_train, y_train, X_test):
    # Encode labels
    # Encode labels
    label_encoder = LabelEncoder()
    y_train_encoded = label_encoder.fit_transform(y_train)

    # Train XGBoost classifier
    clf = XGBClassifier()
    clf.fit(X_train, y_train_encoded)

    # Predict
    y_predict_encoded = clf.predict(X_test)

    # Decode predictions
    y_predict = label_encoder.inverse_transform(y_predict_encoded)
    return y_predict
