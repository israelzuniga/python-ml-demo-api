'''
utils/irisprediction.py
2016 - Demo API
Israel Z
'''
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

# predict function
def predict(features):
    '''
    Docstring
    '''
    iris = load_iris() # Load the iris dataset

    # Create and fit an object based on the classifier
    knn = KNeighborsClassifier()
    knn.fit(iris.data, iris.target)


    # return predictions
    predictions = knn.predict(features)
    if predictions[0] == 0:
        prediction_fam = 'setosa'
    elif predictions[0] == 1:
        prediction_fam = 'versicolor'
    elif predictions[0] == 2:
        prediction_fam = 'virginica'
    else:
        prediction_fam = 'null'

    return prediction_fam
