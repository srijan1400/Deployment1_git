import sklearn
import numpy as np
import pandas as pd 
import flask
from flask import Flask, request, render_template, Request
import pickle
from sklearn.preprocessing import StandardScaler
import streamlit as st

scale = StandardScaler()

grad_model = pickle.load(open("grad.pickle", "rb"))



def main():
    st.title("Company X Attrition Probability")
    Age = st.slider("What is your Age?", 18,60,25)
    Daily_Income = st.number_input('How much is your Daily Income?',100,1500)
    DistanceFromHome = st.slider("How far do you live?",1,30,10)
    EducationLevel = st.slider("What is your education level?",1,4)
    Work_Satisfaction = st.slider('What is your current work satisfaction level?',1,4)
    Job_Involvement = st.slider("What is your job involvement level?",1,4)
    Job_Satisfaction = st.slider("What is your job satisfaction level?",1,4)
    Companies_Before = st.slider("How many companies have you worked for before?",0,10,5)
    Company_Satisfaction = st.slider("What is your current company satisfaction level?",1,4)
    Company_Stock = st.slider("How much comapny stock do you have on a scale?",1,4)
    Training = st.slider("How much training time did you have at the company last year? (In Hours)",0,6)
    Work_Life = st.slider("What is your Work-Life balance level?",1,4)
    Last_Promotion = st.slider("How much time is it since your last promotion? (In Years)",0,15)
    Curr_Manager = st.slider("How long have you worked with your current Manager? (In Years)",0,15)
    Work_Travel = st.slider("What is your work travel level? (Never, Rarely, Frequently)",0,2)
    Work_Dept = st.slider("Which department do you work in? ( HR, R&D, Sales )",0,2)
    Sex = st.slider("What is your gender? ( M, F )",0,1)
    Marital = st.slider('What is your Marital Status?',0,2)
    result = ""
    if st.button("Result"):
        result = grad_model.predict([[Age,Daily_Income,DistanceFromHome,EducationLevel,Work_Satisfaction,Job_Involvement,Job_Satisfaction,Companies_Before,Company_Satisfaction,Company_Stock, Training, Work_Life, Last_Promotion,Curr_Manager,Work_Travel, Work_Dept, Sex, Marital]])
        if result ==[1]:
            st.success("The Employee will leave the company !!")
        elif result ==[0]:
            st.success("The Employee will not leave the company !!")

if __name__ == "__main__":
    main()


#result = grad_model.predict([[Age,Daily_Income,DistanceFromHome,EducationLevel,Work_Satisfaction,Job_Involvement,Job_Satisfaction,Companies_Before,Company_Satisfaction,Company_Stock, Training, Work_Life, Last_Promotion,Curr_Manager,Work_Travel, Work_Dept, Sex, Marital]])