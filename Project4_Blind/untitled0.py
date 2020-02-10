#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 11:37:52 2020

@author: priyamisner
based off of: https://medium.com/technology-invention-and-more/how-to-build-a-simple-neural-network-in-9-lines-of-python-code-cc8f23647ca1
"""
from numpy import exp, array, random, dot

class NeuralNetwork():
    def __init__(self):
        random.seed(1)
        #this models a neuron with 3 input connections from data set and 1 output
        #random weights assigned to this matrix w/ range [-1,1], mean 0
        self.synaptic_weights = 2* random.random((3,1))-1
   
    #sigmoid function (S shaped curve) helps normalise between 0 and 1
    def __sigmoid(self,x):
        return (1/(1+exp(-x)))
    
    #der of Sigmoid, indicate how confident we are of existing weight
    def __sigmoid_derivative(self,x):
        return (x*(1-x))
    
    #training neural network thorugh trial and error
    #synaptic weights adjusted each time
    def train(self, training_set_inputs, training_set_outputs, num_training_iterations):
        for iteration in range(num_training_iterations):
            #pass training data through neural network
            output = self.think(training_set_inputs)
            
            #calculate error
            error = training_set_outputs - output
            
            #multiplying error by S curve means less confident weights adjusted more
            adjustment = dot(training_set_inputs.T, error*self.__sigmoid_derivative(output))
            
            #adjust weights
            self.synaptic_weights += adjustment
    def think(self, inputs):
        # Pass inputs through our neural network (our single neuron).
        return self.__sigmoid(dot(inputs, self.synaptic_weights))

if __name__ == "__main__":
    neural_network = NeuralNetwork()
    print("Starting Weight: ")
    print(neural_network.synaptic_weights)  
    training_set_inputs = array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
    training_set_outputs = array([[0,1,1,0]]).T
    # Train the neural network using a training set.
    # Do it 10,000 times and make small adjustments each time.
    neural_network.train(training_set_inputs, training_set_outputs, 100000)
    print ("New synaptic weights after training: ")
    print(neural_network.synaptic_weights)

    # Test the neural network with a new situation.
    print("Considering new situation [1, 0, 0] -> ?: ")
    print(neural_network.think(array([1, 0, 0])))
