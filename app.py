import streamlit as st
import pandas as pd
import numpy as np
import pickle

loaded_model = pickle.load(open('Disease_prediction.pkl', 'rb'))
sc = pickle.load(open('sc.pkl', 'rb'))

st.header(" DISEASE PREDICTION ")

Age=st.number_input("Age",min_value=0,max_value=100,value=10,step=1)

sex=st.selectbox("Sex",['Male','Female'],index=0)
if sex=="Male":
    sex=1
else:
    sex=0

ChestPainType=st.selectbox("ChestPainType",['ASY','NAP','ATA','TA'],index=0)
if ChestPainType=="ASY":
   ChestPainType=0
elif ChestPainType=="NAP":
   ChestPainType=1
elif ChestPainType=="ATA":
   ChestPainType=2
else:
   ChestPainType=3

RestingBP=st.number_input("RestingBP",min_value=0,max_value=200,value=1,step=1)

Cholesterol=st.number_input("Cholesterol",min_value=0,max_value=700,value=1,step=1)

FastingBS=st.number_input("FastingBS",min_value=0,max_value=1,value=1,step=1)

RestingECG=st.selectbox("RestingECG",['Normal','LVH','ST'],index=0)
if RestingECG=="":
   RestingECG=1
elif RestingECG=="":
   RestingECG=0
else:
   RestingECG=2

ExerciseAngina=st.selectbox("ExerciseAngina",['No','Yes'],index=0)
if ExerciseAngina=="No":
   ExerciseAngina=0
else:
   ExerciseAngina=1

Oldpeak=st.number_input("Oldpeak",min_value=-2.6,max_value=10.0,value=0.0,step=0.5)

ST_Slope=st.selectbox("ST_Slope",['Flat','Up',"Down"],index=0)
if ST_Slope=="Flat":
   ST_Slope=1
elif ST_Slope=="Up":
   ST_Slope=2
else:
   ST_Slope=0

if st.button("PREDICT"):
    classifier=loaded_model.predict(sc.transform([[Age,sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,ExerciseAngina,Oldpeak,ST_Slope]]))
    if classifier == 0:
        st.error("You are not affected by HeartDisease")
        st.write("<span style='font-size: 30px;'>You are SAFE!!!</span>", unsafe_allow_html=True)
    else:
        st.success("You are affected by HeartDisease")
        st.write("<span style='font-size: 30px;'>Consult Doctor IMMEDIATELY!!</span>", unsafe_allow_html=True)
st.write("")	
st.write("A PROJECT BY")
st.markdown("<h1 style='font-size: 20px;'>SYAM, HARSHA and RAMAKRISHNA</h1>", unsafe_allow_html=True)
