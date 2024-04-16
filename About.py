import streamlit as st

# Header and Introduction
st.title("Women’s Clothing E-Commerce Analysis")
st.write("Welcome to the Women's Clothing E-commerece Use the sidebar to navigate. 🚀")

# About Page
st.title("About ℹ️")
st.image("img1.jpg", use_column_width=True)
st.markdown("---")

st.write("""
This dataset includes 23486 rows and 10 feature variables. Each row corresponds to a customer review,
and includes the variables:

● Age: Positive Integer variable of the reviewers' age.
         
● Title: String variable for the title of the review.
         
● Review Text: String variable for the review body.
         
● Rating: Positive Ordinal Integer variable for the product score granted by the customer from 1
Worst to 5 Best.
         
● Recommended IND: Binary variable stating where the customer recommends the product
where 1 is recommended, and 0 is not recommended.
         
● Positive Feedback Count: Positive Integer documenting the number of other customers who
found this review positive.
         
● Division Name: Categorical name of the product high-level division.
         
● Department Name: Categorical name of the product department name.
         
● Class Name: Categorical name of the product class name
""")

# Additional Information
st.markdown("---")  
st.subheader("Additional Information ℹ️")
st.write("""
- **Dataset Source:** No specific source provided. 🤷‍♂️
- **Created By:** [Likitha Yadav G] 🧑‍💻
- **Contact Information:** [likitha@12345.gmail.com] ✉️
""")
