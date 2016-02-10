class AbstractClassifier(object):
    def __init__(self, name):
        self.name = name
        self.model = None
    def predict(self, instance):
        # predict the instance
        pass
    def trainClassifier(self, data):
        # do something to train the classifier
        pass
    def getName(self):
        return self.name

class NaiveBayesClassifier(AbstractClassifier):
    def __init__(self):
        super(NaiveBayesClassifier, self).__init__('NaiveBayesClassifier')

class SMOClassifier(AbstractClassifier):
    def __init__(self):
        super(SMOClassifier, self).__init__('SMOClassifier')

if __name__ == '__main__':
    classifiers = [NaiveBayesClassifier(), SMOClassifier()]
    for c in classifiers:
        print(c.getName())