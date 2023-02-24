import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My parents new healthy dinner')
streamlit.header('🥣Breakfast menu')
streamlit.text('🥑Omega 3 and Blueberry oatmeal')
streamlit.text('🥗Kale spinacha and rocket smothie')
streamlit.text('🐔Hard boiled free range eggs')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


# Display the table on the page.
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries','Honeydew'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


streamlit.header("Fruityvice Fruit Advice!")
#streamlit.text(fruityvice_response.json())
# convert response to table
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
      streamlit.error("Please select fruit to get information.")
  else:
    #streamlit.write('The user entered ', fruit_choice)
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  
except URLError as e:
    streamlit.error
    
# show table on app
streamlit.dataframe(fruityvice_normalized)

streamlit.stop()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
#my_data_row = my_cur.fetchone()
my_data_row = my_cur.fetchall()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
streamlit.header("Fruitload list contains")
streamlit.dataframe(my_data_row)
fruit_like_by_user = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('thanks for adding:', fruit_like_by_user)
my_cur.execute("Insert into PC_RIVERY_DB.PUBLIC.fruit_load_list values ('from streamlite')")

