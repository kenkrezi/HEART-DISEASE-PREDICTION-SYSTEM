# importing dependencies
import numpy as np
import pandas as pd
#from sklearn.model_selection import train_test_split
#from sklearn.linear_model import LogisticRegression
#from sklearn.metrics import accuracy_score
import pickle
def predict(array):
  input_data = array
  

# change input data to numpy array
  input_data_as_numpy_array = np.asarray(input_data)

#reshape the numpy array aswe are predicting for only 1 instance
  input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
  filename = '/home/apex/Heartguard/base/finalized_model.sav'
# load the model from disk
  loaded_model = pickle.load(open(filename, 'rb'))
#result = loaded_model.score(X_test, Y_test)
#print(result)

  prediction = loaded_model.predict(input_data_reshaped)
  print(prediction)

  if (prediction[0] == 0):
    return ('You have a Healthy Heart ')
  else:
    return ('You have a Heart Disease ')

