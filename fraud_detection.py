# -*- coding: utf-8 -*-
"""
Created on Thu May  5 00:03:54 2022

@author: Admin
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 19:04:52 2022

@author: Prasad's PC
"""

import numpy as np
import sklearn
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image


st.image("insurance.jpeg")
#app=Flask(__name__)
#Swagger(app)

pickle_in= open("model_pkl.pkl","rb")
model=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome  All"

#@app.route('/predict',methods=["Get"])
def predict_insurance_fraud(Area_Service,Age,Gender,Cultural_group,ethnicity,Admission_type,Home_care,ccs_procedure_code,Mortality_risk,Surg_Description,Weight_baby,Emergency_dept_yes_No,Tot_charg,ratio_of_total_costs_to_total_charges,Payment_Typology):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=model.predict([[Area_Service,Age,Gender,Cultural_group,ethnicity,Admission_type,Home_care,ccs_procedure_code,Mortality_risk,Surg_Description,Weight_baby,Emergency_dept_yes_No,Tot_charg,ratio_of_total_costs_to_total_charges,Payment_Typology]])
   
    print(prediction)
    

    if (prediction == 0):
       return"The claim is Fraud"
    else:
       return'The claim is Genuine'
    

def main():
    
    html_temp = """
    <div style="background-color:blue;padding:10px">
    <h2 style="color:white;text-align:center;">Insurance Fraud Detection</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Area_Service = st.text_input("Area_Service-Central NY:0,Capital/Adirond:1, Finger Lakes:2, Hudson Valley:3,New York City :4,Southern Tier:5,  Western NY:6")
    Age = st.text_input("Age of person - 0 to 17:1, 18 to 29: 2, 30 to 49: 3, 50 to 69: 4, 70 and older: 5")
    Gender = st.selectbox("Gender", ('Female', 'Male')) 
    Gender= 0 if Gender=="Female" else 1
    Cultural_group = st.text_input("Cultural_group- Black/African American:0,Other Race:1, White:2")
    ethnicity = st.text_input("ethnicity-nonspan/hispanis:0,spanish:1")
    Admission_type = st.text_input("Admission_type - Emergency:1,Urgent:2 ,Elective:3, Newborn:4,Trauma:5")
    Home_care = st.text_input("Home_care","Type Here")
    ccs_procedure_code = st.text_input("ccs_procedure_code","Type Here")
    Mortality_risk = st.text_input("Mortality_risk-Minor:1, Moderate:2, Major:3, Severe:4")
    Surg_Description = st.text_input("Surg_Description","Type Here")
    Weight_baby = st.text_input("Weight_baby","Type Here")
    Emergency_dept_yes_No = st.text_input("Emergency_dept_yes_No -N:0, Y:1")
    Tot_charg = st.text_input("Tot_charg","Type Here")
    ratio_of_total_costs_to_total_charges = st.text_input("ratio_of_total_costs_to_total_charges","Type Here")
    Payment_Typology = st.text_input("Payment_Typology-Medicare:1, Medicaid:2, Other Governments:3, Department of Corrections: 4, Private Health Insurance: 5")
   
    result=""
    if st.button("Predict"):
        result=predict_insurance_fraud(Area_Service,Age,Gender,Cultural_group,ethnicity,Admission_type,Home_care,ccs_procedure_code,Mortality_risk,Surg_Description,Weight_baby,Emergency_dept_yes_No,Tot_charg,ratio_of_total_costs_to_total_charges,Payment_Typology)
    st.success(result)
     
     
    
   

if __name__=='__main__':
    main()