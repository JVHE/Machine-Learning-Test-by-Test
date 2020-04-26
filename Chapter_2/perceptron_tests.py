import nose.tools as nt
from Perceptron import Perceptron
def no_training_data_supplied_test():
    # given
    the_perceptron = Perceptron()
    # when
    result = the_perceptron.predict([])
    # then
    nt.assert_equal(result, None, 'Should have no result with no training data.')

def train_an_OR_function_test():
    # given
    the_perceptron = Perceptron()
    # when
    the_perceptron.train([1,1],1)
    the_perceptron.train([1,0],1)
    the_perceptron.train([0,1],1)
    the_perceptron.train([0,0],0)
    # then
    nt.assert_equal(the_perceptron.predict([1,1]), 1)
    nt.assert_equal(the_perceptron.predict([1,0]), 1)
    nt.assert_equal(the_perceptron.predict([0,1]), 1)
    nt.assert_equal(the_perceptron.predict([0,0]), 0)
