
import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
def load_data():
    return pd.read_csv("WomensClothingE-CommerceReviews.csv")

data = load_data()

# Sidebar Filters
st.sidebar.title("Filters")
min_age = st.sidebar.slider("Minimum Age", int(data['Age'].min()), int(data['Age'].max()), int(data['Age'].min()))
max_age = st.sidebar.slider("Maximum Age", int(data['Age'].min()), int(data['Age'].max()), int(data['Age'].max()))
min_rating = st.sidebar.slider("Minimum Rating", int(data['Rating'].min()), int(data['Rating'].max()), int(data['Rating'].min()))
min_positive_feedback = st.sidebar.slider("Minimum Positive Feedback Count", int(data['Positive Feedback Count'].min()), int(data['Positive Feedback Count'].max()), int(data['Positive Feedback Count'].min()))

# Filter the data
filtered_data = data[(data['Age'] >= min_age) & (data['Age'] <= max_age) & 
                     (data['Rating'] >= min_rating) & 
                     (data['Positive Feedback Count'] >= min_positive_feedback)]

# Display Filtered Data
st.subheader("Filtered Data")
st.write(filtered_data)

# Data Exploration Tools
st.subheader("Data Exploration Tools")

# Summary Statistics
if st.checkbox("Summary Statistics"):
    st.write(filtered_data.describe())

# Visualization
st.subheader("3D Scatter Plot")
st.subheader("RelationShip Between the Age,rating and Postive FeedBack Count")
fig = px.scatter_3d(filtered_data, x='Age', y='Rating', z='Positive Feedback Count', color='Rating', opacity=0.7, size_max=10,
                    hover_data={'Age': True, 'Rating': True, 'Positive Feedback Count': True})
fig.update_layout(scene=dict(xaxis_title='Age', yaxis_title='Rating', zaxis_title='Positive Feedback Count'))
st.plotly_chart(fig)
