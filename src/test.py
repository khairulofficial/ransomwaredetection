from train import train_model
from sklearn.model_selection import cross_val_score

from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier


def test_model(model, test_file):
    model = model
    test_file = test_file

    model, features, target = train_model(model, test_file)
    family = model.predict(test_file)
    cvscore = cross_val_score(model,features,target,cv=10).mean()

    return family, cvscore