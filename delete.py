
import pandas as pd
import streamlit as st
from database import view_all_data, view_only_names, delete_data

def delete():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Train_No', 'Name', 'Train_Type', 'Source', 'Destination', 'Availability'])
    with st.expander("Current data"):
        st.dataframe(df)
    list_data = [i[0] for i in view_only_names()]
    selected_data = st.selectbox("Task to Delete", list_data)
    st.warning("Do you want to delete ::{}".format(selected_data))
    if st.button("Delete Data"):
        delete_data(selected_data)
        st.success("Datahas been deleted successfully")
    new_result = view_all_data()
    df2 = pd.DataFrame(new_result, columns=['Train_No', 'Name', 'Train_Type', 'Source', 'Destination', 'Availability'])
    with st.expander("Updated data"):
        st.dataframe(df2)
