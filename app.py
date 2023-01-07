import streamlit as st
import pickle

st.title('Crop prediction system')
model=pickle.load(open('model.pkl','rb'))

col1,col2=st.columns(2)
n=col1.number_input('Enter Nitriogen')
p=col2.number_input('Enter Phosphorous')
k=col1.number_input('Enter potassium')
t=col2.number_input('Enter temperature')
h=col1.number_input('Enter humidity')
ph=col2.number_input('Enter pH')
r=col1.number_input('Enter rainfall')

if st.button('Predict'):
    data=[[n,p,k,t,h,ph,r]]
    result=model.predict(data)[0]
    st.success(result)
