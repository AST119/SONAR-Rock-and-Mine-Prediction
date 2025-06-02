import numpy as np
import pickle
import streamlit as st
import numpy as np
#loading the model
loaded_model=pickle.load(open("C:/Users/aadit/Machine Learning/trained_model.sav",'rb'))


#creating a function for Prediction
def Rock_Mine_prediction(input_data):
    input_data_as_array=np.asarray(input_data)
    input_data_reshaped=input_data_as_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    
    if(prediction[0]=='R'):
        print('Rock Detected')
    else: 
        print('Mine Detected')
        
def main():
    
    #giving a title
    st.title('SONAR ROCK V/S MINE Prediction Web App')

    parameters=[]
    #getting the input from the user
    
    var=st.text_input("Enter comma separated values)
    parameters=list(var)
    
        
    #code for prediction
    prediction=''
    if st.button('Predict'):
        prediction=Rock_Mine_prediction(parameters)
    st.success(prediction)
    
if __name__=='__main__':
    main()