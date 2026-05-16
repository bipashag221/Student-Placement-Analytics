import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("Student Placement Analytics Dashboard")

# Load dataset
df = pd.read_csv("placement.csv")

# Show dataset
st.subheader("Student Data")
st.dataframe(df)

# Basic statistics
st.subheader("Overall Statistics")

total_students = len(df)
placed_students = len(df[df['Placed'] == 'Yes'])
placement_rate = (placed_students / total_students) * 100
average_cgpa = df['CGPA'].mean()
highest_package = df['Package'].max()

st.write(f"Total Students: {total_students}")
st.write(f"Placed Students: {placed_students}")
st.write(f"Placement Rate: {placement_rate:.2f}%")
st.write(f"Average CGPA: {average_cgpa:.2f}")
st.write(f"Highest Package: {highest_package} LPA")

# Branch-wise placements
st.subheader("Branch-wise Placement Count")

branch_counts = df.groupby('Branch')['Placed'].count()

fig, ax = plt.subplots()
branch_counts.plot(kind='bar', ax=ax)

plt.xlabel("Branch")
plt.ylabel("Students")
plt.title("Branch-wise Students")

st.pyplot(fig)

# Company-wise hiring
st.subheader("Company-wise Hiring")

company_counts = df[df['Placed'] == 'Yes']['Company'].value_counts()

fig2, ax2 = plt.subplots()
company_counts.plot(kind='pie', autopct='%1.1f%%', ax=ax2)

plt.ylabel("")
plt.title("Company Hiring Distribution")

st.pyplot(fig2)

# Top performers
st.subheader("Top Students")

top_students = df.sort_values(by='CGPA', ascending=False).head(5)

st.table(top_students)
branch = st.sidebar.selectbox(
    "Select Branch",
    df['Branch'].unique()
)

filtered_df = df[df['Branch'] == branch]

st.dataframe(filtered_df)
student = st.text_input("Search Student")

if student:
    result = df[df['Name'].str.contains(student)]
    st.write(result)

fig3, ax3 = plt.subplots()

ax3.hist(df['Package'])

plt.xlabel("Package")
plt.ylabel("Students")

st.pyplot(fig3)