from features import prepare_data
from models import get_model 
from sklearn.model_selection import train_test_split

from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier




def train_model(model, test_file):
  """

  Trains, evaluates, and prints performance metrics for multiple models.


  Args:

      db_path: Path to the SQLite database file.

      config_file: Path to the configuration file (optional).
  """
  model = model
  test_file = test_file

  features, target = prepare_data(test_file)


  # Split data into training and testing sets
  X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2)


  # Train model
  model = get_model(model)
  print(X_train, y_train)

  model = model.fit(X_train, y_train)
  

  return model, features, target
