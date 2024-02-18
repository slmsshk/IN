import streamlit as st
import pandas as pd


st.set_page_config('Shahi Hadees',layout='wide',menu_items={'About': 'This is an *Hadees* cool app!'})
st.markdown(f"""<h1 style=text-align:center;margin-top:-300px,>
           Sahih Bukhari</h1>
           """,unsafe_allow_html=True)

st.markdown(f"""<p style=text-align:left;margin-bottom:-50px>
           Select Hadees</p>
           """,unsafe_allow_html=True)
hadees_df = pd.read_csv('Cleaned1_Shahi_bukhari.csv')

# st.write(hadees_df.head())

volume = st.selectbox(' ',options=hadees_df['Volume'],help='Select the hadees from the dropdown to read the hadees')
selected_hadees_texts = hadees_df[hadees_df['Volume'] == volume]['Hadees']

# Join the selected hadees texts into a single string without using to_string()
selected = ' '.join(selected_hadees_texts)
st.markdown(f"""<div text_overflow>
            <p>{selected}</p>
            </div>""",unsafe_allow_html=True)

st.title('Top Narrators')

c1,c2 = st.columns(2)

with c1:
    st.image('narrators.png')
with c2:
    st.image('top_narrator_ratio.png')

# st.write('Hi i am a hadees bot can have limited conversation with you on Sahih Bukhari hadees,')

# st.chat_input('Input')

# st.write('Output')