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

def get_fruitvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")
#streamlit.text(fruityvice_response.json())
# convert response to table
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
      streamlit.error("Please select fruit to get information.")
  else:
    #streamlit.write('The user entered ', fruit_choice)
    #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    back_from_function = get_fruitvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
  
except URLError as e:
    streamlit.error
    
# show table on app
#streamlit.dataframe(fruityvice_normalized)

def get_fruit_load_list():
     with my_cnx.cursor() as my_cur:
            my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
            return my_cur.fetchall()
            
if streamlit.button('Get fruit load list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    #my_cur = my_cnx.cursor()
    #my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
    #my_data_row = my_cur.fetchone()
    my_data_row = get_fruit_load_list()    
    streamlit.text("Hello from Snowflake:")
    #streamlit.text(my_data_row)
    streamlit.header("Fruitload list contains")
    streamlit.dataframe(my_data_row)
def insert_row_into_snowflake(new_fruit):
        with my_cnx.cursor() as my_cur:
                my_cur.execute("Insert into PC_RIVERY_DB.PUBLIC.fruit_load_list values ('from streamlite')")
                return "Thanks for adding new fruit" + new_fruit
 
fruit_choice = streamlit.text_input('What fruit would you like to add?')
        
if streamlit.button('Add a fruit to list'):
    fruit_like_by_user = streamlit.text_input('What fruit would you like to add?','jackfruit')
    #streamlit.write('thanks for adding:', fruit_like_by_user)
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_into_snowflake(fruit_choice)
    streamlit.text(back_from_function)
#my_cur.execute("Insert into PC_RIVERY_DB.PUBLIC.fruit_load_list values ('from streamlite')")
#streamlit.stop()

