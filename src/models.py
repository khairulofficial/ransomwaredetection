from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier

def get_model(model):
  """
  Returns a machine learning model based on the specified name.

  Args:
      model_name: Name of the model (e.g., "random_forest", "logistic_regression", "svm").

  Returns:
      A scikit-learn machine learning model object.
  """

  model_map = {
      "Random Forest (Recommended)": RandomForestClassifier(),
      "Logistic Regression": LogisticRegression(solver="liblinear"),
      "SVM": SVC(),
      "XGBoost": GradientBoostingClassifier(),
      "Neural Network": MLPClassifier(),
      "KNN": KNeighborsClassifier(),
      "Naive Bayes": GaussianNB()
  }

  return model_map.get(model) 