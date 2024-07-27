import streamlit as st
import pandas as pd
import joblib
from data_preprocessing import data_preprocessing, encoder_Course, encoder_Daytime_evening_attendance, encoder_Displaced,encoder_Fathers_occupation, encoder_International, encoder_Mothers_occupation, encoder_Scholarship_holder, encoder_Tuition_fees_up_to_date
from prediction import prediction

col1, col2 = st.columns([1, 5])
# with col1:
    # st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png", width=130)
with col2:
    st.header('Student Status Prediction')

data = pd.DataFrame()

col1, col2, col3= st.columns(3)

with col1:
    Application_order = int(st.number_input(label='Application_order', value=1))
    data["Application_order"] = [Application_order]

with col2:
    Course = st.selectbox(label='Course', options=encoder_Course.classes_, index=1)
    data["Course"] = [Course]
    
with col3:
    Daytime_evening_attendance = st.selectbox(label='Daytime_evening_attendance', options=encoder_Daytime_evening_attendance.classes_, index=1)
    data["Daytime_evening_attendance"] = [Daytime_evening_attendance]

col1, col2, col3= st.columns(3)
with col1:
    Previous_qualification_grade = float(st.number_input(label='Previous_qualification_grade', value=140.0))
    data["Previous_qualification_grade"] = [Previous_qualification_grade]
with col2:
    Mothers_occupation = st.selectbox(label='Mothers_occupation', options=encoder_Mothers_occupation.classes_, index=1)
    data["Mothers_occupation"] = [Mothers_occupation]
with col3:
    Fathers_occupation = st.selectbox(label='Fathers_occupation', options=encoder_Fathers_occupation.classes_, index=1)
    data["Fathers_occupation"] = [Fathers_occupation]

col1, col2, col3= st.columns(3)
with col1:
    Admission_grade = float(st.number_input(label='Admission_grade', value=140.0))
    data["Admission_grade"] = [Admission_grade]
with col2:
    Displaced = st.selectbox(label='Displaced', options=encoder_Displaced.classes_, index=1)
    data["Displaced"] = [Displaced]
with col3:
    Tuition_fees_up_to_date = st.selectbox(label='Tuition_fees_up_to_date', options=encoder_Tuition_fees_up_to_date.classes_, index=1)
    data["Tuition_fees_up_to_date"] = [Tuition_fees_up_to_date]

col1, col2, col3= st.columns(3)
with col1:
    Scholarship_holder = st.selectbox(label='Scholarship_holder', options=encoder_Scholarship_holder.classes_, index=1)
    data["Scholarship_holder"] = [Scholarship_holder]
with col2:
    International = st.selectbox(label='International', options=encoder_International.classes_, index=1)
    data["International"] = [International]
with col3:
    Curricular_units_1st_sem_credited = int(st.number_input(label='Curricular_units_1st_sem_credited', value=2))
    data["Curricular_units_1st_sem_credited"] = [Curricular_units_1st_sem_credited]

col1, col2, col3= st.columns(3)
with col1:
    Curricular_units_1st_sem_enrolled = int(st.number_input(label='Curricular_units_1st_sem_enrolled', value=6))
    data["Curricular_units_1st_sem_enrolled"] = [Curricular_units_1st_sem_enrolled]
with col2:
    Curricular_units_1st_sem_evaluations = float(st.number_input(label='Curricular_units_1st_sem_evaluations', value=11))
    data["Curricular_units_1st_sem_evaluations"] = [Curricular_units_1st_sem_evaluations]
with col3:
    Curricular_units_1st_sem_approved = int(st.number_input(label='Curricular_units_1st_sem_approved', value=1))
    data["Curricular_units_1st_sem_approved"] = [Curricular_units_1st_sem_approved]

col1, col2, col3= st.columns(3)
with col1:
    Curricular_units_1st_sem_grade = float(st.number_input(label='Curricular_units_1st_sem_grade', value=11.833333))
    data["Curricular_units_1st_sem_grade"] = [Curricular_units_1st_sem_grade]
with col2:
    Curricular_units_2nd_sem_credited = int(st.number_input(label='Curricular_units_2nd_sem_credited', value=2))
    data["Curricular_units_2nd_sem_credited"] = [Curricular_units_2nd_sem_credited]
with col3:
    Curricular_units_2nd_sem_enrolled = int(st.number_input(label='Curricular_units_2nd_sem_enrolled', value=6))
    data["Curricular_units_2nd_sem_enrolled"] = [Curricular_units_2nd_sem_enrolled]

col1, col2, col3= st.columns(3)
with col1:
    Curricular_units_2nd_sem_evaluations = int(st.number_input(label='Curricular_units_2nd_sem_evaluations', value=1))
    data["Curricular_units_2nd_sem_evaluations"] = [Curricular_units_2nd_sem_evaluations]
with col2:
    Curricular_units_2nd_sem_approved = int(st.number_input(label='Curricular_units_2nd_sem_approved', value=2))
    data["Curricular_units_2nd_sem_approved"] = [Curricular_units_2nd_sem_approved]
with col3:
    Curricular_units_2nd_sem_grade = float(st.number_input(label='Curricular_units_2nd_sem_grade', value=11.857143))
    data["Curricular_units_2nd_sem_grade"] = [Curricular_units_2nd_sem_grade]

col1, col2 = st.columns(2)
with col1:
    Curricular_units_2nd_sem_without_evaluations = int(st.number_input(label='Curricular_units_2nd_sem_without_evaluations', value=6))
    data["Curricular_units_2nd_sem_without_evaluations"] = [Curricular_units_2nd_sem_without_evaluations]
    
with col2:
    GDP = float(st.number_input(label='GDP', value=1.79))
    data["GDP"] = [GDP]

with st.expander("View the Raw Data"):
    st.dataframe(data=data, width=800, height=10)

if st.button('Predict'):
    new_data = data_preprocessing(data=data)
    with st.expander("View the Preprocessed Data"):
        st.dataframe(data=new_data, width=800, height=10)
    st.write("Student Status Prediction: {}".format(prediction(new_data)))