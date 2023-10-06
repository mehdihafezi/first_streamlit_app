#import streamlit
import pandas

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)




#st.title('My Parents New Healthy Diner')
#st.header('My Breakfast menu')
#st.divider()  # 
#st.text('Omega 3 & Blueberry Oatmeal')
#st.divider()  # 
#st.text('Kale, Spinach & Rocket Smoothie')
#st.divider()  # 
#st.text('Hard-Boiled free-Range Egge')
#st.divider()  # 
#st.write('Omega 3 & Blueberry Oatmeal')
