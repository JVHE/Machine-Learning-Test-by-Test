class Perceptron:
    def __init__(self):
        self._weight_1 = 0.20
        self._weight_2 = 0.20
    def train(self, inputs, label):
        input = inputs[0]
        self._weight_1 = self._weight_1 + .25 * (inputs[0] - label) * self.predict([input])
        #
        self._weight_2 = self._weight_2 + .25 * (inputs[1] - label) * self.predict([input])
    def predict(self, inputs):
        if len(inputs) == 0:
            return None
        return 0 < self._weight_1 * inputs[0] + self._weight_2 * inputs[1]

