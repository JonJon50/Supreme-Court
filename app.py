import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Creating the DataFrame from the given data
data = {
    'Justice': ["John Jay", "John Rutledge", "Oliver Ellsworth", "John Marshall", "Roger B. Taney", "Salmon P. Chase", "Morrison Waite", "Melville Fuller", "Edward Douglass White", "William Howard Taft", "Charles Evans Hughes", "Harlan F. Stone", "Fred M. Vinson", "Earl Warren", "Warren E. Burger", "William Rehnquist", "John Roberts", "Clarence Thomas", "Ruth Bader Ginsburg", "Stephen Breyer", "Samuel Alito", "Sonia Sotomayor", "Elena Kagan", "Neil Gorsuch", "Brett Kavanaugh", "Amy Coney Barrett", "Ketanji Brown Jackson"],
    'Year Appointed': [1789, 1795, 1796, 1801, 1836, 1864, 1874, 1888, 1910, 1921, 1930, 1941, 1946, 1953, 1969, 1986, 2005, 1991, 1993, 1994, 2006, 2009, 2010, 2017, 2018, 2020, 2022],
    'Race': ["White", "White", "White", "White", "White", "White", "White", "White", "White", "White", "White", "White", "White", "White", "White", "White", "White", "Black", "White", "White", "White", "Hispanic", "White", "White", "White", "White", "Black"]
}
df = pd.DataFrame(data)

# Creating the stacked bar chart
race_counts = df.groupby(['Year Appointed', 'Race']).size().unstack().fillna(0)
fig, ax = plt.subplots(figsize=(12, 6))
race_counts.cumsum().plot(kind='bar', stacked=True, ax=ax)

ax.set_title('Diversity of Supreme Court Justices Over Time')
ax.set_xlabel('Year Appointed')
ax.set_ylabel('Number of Justices')
ax.legend(title='Race')

st.pyplot(fig)


# Adding Tenure Length to the DataFrame and creating the line chart
data.update({
    'Tenure Length': [6, 1, 4, 34, 28, 9, 14, 22, 11, 9, 11, 4, 7, 16, 17, 19, 19, 33, 27, 27, 18, 15, 14, 7, 6, 4, 2]
})

df = pd.DataFrame(data)

# Grouping by year and race
avg_tenure = df.groupby(['Year Appointed', 'Race'])['Tenure Length'].mean().unstack()

# Creating the line chart
fig, ax = plt.subplots(figsize=(12, 6))
avg_tenure.plot(kind='line', ax=ax)

ax.set_title('Average Tenure Length of Supreme Court Justices Over Time')
ax.set_xlabel('Year Appointed')
ax.set_ylabel('Average Tenure Length (years)')
ax.legend(title='Race')

st.pyplot(fig)


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Creating the DataFrame for Supreme Court cases
cases_data = {
    'Case': ["Dred Scott v. Sandford", "Plessy v. Ferguson", "Brown v. Board of Education", "Loving v. Virginia", "Swann v. Charlotte-Mecklenburg", "Regents v. Bakke", "Grutter v. Bollinger", "Shelby County v. Holder"],
    'Decision': ["African Americans could not be citizens", "Upheld 'separate but equal'", "Segregation in public schools unconstitutional", "Invalidated laws prohibiting interracial marriage", "Upheld use of busing for desegregation", "Race can be a factor in college admissions", "Upheld affirmative action in university admissions", "Struck down parts of the Voting Rights Act"],
    'Year': [1857, 1896, 1954, 1967, 1971, 1978, 2003, 2013],
    'Chief Justice': ["Roger B. Taney", "Melville Fuller", "Earl Warren", "Earl Warren", "Warren E. Burger", "Warren E. Burger", "William Rehnquist", "John Roberts"],
    'Impact': ["Setback for racial equality, overturned by later amendments", "Legalized segregation", "Major victory for civil rights movement", "Ended race-based legal restrictions on marriage", "Promoted integration in schools", "Affirmed affirmative action with limitations", "Confirmed diversity as a compelling interest", "Weakened federal oversight of voting laws"]
}
cases_df = pd.DataFrame(cases_data)

# Creating the improved timeline chart
fig, ax = plt.subplots(figsize=(12, 6))

# Plotting the cases as scatter points with different colors
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange']
ax.scatter(cases_df['Year'], [1]*len(cases_df), c=colors[:len(cases_df)], s=100)

# Adding annotations for each case with matching colors
for i, (index, row) in enumerate(cases_df.iterrows()):
    ax.annotate(f"{row['Case']} ({row['Year']})", (row['Year'], 1),
                textcoords="offset points", xytext=(0,10), ha='left', rotation=50,
                fontsize=10, weight='bold', color=colors[i])

# Adding title, labels, and grid
ax.set_title('Impact of Key Supreme Court Cases on Racial Equality', fontsize=14)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Cases Names', fontsize=12)
ax.yaxis.set_ticks([])  # Hide the y-axis ticks but keep the label

# Improving the x-axis formatting
ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))

# Adding grid for better readability
ax.grid(True, axis='x', linestyle='--', alpha=0.7)

st.pyplot(fig)

