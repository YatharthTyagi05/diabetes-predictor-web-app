import pandas as pd
import pickle
import streamlit as st

loaded_model = pickle.load(open(r'trained_model1.sav', 'rb'))


def Diabetes_prediction(input_data):
    
    
    input_data = (6,148,72,35,0,33.6,0.627,50)
    input_df = pd.DataFrame([input_data], columns=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age'])
    prediction = loaded_model.predict(input_df)
    if prediction[0] == 1:
        return "Diabetic"
    
    else: 
        return "Non-Diabetic"
    
    
def main():
    
    st.title("Diabetes Prediction web app")
    
    
    pregnancies=st.text_input("enter the pregnancies")
    Glucose=st.text_input("enter the Glucose")
    BloodPressure=st.text_input("enter the BloodPressure")
    SkinThickness=st.text_input("enter the SkinThickness")
    Insulin=st.text_input("enter the Insulin")
    BMI=st.text_input("enter the BMI")
    DiabetesPedigreeFunction=st.text_input("enter the DiabetesPedigreeFunctiond")
    Age=st.text_input("enter the Age")
    
    predict=""
    
    if st.button("Diabetes prediction"):
        predict=Diabetes_prediction([pregnancies,Glucose, BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])

    

        
    st.success(predict)
    
if __name__ == '__main__':
    main()