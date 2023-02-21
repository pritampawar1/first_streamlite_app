import streamlit
import pandas
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
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avacado','Blueberries'])
streamlit.dataframe(my_fruit_list)
