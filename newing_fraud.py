import pandas as pd
import sklearn.utils
import streamlit as st
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import SGDClassifier

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import f1_score
df = pd.read_csv("spam.csv")
df = df[["class", "message"]]
st.write(df)
value_diction = {"ham": 0, "spam": 1}
df["class"] = df["class"].map(value_diction)
df = sklearn.utils.shuffle(df)
vectorizer = TfidfVectorizer()
X = (vectorizer.fit_transform(df["message"].values)).toarray()
y = df["class"].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05)
clf = SGDClassifier()
clf.fit(X_train, y_train)
value_ = ["ASZIMPORTANT: Earn 25% on prime coupons!"]
value_ = vectorizer.transform(value_)
pred = clf.predict(value_.toarray())
for cval, k in value_diction.items():
    if [k] == pred:
        print(cval)

