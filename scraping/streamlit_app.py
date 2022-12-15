from pymongo import MongoClient
import streamlit as st
import pymongo

# Initialize connection.
# Uses st.experimental_singleton to only run once.

def init_connection():
    return pymongo.MongoClient(**st.secrets["mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"])

client = init_connection()
# Connect to the "my_database" database
client= MongoClient("mongodb://localhost:27017/crawel_films")

# Get a reference to the "my_collection" collection
db= client["crawel_films"]
collection=db['films']
act=collection.find().sort("duree",-1).limit(1)
for item in act:
    st.write(f"{item['name']} has a :{item['pet']}:")
