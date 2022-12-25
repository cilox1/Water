import pickle
import streamlit as st

# membaca model
dataset_model = pickle.load(open('dataset_model2.sav', 'rb'))

#judul web
st.title('Prediksi kualitas air')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    aluminium = st.text_input ('input nilai aluminium')

with col2 :
    ammonia = st.text_input ('input nilai ammonia')

with col1 :
    arsenic = st.text_input ('input nilai arsenic')

with col2 :
    barium  = st.text_input ('input nilai barium')

with col1 :
    cadmium = st.text_input ('input nilai cadmium')

with col2 :
    chloramine = st.text_input ('input nilai chloramine')
with col1 :
    chromium = st.text_input ('input nilai chromium')

with col2 :
    copper = st.text_input ('input nilai copper')

with col1 :
    flouride = st.text_input ('input nilai flouride')

with col2 :
    bacteria = st.text_input ('input nilai bacteria')

with col1 :
    viruses = st.text_input ('input nilai viruses')

with col2 :
    lead = st.text_input ('input nilai lead')

with col1 :
    nitrates = st.text_input ('input nilai nitrates')

with col2 :
    nitrites = st.text_input ('input nilai nitrites')

with col1 :
    mercury = st.text_input ('input nilai mercury')

with col2 :
    perchlorate = st.text_input ('input nilai perchlorate')

with col1 :
    radium = st.text_input ('input nilai radium')

with col2 :
    selenium = st.text_input ('input nilai selenium')

with col1 :
    silver = st.text_input ('input nilai silver')

with col2 :
    uranium = st.text_input ('input nilai uranium')


# code untuk prediksi
water_diangnosis = ''

# membuat tombol untuk prediksi
if st.button('test prediksi kualitas air') :
    water_prediction = dataset_model.predict([[aluminium,ammonia,arsenic,barium,cadmium,chloramine,chromium,copper,flouride,bacteria,viruses,lead,nitrates,nitrites,mercury,perchlorate,radium,selenium,silver,uranium]])

    if(water_prediction[0] == 1):
        water_diangnosis = 'Bersih'
    else :
        water_diangnosis = 'Tercemar'
    
    st.success(water_diangnosis)