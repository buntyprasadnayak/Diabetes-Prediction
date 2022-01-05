# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle  

#loading the saved Model
loaded_model = pickle.load(open('/Users/bunty/VS Code/MachineLearning/Deploy ML Model/trained_model.sav', 'rb')) 


input_data = (5,166,72,19,175,25.8,0.587,51)

# Changing the input_data to numpy array 
input_data_as_numpy_array = np.asarray(input_data)

#reshape the array as we are predicting for one instance 
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardize the input_data 
# std_data = scaler.transform(input_data_reshaped)

# print(std_data)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if(prediction[0]==0):
  print('The Person is not Diabetic ')
else :
  print('The person is Diabetic ')    