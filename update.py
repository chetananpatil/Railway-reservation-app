import pandas as pd
import streamlit as st
from database import view_all_data, view_only_names,edit_data,get_data


def update():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Train_No', 'Name', 'Train_Type', 'Source', 'Destination', 'Availability'])
    with st.expander("Current Data"):
        st.dataframe(df)
    list_of_data = [i[0] for i in view_only_names()]
    selected_data = st.selectbox("Data to Edit", list_of_data)
    selected_result = get_data(selected_data)
    if selected_result:
        Train_No = selected_result[0][0]
        name = selected_result[0][1]
        Train_Type = selected_result[0][2]
        Source = selected_result[0][3]
        Destination = selected_result[0][4]
        Availability=selected_result[0][5]
        col1, col2 = st.columns(2)
        with col1:
            new_Train_No = Train_No
            new_name = st.text_input("Name:", name)
            new_Train_Type=st.text_input("Train_Type:",Train_Type)
        with col2:
            new_Source = st.text_input("Source:",Source)
            new_Destination = st.text_input("Destination:",Destination)
        new_Availability = st.text_input("Availability:", Availability)
        if st.button("Update Data"):
            edit_data(new_Train_No, new_name, new_Train_Type, new_Source, new_Destination, new_Availability, Train_No, name, Train_Type, Source,Destination,Availability)
            st.success("Successfully updated:: {} to ::{}".format(Train_No,new_Train_No))
    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=['Train_No', 'Name', 'Train_Type', 'Source', 'Destination', 'Availability'])
    with st.expander("Updated data"):
        st.dataframe(df2)
