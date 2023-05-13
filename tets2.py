import streamlit as st
import pandas as pd
import numpy as np

from pymongo import MongoClient
from streamlit_option_menu import option_menu  # pip install streamlit-option-menu
from PIL import Image

# import datetime for date fields
from datetime import datetime
datetime_now = datetime.now() # pass this to a MongoDB doc
print ("datetime_now:", datetime_now)
print ("type datetime_now:", type(datetime_now))

# im = Image.open("favicon.ico")
st.set_page_config(
    page_title='SmartFishSense',
    # page_icon=im,
    layout='wide', #centered or wide
    initial_sidebar_state='expanded',
)

st.title("Smart Fish Sense")

# --- NAVIGATION MENU ---
selected = option_menu(
    menu_title=None,
    options=["Control Menu", "Recent Status"],
    icons=["bi bi-toggles2", "bi bi-hourglass-split"],  # https://icons.getbootstrap.com/
    orientation="horizontal",
)

col1, col2 = st.columns(2)

#Inisialisasi awal
resetx = 0
exitx = 0
statusx = 0
confidencex = 0

with col1:
  if st.button('Reset'):
    resetx = 1
  else:
    resetx = 0

with col2:
  if st.button('Exit Idle'):
    exitx = 1
  else:
    exitx = 0

with st.expander("Recent Status"):
   chart_data=pd.DataFrame(
     np.random.randn(10,3),
     columns=['Time','Status','Confidence'],
    )
   
   st.table(chart_data)
  
# chart_data= chart_data.reset_index(level='Time)
# chart_data

# Replace the uri string with your MongoDB deployment's connection string.

uri = "mongodb+srv://agapedsky:dagozilla@cluster0.ro1gcoc.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

# database and collection code goes here

db = client.TA

coll = db.data1

# coll.drop()

# insert code goes here

docs = [

	{"time": datetime.today(), "reset": resetx, "exit_idle": exitx, "statusx": statusx, "confidencex": confidencex,},
  # {"time": datetime.today(), "reset": resetx, "exit_idle": exitx, "status": statusx, "confidence": confidencex},

    ]

result = coll.insert_many(docs)


# display the results of your operation

print(result.inserted_ids)

# Close the connection to MongoDB when you're done.

client.close()
