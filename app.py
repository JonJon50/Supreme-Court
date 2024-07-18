import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Load the CSV files
justices_file = 'SupremeCourt.csv'
cases_file = 'RacialEqualityCases.csv'
justices = pd.read_csv(justices_file)
cases = pd.read_csv(cases_file)

# Create a color mapping for states
state_colors = {
    'New York': 'blue', 'South Carolina': 'green', 'Connecticut': 'red', 'Virginia': 'purple',
    'Maryland': 'orange', 'Ohio': 'brown', 'Illinois': 'pink', 'Louisiana': 'gray', 'Kentucky': 'yellow',
    'California': 'red', 'Minnesota': 'blue', 'Arizona': 'gray', 'Georgia': 'purple', 'New Jersey': 'blue',
    'Indiana': 'green', 'Colorado': 'pink', 'Washington D.C.': 'red'
}

# Assign colors to justices based on their state
justices['Color'] = justices['State From'].map(state_colors)

# Title
st.title('Supreme Court Justices and Racial Equality Cases Analysis')

# Gender Distribution
st.header('Gender Distribution of Supreme Court Justices')
if 'Gender' in justices.columns:
    gender_counts = justices['Gender'].value_counts()
    fig, ax = plt.subplots()
    gender_counts.plot(kind='bar', color=['blue', 'pink'], ax=ax)
    ax.set_title('Gender Distribution of Supreme Court Justices')
    ax.set_xlabel('Gender')
    ax.set_ylabel('Count')
    st.pyplot(fig)

# Race Distribution
st.header('Race Distribution of Supreme Court Justices')
if 'Race' in justices.columns:
    race_counts = justices['Race'].value_counts()
    fig, ax = plt.subplots()
    race_counts.plot(kind='bar', color=['brown', 'tan', 'yellow', 'black', 'red'], ax=ax)
    ax.set_title('Race Distribution of Supreme Court Justices')
    ax.set_xlabel('Race')
    ax.set_ylabel('Count')
    st.pyplot(fig)

# Supreme Court Cases Impacting Racial Equality
st.header('Supreme Court Cases Impacting Racial Equality')
fig, ax = plt.subplots()
ax.plot(cases['Year'], cases['Case'], marker='o', linestyle='-', color='b')
ax.set_title('Supreme Court Cases Impacting Racial Equality')
ax.set_xlabel('Year')
ax.set_ylabel('Case')
ax.set_xticks(cases['Year'])
ax.set_xticklabels(cases['Year'], rotation=45)
ax.grid(True)
st.pyplot(fig)

# Impact Analysis - Waterfall Chart
st.header('Impact of Supreme Court Cases on Racial Equality')
impact_counts = cases['Impact'].value_counts().reset_index()
impact_counts.columns = ['Impact', 'Count']

fig = go.Figure(go.Waterfall(
    name="Impact",
    orientation="v",
    measure=["relative"] * len(impact_counts),
    x=impact_counts['Impact'],
    y=impact_counts['Count'],
    connector={"line": {"color": "rgb(63, 63, 63)"}},
))

fig.update_layout(
    title="Impact of Supreme Court Cases on Racial Equality",
    xaxis_title="Impact",
    yaxis_title="Count",
    waterfallgroupgap=0.5
)

st.plotly_chart(fig)

# Cases by Chief Justice
st.header('Supreme Court Cases by Chief Justice')
chief_justice_counts = cases['Chief Justice'].value_counts()
fig, ax = plt.subplots()
chief_justice_counts.plot(kind='bar', color='orange', ax=ax)
ax.set_title('Supreme Court Cases by Chief Justice')
ax.set_xlabel('Chief Justice')
ax.set_ylabel('Count')
st.pyplot(fig)

# Cases Over Time
st.header('Supreme Court Cases Impacting Racial Equality Over Time')
fig, ax = plt.subplots()
ax.plot(cases['Year'], cases['Case'], marker='o')
ax.set_title('Supreme Court Cases Impacting Racial Equality Over Time')
ax.set_xlabel('Year')
ax.set_ylabel('Case')
ax.grid(True)
st.pyplot(fig)

# Justices by State of Origin and Year Appointed
st.header('Supreme Court Justices by Year Appointed and State of Origin')
justices = justices.sort_values('Year Appointed')
fig, ax = plt.subplots(figsize=(15, 10))
bars = ax.barh(justices['Justice'], justices['Year Appointed'], color=justices['Color'])
for bar, justice_name, year, color in zip(bars, justices['Justice'], justices['Year Appointed'], justices['Color']):
    ax.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f' {year}', va='center', ha='left', fontsize=8, color='black')
    ax.text(bar.get_width() - 5, bar.get_y() + bar.get_height()/2, justice_name, va='center', ha='right', fontsize=8, color=color)
ax.set_xlabel('Year Appointed')
ax.set_ylabel('Justice Names')
ax.set_title('Supreme Court Justices by Year Appointed and State of Origin')
ax.grid(True)
st.pyplot(fig)
