import pandas as pd
import pickle 

loaded_model=pickle.load(open(r'trained_model1.sav','rb'))
 
input_data = (6,148,72,35,0,33.6,0.627,50)
input_df = pd.DataFrame([input_data], columns=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age'])
prediction = loaded_model.predict(input_df)
print("Prediction result:", "Diabetic" if prediction[0] == 1 else "Non-Diabetic")