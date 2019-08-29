from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.svm import LinearSVC


class SVM:
    """ SVM model to support Online Troll comment detection

    Attributes
    ----------
    description : string, model description for referencing parameters of object

    clf : sklearn svm model object

    """

    def __init__(self, description):
        """ Initialize model configuration

        Parameters
        --------------
            data: (dict) dictionary of training and testings sets of data
            description: (str) description of model being trained
        """
        self.description = description
        self.clf = LinearSVC()

    def train(self, data, **params):
        """ Trains model with grid search over user defined parameters

        Parameters
        -------------
            parameters: (dict) key value pairs specifying sklearn parameter search

        """

        self.clf = GridSearchCV(self.clf, params, cv=5)
        self.clf.fit(data['X_train'], data['y_train'])

    def display_results(self, data):
        """ Prints testing and training accuracies along with other model
            validation metrics.

        Parameters
        ---------------
            clf: (scikit-learn model) predictive model to test
            data: (dict) training and testing data for model
        """
        train_accuracy = self.clf.score(data['X_train'], data['y_train'])
        test_accuracy = self.clf.score(data['X_test'], data['y_test'])
        y_pred = self.clf.predict(data['X_test'])
        print('{:>20s} {:.2f}'.format('Train Accuracy:', train_accuracy))
        print('{:>20s} {:.2f}'.format('Test Accuracy:', test_accuracy))
        print(confusion_matrix(data['y_test'], y_pred))