import streamlit as st
from database import add_data

def create():
    col1, col2 = st.columns(2)
    with col1:
        Train_No = st.text_input("Train_No:")
        name = st.text_input("Name:")
        Train_Type = st.text_input("Train_Type:")
    with col2:
        Source = st.text_input("Source")
        Destination=st.text_input("Destination")
        Availability = st.text_input("Availability:")
    if st.button("Add Data"):
        add_data(Train_No,name, Train_Type, Source,Destination, Availability)
        st.success("Successfully added data: {}".format(name))
