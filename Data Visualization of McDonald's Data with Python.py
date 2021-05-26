#!/usr/bin/env python
# coding: utf-8

# <img src = 'https://github.com/insaid2018/Term-1/blob/master/Images/INSAID_Full%20Logo.png?raw=true' width="240" height="360">
# 
# # Data Visualization in Python using McDonald's Data
# 
# <img src="https://raw.githubusercontent.com/insaid2018/Term-1/master/Images/banner.jpg" align='left'><br/>

# 
# ## Table of Contents
# 
# 1. [Introduction to Data Visualization](#section1)<br>
#      
# 2. [Packages in Python for Plotting](#section2)<br>
#      - 2.1. [Installing Packages](#section201)<br> 
#      - 2.2. [Importing the Packages](#section202)<br>
# 3. [Types of Plotting](#section3)
#      - 3.1. [Univariate Plotting with pandas](#section301)<br>
#           - 3.1.1. [Bar Charts](#section30101)<br>
#           - 3.1.2. [Line Charts](#section30102)<br>
#           - 3.1.3. [Area Charts](#section30103)<br>
#           - 3.1.4. [Histograms](#section30104)<br>
#           - 3.1.5. [Donut Chart](#section30105)<br><br>
#      - 3.2. [Bivariate Plotting](#section302)<br>
#           - 3.2.1. [Scatter Plot](#section30201)<br>
#           - 3.2.2. [Hexplot](#section30202)<br>
#           - 3.2.3. [Stacked Plots](#section30203)<br>
#           - 3.2.4. [Bivariate Linear Charts](#section30204)<br>
#           - 3.2.5. [Pair Plot](#section30205)<br><br>
#      - 3.3. [Multivariate Plotting](#section303)<br>
#           - 3.3.1. [Multivariate Scatter Plot](#section30301)<br>
#           - 3.3.2. [Grouped Boxplot ](#section30302)<br>
#           - 3.3.3. [Heat Map](#section30303)<br>
#           - 3.3.4. [Parallel Coordinates](#section30304)<br>
#           - 3.3.5. [Violin Plot](#section30305)<br><br>
# 4. [Interactive Charts using Bokeh](#section4)<br>
# 5. [Plotting Geographical Data using Plotly](#section5)<br>

# <a id=section1></a>
# ## 1. Introduction to Data Visualization
# 
# - Data is only as good as it’s presented.
# 
# 
# - **Data visualization** is one of the **core skills** in **data science**. In order to start building useful models, we need to understand the underlying dataset. You might not be an expert on the subject of the data you're working with, and will always need to explore the variables in great depth before you can move on to building a model or doing something else with the data.
# 
# 
# - Effective data visualization is the most important tool in your arsenal for getting this done, and hence a critical skill for you to master.
# 
# 
# - **Also data visualization helps in understanding the problem better, and if you understand the problem better, there are higher chances that you'll find a better solution for it, and that too in less time**. 
# 
# 
# ### Why Plotting??
# 
# - Visual representation helps humans to inspect and understand better. 
# 
# 
# - **Humans process visual inputs better and faster than all other types of inputs**. This is the key reason for visualizing data. 
# 
# 
# - When the representation of data is pictorial it’s easier to find patterns, digest the data and develop insights to solve the problems.
# 
# <img src="https://github.com/insaid2018/Term-1/blob/master/Images/gp-2.png?raw=true" width=750 height=750><br/>
# 
# - From the above figure you can see that its easier for us to process images rather than text, visuals are processed __60k__ times faster than texts.

# <a id=section2></a>
# ## 2. Packages in Python for Plotting 
# 
# - There are various packages available in Python for visualization purpose. Some of them are: __matplotlib, pandas, seaborn, bokeh, plotly__, etc. 
# 
# 
# - Each package has its own utility and which package to use depends mainly on the type of dataset, problem to solve and what you want to infer from it.
# 
# 
# - Here we will mainly use **matplotlib, pandas, seaborn, bokeh, and plotly.**

# <a id=section201></a>
# ### 2.1 Installing Packages
# 
# - Commonly used packages are:
#   - matplotlib
#   - pandas
#   - seaborn  
#   - bokeh 
#   - plotly
# 
# 
# - To **install** the required **multiple packages**, below are the commands to use:
# <br>
# 
#   - Using **pip**: ```pip install matplotlib pandas seaborn bokeh plotly```
# <br>  or  <br>
#   - Using **conda**: ```conda install matplotlib pandas seaborn bokeh plotly```
#   
#   Type anyone of the above commands either in **Anaconda Prompt** or in **Jupyter Notebook code cell** and **execute**.

# <a id=section202></a>
# ### 2.2 Importing the Packages
# 
# - **Import** all the **modules** and give them **suitable aliases**, so that you don't have to repeatedly use the longer form of the name.

# In[1]:


import numpy as np
np.set_printoptions(precision=4)                    # To display values only upto four decimal places. 

import pandas as pd
pd.set_option('mode.chained_assignment', None)      # To suppress pandas warnings.
pd.set_option('display.max_colwidth', -1)           # To display all the data in each column
pd.options.display.max_columns = 50                 # To display every column of the dataset in head()

import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')                  # To apply seaborn whitegrid style to the plots.
get_ipython().run_line_magic('matplotlib', 'inline')

import seaborn as sns
sns.set(style='whitegrid', font_scale=1.3, color_codes=True)      # To adjust seaborn settings for the plots.

import warnings
warnings.filterwarnings('ignore')                   # To suppress all the warnings in the notebook.


# In[2]:


# Importing the parallel_coordinates from pandas.plotting which will help in plotting the Parallel Coordinates.

from pandas.plotting import parallel_coordinates


# In[3]:


# Install and update plotly using this command to the latest version (higher than version 4.0.0)

get_ipython().system('pip install plotly --upgrade')


# In[4]:


# Install chart_studio, please use this command. 

get_ipython().system('pip install chart-studio')


# <a id=section3></a>
# ## 3. Types of Plotting
# 
# - On the basis of the **number of variables** you want to see **relationship in between**, plotting can be classified as:
# <br>
# 
#   - **Univariate** Plotting
# <br><br>  
#   - **Bivariate** Plotting 
# <br><br>
#   - **Multivariate** Plotting

# <a id=section301></a>
# ## 3.1 Univariate Plotting with pandas
# 
# <table style="border: 2px solid black; border-collapse: collapse">
# 
# <tr>
# <td style="border-right: 2px solid black; border-bottom: 2px solid black"><img src="https://i.imgur.com/skaZPhb.png" width="350px"/></td>
# <td style="border-right: 2px solid black; border-bottom: 2px solid black"><img src="https://i.imgur.com/gaNttYd.png" width="350px"/></td>
# <td style="border-right: 2px solid black; border-bottom: 2px solid black"><img src="https://i.imgur.com/pampioh.png"/></td>
# <td style="border-right: 2px solid black; border-bottom: 2px solid black"><img src="https://i.imgur.com/OSbuszd.png"/></td>
# <td style="border-right: 2px solid black; border-bottom: 2px solid black"><img src="https://raw.githubusercontent.com/insaid2018/Term-2/master/images/donut.png"/ width="350px"></td>
# 
# </tr>
# 
# 
# 
# <tr>
# <td style="font-weight:bold; font-size:16px; text-align:center; border-right: 2px solid black">Bar Chat</td>
# <td style="font-weight:bold; font-size:16px; text-align:center; border-right: 2px solid black">Line Chart</td>
# <td style="font-weight:bold; font-size:16px; text-align:center; border-right: 2px solid black">Area Chart</td>
# <td style="font-weight:bold; font-size:16px; text-align:center;border-right: 2px solid black">Histogram</td>
# <td style="font-weight:bold; font-size:16px; text-align:center">Donut Chart</td>    
# 
# </tr>
# 
# <tr>
# <td style="font-size:14px; text-align:center; border-right: 2px solid black">df.plot.bar()</td>
# <td style="font-size:14px; text-align:center; border-right: 2px solid black">df.plot.line()</td>
# <td style="font-size:14px; text-align:center; border-right: 2px solid black">df.plot.area()</td>
# <td style="font-size:14px; text-align:center; border-right: 2px solid black">df.plot.hist()</td>
#     
# <td style="font-size:14px; text-align:center">df.plot.pie()</td>
# </tr>
# 
# <tr>
# <td style="font-size:14px; text-align:center; border-right: 2px solid black">Good for nominal and small ordinal categorical data.</td>
# <td style="font-size:14px; text-align:center; border-right: 2px solid black">Good for ordinal categorical and interval data.</td>
# <td style="font-size:14px; text-align:center; border-right: 2px solid black">Good for ordinal categorical and interval data.</td>
# <td style="font-size:14px; text-align:center; border-right: 2px solid black">Good for interval data.</td>
#     
# <td style="font-size:14px; text-align:center">Good for categorical count representation.</td>
# </tr>
# 
# </table>
# 
# <br>
# 
# - The **pandas** library is the **core library** for Python **data analysis**. However, it can do more than loading and transforming your data, it **can visualize** it too! Indeed, the **easy-to-use** and expressive pandas plotting API is a big reason behind pandas popularity.
# 
# 
# - In this section we will learn the basic pandas plotting facilities, starting with the simplest type of visualization: single-variable or __Univariate__ visualizations. This includes basic tools like __bar plots and line charts__. Through these we'll get an understanding of pandas plotting library structure, and spend some time examining data types.

# ### Disclaimer: The images are only for illustration purpose. Please don't compare them with our data.

# ### Loading the Dataset

# In this **Data Visualization** sheet we are going to use two datasets of **McDonald's India**. 
# 
# <img src="https://raw.githubusercontent.com/insaid2018/Term-1/master/Images/mcdonalds_logo.jpg" width=750 height=750><br/>
# 
# 1. **Nutrition Facts for McDonald's Menu** dataset: This dataset contains information about the **nutritional content** present in different items of **McDonald's India Menu**.
# 
# 
# 2. **McDonald's Store Information** dataset: This dataset contains information about various **McDonald's stores** in **India**. 

# **Importing 1st Dataset**

# In[5]:


# Importing the 1st dataset (Nutrition Facts for McDonald's Menu dataset).

df_mcd = pd.read_excel('https://github.com/insaid2018/Term-1/raw/master/Data/Casestudy/mcdonalds_india_menu.xlsx')
df_mcd.head()


# #### Description of the Dataset
# 
# - This dataset provides a **nutrition analysis** of every menu item on the **India's McDonald's menu**, including breakfast, chicken wings, shake, snacks, hot beverages, cold beverages and desserts.
# 
# 
# - Detailed information about each nutrient column can be found at this [link](https://www.fda.gov/food/nutrition-education-resources-materials/how-understand-and-use-nutrition-facts-label).
# 
# 
# | Column Name                    | Description                                                                                |
# | -------------------------------|:------------------------------------------------------------------------------------------:| 
# | Category                       | The category to which an item belong to.                                                   | 
# | Item                           | Name of the item.                                                                          | 
# | Serve_Size                     | The weight of a single serving (g).                                                        | 
# | Energy                         | Number of calories in the item (kcal).                                                     |
# | Protein                        | Protein in the item (g).                                                                   |
# | Total_Fat                      | Total Fat in the item (g).                                                                 |
# | Saturated_Fat                  | Saturated Fat in the item (g).                                                             |
# | Trans_Fat                      | Trans Fat in the item (g).                                                                 |
# | Cholestrol                     | Cholestrol in the item (mg).                                                               |
# | Carbohydrates                  | Carbohydrates in the item (g).                                                             |
# | Sugars                         | Sugars in the item (g).                                                                    |
# | Dietary_Fibre                  | Dietary Fibres in the item (g).                                                            |
# | Sodium                         | Sodium in the item (mg).                                                                   |
# | High_Or_Low_Sugar              | Whether the item have a high sugar content or low sugar content (High Sugar, Low Sugar).   |
# 
# 
# <img src="https://raw.githubusercontent.com/insaid2018/Term-1/master/Images/Mcd.png" width=750 height=750><br/>
# 

# **Importing 2nd Dataset**

# In[6]:


# Importing the 2nd dataset (McDonald's Store Information dataset).

df_store = pd.read_excel('https://github.com/insaid2018/Term-1/raw/master/Data/Casestudy/mcdonalds_store_data.xlsx')
df_store.head()


# #### Description of the Dataset
# 
# - This dataset provides information different **McDonald's India stores** like their Store ID, Address, City, State, Revenue, Profits, Number of Employees, Most Selling Item, etc.
# 
# 
# | Column Name                    | Description                                                                                |
# | -------------------------------|:------------------------------------------------------------------------------------------:| 
# | Company                        | Company of the store.                                                                      | 
# | Store ID                       | ID of the store.                                                                           | 
# | Store Name                     | Name of the store.                                                                         | 
# | Address                        | Address of the store.                                                                      |
# | City                           | City of the store.                                                                         |
# | State                          | State of the store.                                                                        |
# | Postcode                       | Postcode of the store.                                                                     |
# | Longitude                      | Longitude of the store.                                                                    |
# | Latitude                       | Latitude of the store.                                                                     |
# | Revenue                        | Revenue of the store.                                                                      |
# | Profits                        | Profits of the store.                                                                      |
# | Selling Price                  | Total Selling Price of items of the store.                                                 |
# | Cost Price                     | Total Cost Price of items of the store.                                                    |
# | Gross Profit Margin            | Gross Profit Margin of the store.                                                          |
# | Number of Employees            | Number of employees of the store.                                                          |
# | Most Prefered Meal             | Most preferred meal of the store.                                                          |
# | Most Selling Item              | Most selling item of the store.                                                            |
# 
# <img src="https://raw.githubusercontent.com/insaid2018/Term-1/master/Images/store.jpg" width=750 height=750><br/>
# 

# - This notebook will aim to visualize the **nutritional content** of the various **offerings** provided in this **McDonald's Indian Menu** dataset. 
# 
# 
# - We will also **visualize** the information related to **different stores** of **McDonald's India** franchise.
# 
# 
# - We will start with the **Univariate analysis** of the dataset.

# <a id=section30101></a>
# ### 3.1.1. Bar Charts 
# 
# - Bar charts are one of the simplest tool for data visualization.
# 
# 
# - The **bar-chart** is useful for **categorical data** that doesn’t have a lot of different categories. <br>
# 
#   - They **map categories** to **numbers**.

# In[7]:


# Using pandas plot.bar function to plot the bar chart for the Category column of the dataframe df_mcd.

df_mcd['Category'].value_counts().plot.bar(figsize=(15,7), colormap='Dark2', fontsize=13, yticks=np.arange(0, 19, 2))

# Using matplotlib to add labels and title to the plot. 
# Pandas and matplotlib are linked with each other in the notebook by the use of this line in the Imports: %matplotlib inline

plt.xlabel('Category')
plt.ylabel('Number of Items')
plt.title('Bar Chart showing the Number of Items in each Category value')

# In order to save your plot into an image on your system, use the following command.
# The image will be saved in the directory of this notebook.

plt.savefig('barchart.png')   


# - We can see that the number of **Cold Beverages** is **highest** in our dataset with **18 items** corresponding to this category as seen from **Cold Beverages** bar.
# 
# 
# - What if we want to know what **percent of the total** is **Cold Beverages** or **Desserts**?
# 
# 
# - This bar chart plots the __absolute numbers__, but we can also plot the __relative proportions__ of each category.

# In[8]:


# Using pandas plot function to plot the bar chart for the Category column of the dataframe df_mcd.
# Using the kind='bar' to plot a bar chart. This method provides a lot of flexibility as different type of plots can be plotted
# just by changing the kind attribute.
# Here we are calculating the proportion by diving the each Category frequency with the number of rows (length) of the dataset.

(df_mcd['Category'].value_counts() / len(df_mcd)).plot(kind='bar', figsize=(16,7), colormap='magma', fontsize=13)

plt.xlabel('Category')
plt.ylabel('Proportion of Items')
plt.title('Bar Chart showing the proportion of Items in each Category value')


# - It is visible from the above plot that about **60% items** belong to the **Cold Beverages, Desserts** and **Sandwiches and Wraps** categories of **Category** column. 
# 
# 
# - **What did you have when you last visited a McDonald's?** 
# 
# 
# <img src="https://raw.githubusercontent.com/insaid2018/Term-1/master/Images/ChickenWrap.jpg" width=800 height=750><br/>

# <a id=section30102></a>
# ### 3.1.2. Line Charts
# 
# - A line chart can pass over **any number of individual values**, making it the tool of first choice for distributions with **many unique values or categories**. 
# 
# 
# - They are also **good for depicting trends** for different categories __over__ the same **period of time**, to aid comparison.

# In[9]:


# Using pandas plot function to plot the line chart for the Energy column.
# Using the kind='line' to plot a line chart. 

df_mcd[['Energy']].plot(kind='line', figsize=(15,7), color='blue', fontsize=13, linestyle='-.')

plt.xlabel('Index')
plt.ylabel('Energy (kcal)')
plt.title('Line chart showing the variation of energy across different items')


# In[10]:


df_mcd.iloc[:28]['Category'].value_counts()


# - This plot shows the **trend** followed by **Amount of Calories (Energy)** present in **different items** on our **menu**.
# 
# 
# - We can see that the **menu items** at the **beginning** of the dataset have **very high energy content** when **compared to** the **items at the end**.
# 
# <img src="https://raw.githubusercontent.com/insaid2018/Term-1/master/Images/fries1.jpg" width=650 height=550><br/>

# <a id=section30103></a>
# ### 3.1.3. Area Charts
# 
# - Area charts are line charts, but with the __area under the line shaded in.__
# 
# 
# - Area charts are useful as they give a sense of the overall **volume**, as well as the **proportion** taken up by each category.

# In[11]:


# Using pandas plot function to plot the area chart for the Total_Fat column.
# Using the kind='area' to plot a area chart. 

df_mcd['Total_Fat'].plot(kind='area', figsize=(15,7), color='violet', fontsize=13)
                                                                    
plt.xlabel('Index')
plt.ylabel('Total_Fat')
plt.title('Area chart showing the variation of Total Fat across different items')


# In[12]:


print(df_mcd.iloc[15:28]['Category'].value_counts())

print('\n\nThe item with highest Total Fat belongs to', df_mcd.iloc[df_mcd.iloc[15:28]['Total_Fat'].argmax()]['Category'])


# - The **categories** having **high Total Fat** value are **Sandwiches and Wraps, Snacks, Nuggets, Chicken Wings**. 
# 
# <img src="https://raw.githubusercontent.com/insaid2018/Term-1/master/Images/chicken_wings2.png" width=450 height=450> 

# <a id=section30104></a>
# ### 3.1.4. Histograms

# - **Histograms** are great for **illustrating distributions** of your **data**.
# 
# 
# - The **continuous variable** shown on the X-axis is **broken into discrete intervals** and the **number of data samples** you have in that discrete interval **determines the height of the bar**.

# In[13]:


# We want to check the histogram on the Serve_Size column.

df_mcd['Serve_Size'].head(10)


# In[14]:


# Using pandas plot function to plot the histogram for the Serve_Size column.
# Using the kind='hist' to plot a histogram.

bins = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
df_mcd['Serve_Size'].plot(kind='hist', bins = bins, figsize=(15, 7), color='brown', yticks=np.arange(0, 22, 3), xticks=bins)

plt.xlabel('Serve_Size')
plt.ylabel('Frequency')
plt.title('Histogram showing the distribution of Serve Size values')


# #### Kernel Density Estimation (KDE) Plot
# 
# - A **Density Plot** visualizes the **distribution of data** over a **continuous interval** or **time period**. 
# 
# 
# - This chart is a **variation of a Histogram** that uses **smoothing to plot values**, allowing for **smoother distributions** by smoothing out the noise. 
# 
# 
# - The **peaks** of a **Density Plot** help display where **values are concentrated** over the **interval**.
# 
# 
# - An **advantage Density Plots** have **over Histograms** is that they're **better at determining the distribution shape** because they're **not affected by the number of bins used**. 

# In[15]:


# Using pandas plot function to plot the kde plot for the Energy column.
# Using the kind='plot' to plot a kde plot.

df_mcd['Serve_Size'].plot(kind='kde', figsize=(15, 7), color='black')

plt.xlabel('Serve Size')
plt.ylabel('Density')
plt.title('KDE plot showing the density of Serve_Size values')


# - The data in **Serve_Size** column is somewhat following a **normal distribution**, as the shape of the density plot is similar to the **bell-shaped curve** of the **normal distribution**.
# 
# 
# - The only **analytical difference** between a **barplot** and **histogram** is that instead of each bar representing a single value, it represents __a range of values__.
# 
# 
# - However, since histograms break space up into even intervals, so __they don't deal very well with skewed data__.

# <a id=section30105></a>
# ### 3.1.5.  Donut Chart

# - __Donut Chart__ (also known as Doughnut chart) is a **variation of a Pie chart** except it is hollow in the __center__ which makes it look like a **donut**, hence the name.
# 
# 
# - __Pie Charts__ are sometimes criticised for focusing readers on the __proportional areas__ of the slices to one another and to the chart as a whole. This makes it tricky to see the differences between slices, especially when you try to __compare multiple Pie Charts together__.
# 
# 
# - A __Donut Chart__ somewhat remedies this problem by __de-emphasizing__ the use of the area. Instead, readers focus more on reading the __length of the arcs__, rather than __comparing__ the proportions between __slices__.
# 
# 
# - Also, __Donut Charts__ are more __space-efficient than Pie Charts__ because the __blank space__ inside a __Donut Chart__ can be used to __display information__ inside it.

# In[16]:


# Using pandas plot function to plot a donut plot of the Category column.
# Using kind='pie' to plot a donut plot, also setting explode values so that it takes a donut shape instead of a pie shape.

space = np.ones(11)/10
df_mcd['Category'].value_counts().plot(kind='pie', explode=space, fontsize=14, autopct='%3.1f%%', wedgeprops=dict(width=0.15), 
                                       shadow=True, startangle=160, figsize=(10,10), cmap='inferno', legend=True)

plt.ylabel('Category')
plt.title('Donut Plot showing the proportion of each Category value')


# - From the above __donut plot__ we can see the __share__ of each __Category__ value in the data.
# <br> <br>
#   - __Larger strip__ on the __donut__ represents a **higher share** of a particular **Category**.
# <br> <br>  
#   - Here **Cold Beverages** have the **highest share** with **21.7%** samples belonging to this category.

# <a id=section302></a>
# ## 3.2 Bivariate Plotting
# 
# <table style="border: 2px solid black; border-collapse: collapse">
# 
# <tr>
# <td style="border-right: 2px solid black; border-bottom: 2px solid black"><img src="https://i.imgur.com/bBj1G1v.png" width="350px"/></td>
# <td style="border-right: 2px solid black; border-bottom: 2px solid black"><img src="https://i.imgur.com/ChK9zR3.png" width="350px"/></td>
# <td style="border-right: 2px solid black; border-bottom: 2px solid black"><img src="https://i.imgur.com/KBloVHe.png" width="350px"/></td>
# <td style="border-right: 2px solid black; border-bottom: 2px solid black"><img src="https://i.imgur.com/C7kEWq7.png" width="350px"/></td>
# <td style="border-bottom: 2px solid black"><img src="https://seaborn.pydata.org/_images/seaborn-pairplot-1.png" width="350px"/> 
# </tr>
# 
# <tr>
# <td style="font-weight:bold; font-size:16px; text-align:center; border-right: 2px solid black">Scatter Plot</td>
# <td style="font-weight:bold; font-size:16px; text-align:center; border-right: 2px solid black">Hex Plot</td>
# <td style="font-weight:bold; font-size:16px; text-align:center; border-right: 2px solid black">Stacked Bar Chart</td>
# <td style="font-weight:bold; font-size:16px; text-align:center; border-right: 2px solid black">Bivariate Line Chart</td>
# <td style="font-weight:bold; font-size:16px; text-align:center">Pair Plot</td>    
# </tr>
# 
# <tr>
# <td style="font-size:14px; text-align:center; border-right: 2px solid black">df.plot.scatter()</td>
# <td style="font-size:14px; text-align:center; border-right: 2px solid black">df.plot.hex()</td>
# <td style="font-size:14px; text-align:center; border-right: 2px solid black">df.plot.bar(stacked=True)</td>
# <td style="font-size:14px; text-align:center; border-right: 2px solid black">df.plot.line()</td>
# <td style="font-size:14px; text-align:center">sns.pairplot()</td>    
# </tr>
# 
# <tr>
# <td style="font-size:14px; text-align:center; border-right: 2px solid black">Good for interval and some nominal categorical data.</td>
# <td style="font-size:14px; text-align:center; border-right: 2px solid black">Good for interval and some nominal categorical data.</td>
# <td style="font-size:14px; text-align:center; border-right: 2px solid black">Good for nominal and ordinal categorical data.</td>
# <td style="font-size:14px; text-align:center; border-right: 2px solid black">Good for ordinal categorical and interval data.</td>
# <td style="font-size:14px; text-align:center">Good for finding pairwise relationship in the data.</td>    
# </tr>
# 
# </table>
# 
# <br>
# 
# - Data without __relationships__ between variables is equivalent to a blank canvas. To paint the picture in, we need to understand how variables __interact__ with one another.
#   
#   - Does an increase in one variable __correlate__ with an increase in another?
#   
#   - Does it __relate__ to a decrease somewhere else?
# 
# 
# - The best way to paint the picture is by using plots that enable these possibilities.

# <a id=section30201></a>
# ### 3.2.1. Scatter Plot
# 
# - The simplest bivariate plot is the **scatter plot**. 
# 
# 
# - A scatter plot __maps__ each __variable__ of interest to a __point in two-dimensional space__.

# In[17]:


# Using pandas plot function to plot the scatter plot for the Energy and Carbohydrates columns.
# Using the kind='scatter' to plot a scatter plot.

df_mcd.plot(kind='scatter', x='Carbohydrates', y='Energy', figsize=(10, 6), color='purple', grid=False)

plt.title('Scatter plot showing the variation of Energy with Carbohydrates present in each item')


# - Here we can see the variation of **Energy** with respect to change in **Carbohydrates**.
# 
# 
# <img src="https://raw.githubusercontent.com/insaid2018/Term-1/master/Images/Correl.png" width=650 height=550> <br>
# 
# <img src="https://raw.githubusercontent.com/insaid2018/Term-1/master/Images/corr3.png" width=600 height=500> <br>
# 
# 
# - It is quite evident that there is a **positive correlation** between the **two variables**, as the **Energy** present in an item **increases** with the **Carbohydrates** present in it.
# 
# <img src="https://raw.githubusercontent.com/insaid2018/Term-1/master/Images/calories.jpg" width=750 height=650> <br>
# 
# 
# #### Regplot:
# 
# - Another way to plot the **scatter plot** is using **Seaborn's regplot**. <br><br>
# 
#   - The **regplot** plots the data along with a **linear regression model fit** showing the **rate of change of one variable with respect to the other**.
# <br><br>  
#   - If the line is moving from the bottom-left corner to the top-right corner then there is a **positive correlation** between the variables, and if the line if moving form the top-left corner to the bottom-right corner then there is a **negative correlation** between the variables.

# In[18]:


# Using seaborn's regplot function to plot the scatter plot for the Energy and Carbohydrates columns with the regression line.

plt.figure(figsize=(12,7))
sns.regplot(data=df_mcd, x='Carbohydrates', y='Energy', color='brown')

plt.title('Regplot showing the variation of Energy with Carbohydrates present in each item')


# - Using this **regplot** we can clearly see the relationship between the two variables **Energy** and **Carbohydrates**.<br><br>
# 
#   - The **regression line** is moving from the bottom-left corner to the top-right corner, which tells us that there is a **positive correlation** between the two variables. 
# 
# <br>
# 
# - A shortcoming of the scatter plots is that **scatter plots do not effectively treat points which map to the same place**.<br><br>
#   - For example, if two items, both having **30** value of **Carbohydrates**, have an **Energy** value of **50**, then the **second one is overplotted onto the first one**, and we add just one point to the plot.<br> <br> 
#   
#   - This isn't a problem if it happens just a few times. But with enough points the distribution starts to look like a shapeless blob.
# 
# <br>  
# 
# - An interesting way to solve the above mentioned problem is to use our next plot type, a **hexplot**.

# <a id=section30202></a>
# ### 3.2.2 Hexplot
# 
# 
# - A  hexplot __aggregates points in space into hexagons__, and then __colorize those hexagons__.

# In[19]:


# Using pandas plot function to plot the hexplot for the Energy and Serve_Size columns.
# Using the kind='hexbin' to plot a hexplot.

df_mcd.plot(kind='hexbin', x='Serve_Size', y='Energy', figsize=(15, 7), gridsize=25, fontsize=13, colormap='Reds')

plt.title('Hexplot showing the variation of Energy with Serve_Size of each item')


# - The hexplot provides us a different point of view, showing that the **maximum density of points** lie in the __Serve_Size__ range of **100 to 300**.
# 
# <img src="https://raw.githubusercontent.com/insaid2018/Term-1/master/Images/serve2.jpg" width=650 height=550> <br>
# 
# <br>
# 
# 
# - Hexplots and scatter plots can be applied to combinations of __interval variables or ordinal categorical variables__. 

# <a id=section30203></a>
# ### 3.2.3 Stacked Plots
# 
# 
# - The easiest way to **modify bar charts** to support another __visual variable__ is by using __stacking__. 
# 
# 
# - A **stacked chart** is one which **plots the variables one on top of the other**.

# - Many pandas multivariate plots expect input data to be in this format, with: <br> <br> 
#  
#   - One categorical variable in the columns
# <br> <br>
#   - One categorical variable in the rows
# <br> <br> 
#   - Counts of their intersections in the entries.

# In[20]:


# Using pandas plot function to plot the stacked bar chart for the Total_Fat, Saturated_Fat and Trans_Fat columns.
# Using the kind='bar' to plot a bar chart.
# This chart shows the amount of Saturated_Fat and Trans_Fat in each category with respect to the Total_Fat.

df_mcd.groupby(['Category'])['Total_Fat'].mean().plot(kind='bar', figsize=(15, 7), color='orange')
df_mcd.groupby(['Category'])['Saturated_Fat'].mean().plot(kind='bar', figsize=(15, 7), color='grey')
df_mcd.groupby(['Category'])['Trans_Fat'].mean().plot(kind='bar', figsize=(15, 7), color='red', fontsize=13)

plt.xlabel('Category')
plt.ylabel('Fat Content')
plt.title('Stacked Bar Chart showing the Fat content of each Category')
plt.legend(labels=('Total_Fat', 'Saturated_Fat', 'Trans_Fat'))


# - Here we can see the amount of different **fats** in each category. **Saturated_Fat is red, Trans_Fat is blue** and **Total_Fat is yellow**.
# 
# 
# - **Trans fats** only occur in **small amounts in meat and milk fat**, that's why they show such a low content in the chart.
# 
# 
# <img src="https://raw.githubusercontent.com/insaid2018/Term-1/master/Images/bad_fats1.jpg" width=750 height=650> <br>
# 
# 
# - **Stacked bar plots** share the __strengths__ and __weaknesses__ of __univariate bar charts__. 
# 
# 
# - They work best for __nominal categorical__ or __small ordinal categorical variables__.

# In[21]:


# Using pandas plot function to plot the stacked area chart for the Revenue and Profits columns of df_store dataframe.
# Using the kind='area' to plot a bar chart.
# You can specify color using their hex code as well. (Just type any 6 random digits after #)

df_store.groupby(['Customers'])['Revenue'].mean().plot(kind='area', figsize=(15, 7), color='#347593')
df_store.groupby(['Customers'])['Profits'].mean().plot(kind='area', figsize=(15, 7), color='#363552', fontsize=13)


plt.xlabel('Customers')
plt.ylabel('Value')
plt.title('Stacked Area Chart showing the Revenue and Profit in each state')
plt.legend(labels=('Revenue', 'Profits'))


# - We can see that as the **number of customers increase**s the **Revenue of stores** also **increases** and the **Profits increases** as well. **Profits** are always a **small portion** of the **total revenue**.
# <br><br>
# 
# 
# - Like single-variable area charts, multivariate area charts are meant for __nominal categorical__ or __interval variables__.
# 
# <br>
# 
# - Stacked plots are visually very pretty. However, they suffer from two major problems: <br> <br>
# 
#   - The __first limitation__ is that the second variable in a stacked plot __must be a variable__ with a very **limited number of possible values** (probably an ordinal categorical), like in the above example, we only have a few categories in **State** column. <br> <br>
# 
#   - The __second limitation__ is one of __interpretability__. Its really hard to distinguish the values within a stacked plot, if **contrasting colors (like our example)** aren't used.

# <a id=section30204></a>
# ### 3.2.4 Bivariate Linear Charts
# 
# - Bivariate Linear Chart remains __highly effective__ when made. <br> <br>
#   
#   - The line in this chart takes up so __little visual space__, it's really easy and effective to overplot multiple lines on the same chart.

# In[22]:


# Using pandas plot function to plot the bivariate line chart for Cholestrol, and Total_Fat columns on the basis of Serve_Size.
# Using the kind='line' to plot a line chart.

df_mcd.groupby(['Serve_Size'])['Cholestrol'].mean().plot(kind='line', figsize=(15, 7), color='green')
df_mcd.groupby(['Serve_Size'])['Total_Fat'].mean().plot(kind='line', figsize=(15, 7), color='red')

plt.ylabel('Value')
plt.title('Bivariate Linear Chart showing the variation of Cholestrol and Total_Fat with Serve_Size')
plt.legend(['Cholestrol (in mg)', 'Total_Fat (in g)'])


# - For different **serve size**s the **amount of Total Fat (in grams)** and **Cholestrol (in miligrams) follows** a **similar trend**. As the **amount** of **Total Fat increases** the **amount of Cholestrol also increases** with it for each serve size.
# 
# 
# - Using a line chart this way **solves** the second **limitation of stacked plotting**. Bivariate line charts are much more __interpretable__: we have plotted different variables, but still we are able to see the trend they all follow clearly.

# <a id=section30205></a>
# ### 3.2.5 Pair Plot
# 
# 
# - To plot pairwise relationship in a dataset.
# 
# 
# - By default, this function will __create a grid of axes__ such that each variable in data will be __shared in y-axis across a single row__ and in the __x-axis across a single column__. The __diagonal axes__ are treated differently, drawing a lot to show the __univariate distribution__ of the data for the variable in that column.
# 
# 
# - It is also possible to show a **subset of variables** or **plot different variables** on the rows and columns.
# 
# 
# - This is a __high-level interface PairGrid__ that is intended to make it easy to draw a few common style. We should use __PairGrid__ directly if we need more flexibility.

# In[23]:


# Using seaborn's pairplot function to plot the pairplot for specific columns of the dataset.

sns.pairplot(data=df_mcd[['Energy', 'Total_Fat', 'Sugars', 'Carbohydrates', 'Protein']], size=2.5, diag_kind='kde')


# - Seaborn **pairplot** function makes it very easy to make a pairplot in a single line of code, showing the **bivariate relation** between each **pair of features**.
# 
# 
# - The **highest positive correlation** can be seen between **Energy** and **Total_Fat** columns.
# 
# 
# - The __diagonal elements__ in a __pairplot__ show the __frequency distribution of that column__.

# <a id=section303></a>
# ## 3.3 Multivariate Plotting
# 
# <table style="border: 2px solid black; border-collapse: collapse">
# 
# <tr>
# <td style="border-right: 2px solid black; border-bottom: 2px solid black"><img src="https://i.imgur.com/gJ65O47.png" width="350px"/></td>
# <td style="border-right: 2px solid black; border-bottom: 2px solid black"><img src="https://i.imgur.com/3qEqPoD.png" width="350px"/></td>
# <td style="border-right: 2px solid black; border-bottom: 2px solid black"><img src="https://i.imgur.com/1fmV4M2.png" width="350px"/></td>
# <td style="border-right: 2px solid black; border-bottom: 2px solid black"><img src="https://i.imgur.com/H20s88a.png" width="350px"/></td>
# <td style="border-bottom: 2px solid black"><img src="https://seaborn.pydata.org/_images/seaborn-swarmplot-5.png" width="350px"/></td>
# </tr>
# 
# <tr>
# <td style="font-weight:bold; font-size:16px; text-align:center; border-right: 2px solid black">Multivariate Scatter Plot</td>
# <td style="font-weight:bold; font-size:16px; text-align:center; border-right: 2px solid black">Grouped Box Plot</td>
# <td style="font-weight:bold; font-size:16px; text-align:center; border-right: 2px solid black">Heatmap</td>
# <td style="font-weight:bold; font-size:16px; text-align:center; border-right: 2px solid black">Parallel Coordinates</td>
# <td style="font-weight:bold; font-size:16px; text-align:center">Swarm plot</td>    
# </tr>
# 
# <tr>
# <td style="font-size:14px; text-align:center; border-right: 2px solid black">sns.scatterplot()</td>
# <td style="font-size:14px; text-align:center; border-right: 2px solid black">sns.boxplot()</td>
# <td style="font-size:14px; text-align:center; border-right: 2px solid black">sns.heatmap()</td>
# <td style="font-size:14px; text-align:center; border-right: 2px solid black">pd.plotting.parallel_coordinates()</td>
# <td style="font-size:14px; text-align:center">sns.swarmplot()</td>    
# </tr>
# 
# <tr>
# <td style="font-size:14px; text-align:center; border-right: 2px solid black">Good for interval and some nominal categorical data.</td>
# <td style="font-size:14px; text-align:center; border-right: 2px solid black">Good for interval and some nominal categorical data.</td>
# <td style="font-size:14px; text-align:center; border-right: 2px solid black">Good for nominal and ordinal categorical data.</td>
# <td style="font-size:14px; text-align:center; border-right: 2px solid black">Good for ordinal categorical and interval data.</td>
# <td style="font-size:14px; text-align:center">Good for drawing categorical variable with non-overlapping points.</td>
# </tr>
# 
# </table>
# 
# <br>
# 
# - In this section we'll explore __multivariate charts__.

# #### Adding more Visual Variables
# 
# - The most obvious way to plot lots of variables is to __augement the visualizations__ with even more visual variables.
# 
# 
# - A **visual variable** is any visual **dimension or marker** that we can use to **perceptually distinguish two data elements from one another**. 
#  
#  
# - Examples include **size, color, shape**, and **one, two, and even three dimensional position**.
# 
# 
# - __Good__ multivariate data displays are ones that make __efficient, easily-interpretable use of these parameters__.

# <a id=section30301></a>
# ### 3.3.1 Multivariate Scatter Plots

# In[24]:


# Using seaborn's scatterplot function to plot the scatter plot for the Energy and Sugars columns.
# Setting hue='Category' to give different colors to the data points based on the category they belong to.

plt.figure(figsize=(12,8))
sns.scatterplot(data=df_mcd, x='Sugars', y='Energy', hue='Category')

plt.xlabel('Sugars')
plt.ylabel('Energy')
plt.title('Scatter plot showing the variation of Energy with Sugars present in each item with a hue based on Category')
plt.grid(False)
plt.legend(fontsize=12)


# - This scatterplot uses **three visual variables**: <br><br>
# 
#   - The horizontal position __(x-value)__ tracks the __Sugars__ column (Sugar content). 
#   
#   - The vertical position __(y-value)__ tracks the __Energy__ column (Energy output). 
#   
#   - And the color (the __hue parameter__) tracks the **Category** column (Category to which the item belongs).
# 
# 
# - The new variable in this chart is __hue__.<br/>
#   
#   - **Hue** provides an __aesthetically pleasing visual__.
#   
# 
# - The **Sandwiches and Wraps** category have the **highest Energy output** with the **least Sugar content**.
# 
# <img src="https://raw.githubusercontent.com/insaid2018/Term-1/master/Images/PaneerWrap.jpg" width=450 height=450> <br>

# <a id=section30302></a>
# ### 3.3.2 Grouped Boxplot
# 
# 
# - A **Box and Whisker Plot (or Box Plot)** is a convenient way of visually displaying the data distribution through their **quartiles**.
#   
#   - The term “box plot” comes from the fact that the graph **looks like a rectangle with lines extending from the top and bottom**. 
# 
# 
# - The **lines extending parallel** from the boxes are known as the **“whiskers”**, which are used to **indicate variability outside the upper and lower quartiles**. 
#   
#   - **Outliers** are sometimes **plotted as individual dots** that are in-line with whiskers. 
#   
#   - Box Plots can be **drawn either vertically or horizontally**.
#   
#   - Because of the extending lines, this type of graph is sometimes called a **box-and-whisker** plot.
#   
# 
# - They have the **advantage** of taking up **less space**, which is useful when comparing distributions between many groups or datasets.

# In[25]:


# Using seaborn's boxplot to plot a grouped boxplot of the Revenue and State columns.

plt.figure(figsize=(12,7))
sns.boxplot(data=df_store, x='State', y='Revenue', palette='rainbow')

plt.title('Revenue vs State')


# - Here are the types of **observations** we can make from viewing a **Box Plot**:
# 
#   - What the key values are, such as: the **median, 25th percentile, 75th percentile** etc.
# 
#   - If there are any **outliers** and what their values are.
# 
#   - Is the **data symmetrical**.
# 
#   - How **tightly** is the **data grouped**.
# 
#   - If the **data is skewed** and if so, in what **direction**.
#   
#   
# - In the above boxplot, the following observations, can be made:
# 
#   - **Revenue** in **TN (Tamil Nadu)** is usually **higher** than the rest of the states.
#   
#   - Each **State** has **skewed** data as the **median** line is not in the middle of the **whiskers** for each state.
#   
#   - The **outliers are plotted as points**. 
#   
#   - Since there's only **one sample (row)** with **State MH**, so the boxplot shows just a single line for all the values. 

# #### Summarization
# 
# - It is difficult to __squeeze enough dimensions onto a plot without hurting its interpretability__. Very busy plots are naturally very hard to interpret. Hence highly multivariate can be difficult to use.
# 
# - Another way to plot many features while circumnavigating this problem is to use __summarization__. 
# 
#   - Summarization is the __creation__ and __addition__ of new variables by __mixing and matching__ the information provided in the old ones.
#   
#   - Summarization is a useful technique in data visualization because it allows us to __boil down__ potentially very complicated relationships into simpler ones.

# <a id=section30303></a>
# ### 3.3.3 Heat Map
# 
# 
# - Heatmaps **visualise data** through **variations in colouring**. 
# 
#   - When applied to a tabular format, Heatmaps are useful for **cross-examining multivariate data**, through placing variables in the rows and columns and colouring the cells within the table. 
#   
#   - Heatmaps are good for showing **variance across multiple variables**, revealing any patterns, displaying whether any variables are similar to each other, and for detecting if any **correlations exist in-between** them.
# 
# 
# - Typically, all the rows are one category (labels displayed on the left or right side) and all the columns are another category (labels displayed on the top or bottom). 
#   
#   - The individual rows and columns are divided into the subcategories, which all match up with each other in a matrix. 
#   
#   - The cells contained within the table either contain **colour-coded categorical data or numerical data**, that is based on a colour scale. 
#   
#   - The **data** contained within a cell is **based on the relationship between the two variables** in the **connecting row and column**.
# 
# 
# - A **legend** is required **alongside a Heatmap** in order for it __to__ be successfully **read**. 
# 
#   - **Categorical data** is **colour-coded**, while **numerical data requires a colour scale** that blends from one colour to another, in order to represent the difference in high and low values. 
#   
#   - A selection of **solid colours** can be used **to represent multiple value ranges** (0-10, 11-20, 21-30, etc) or you can use a **gradient scale for a single range** (for example 0 - 100) by blending two or more colours together.

# In[26]:


# Creating a correlation matrix using the corr function of the dataframe.
# Using seaborn's heatmap function to plot a heatmap of the correlatin matrix.

corr_mat = df_mcd.corr()
plt.figure(figsize=(10,8))
sns.heatmap(corr_mat, annot=True, cmap='viridis')


# - The **diagonal** of above matrix shows the **auto-correlation** of variable. It is always equal to 1. 
# 
# 
# - **Correlations** can vary from **-1 to +1**. Closer to **+1 means strong positive correlation** and close **-1 means strong negative correlation**. Closer to **0 means not very strongly correlated**. Variables with strong correlations are mostly probable candidates for model builing.
# 
# 
# - Because of their **reliance on colour to communicate values**, Heatmaps are a chart better **suited to displaying a more generalised view of numerical data**, as it’s **harder to** accurately **tell the differences between colour shades** and **to extract specific data points** from (unless of course, you include the raw data in the cells).

# <a id=section30304></a>
# ### 3.3.4 Parallel Coordinates
# 
# 
# - This type of visualisation is **used for plotting multivariate, numerical data**. 
# 
# 
# - **Parallel Coordinates Plots** are ideal for **comparing many variables together** and **seeing the relationships between them**.
# 
# 
# - In a **Parallel Coordinates Plot**, **each variable** is **given its own axis** and **all the axes are placed in parallel to each other**. 
# 
#   - **Each axis can have a different scale**, as each variable works off a different unit of measurement, or all the axes can be normalised to keep all the scales uniform. 
#   
#   - **Values are plotted as a series of lines** that connected across all the axes. This means that each line is a collection of points placed on each axis, that have all been connected together.

# In[27]:


# Creating a copy of df_mcd to use in plotting the Parallel Coordinates.

df_pc = df_mcd.copy()
df_pc.head()


# In[28]:


# Normalizing the columns of df_pc dataframe.
# x_norm = (x - x_min) / (x_max - x_min)

for colname in df_pc.columns:
    if colname not in ['Category', 'Item', 'Sodium', 'High_Or_Low_Sugar']:
        df_pc[colname] = (df_pc[colname] - df_pc[colname].min()) / (df_pc[colname].max() - df_pc[colname].min())


# In[29]:


df_pc.head()


# In[30]:


# Using pandas parallel_coordinates to plot the Parallel Coordinates betwen 'Serve_Size', 'Energy', 'Cholestrol', 
# 'Carbohydrates' columns on the basis of Category_colab column.

plt.figure(figsize=(16,9))
parallel_coordinates(df_pc, 
                     class_column='High_Or_Low_Sugar', colormap='viridis',  
                     cols=['Energy', 'Protein', 'Total_Fat', 'Carbohydrates'])


# - Here we are plotting the **Parallel Coordinates** between **Energy, Protein, Total_Fat**, and **Carbohydrates** columns on the basis of **High_Or_Low_Sugar** column.
# 
# 
# - We can see the variation in values of different columns of **df_pc** dataframe.

# <a id=section30305></a>
# ### 3.3.5 Violin Plot
# 
# 
# - A **Violin Plot** is used to **visualise** the **distribution** of the **data** and its **probability density**.
# 
# 
# - This chart is a **combination** of a **Box Plot** and a **Density Plot that is rotated and placed on each side**, to **show** the **distribution shape of the data**. 
# 
# 
# - The **white dot** in the **middle** is the **median value** and the **thick black bar** in the **centre represents** the **interquartile range**. 
# 
# 
# - The **thin black line extended** from it **represents** the **upper (max)** and **lower (min) adjacent values** in the **data**. Sometimes the graph marker is clipped from the end of this line.
# 
# 
# - **Box Plots** are **limited** in their **display** of the **data**, as their visual simplicity tends to hide significant details about how values in the data are distributed. For example, with Box Plots, you can't see if the distribution is bimodal or multimodal. While **Violin Plots display more information**, they can be noisier than a Box Plot

# In[31]:


# Using seaborn's violinplot function to draw a violin plot between High_Or_Low_Sugar and Serve_Size columns.

plt.figure(figsize=(15,8))
sns.violinplot(data=df_mcd, x='High_Or_Low_Sugar', y='Energy', palette='magma')

plt.title('Violen plot showing the variation of Energy on the basis of High_Or_Low_Sugar')


# - From the above **violin plot** we can clearly see the distribution on the basis of **High_Or_Low_Sugar** and **Energy**.
# 
# 
# - The items having **high sugar** content have **lower energy** when compared to items having **low sugar** content.

# <a id=section4></a>
# ## 4. Interactive Charts using Bokeh
# 
# 
# - Bokeh is an __interactive visualization library__ that targets modern __web browsers__ for presentation.
# 
# 
# - Its goal is to provide __elegant, concise construction of versatile graphics__, and to extend this capability with high-performance interactivity over very large or streaming datasets.
# 
# 
# - Bokeh can help anyone who would like to quickly and easily create __interactive plots, dashboards, and data applications.__
# 
# 
# - To know more about Bokeh, click on this **[link](https://bokeh.pydata.org/en/latest/docs/gallery.html)**.

# In[32]:


# Making bokeh specific imports.

from bokeh.plotting import Figure, figure, output_file, show, output_notebook
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, CustomJS, Slider, HoverTool
from bokeh.io import push_notebook
output_notebook()


# In[33]:


# Plotting a simple plot using bokeh (here we are plotting 3 points along x and y axis).

plot = figure(plot_width=600, plot_height=400)
plot.circle(x=[1,2,3], y=[4,5,6], size=20,
                  color="#FB8072", fill_alpha=0.2, line_width=2)

show(plot)


# In[34]:


# Adding interactivity to the plot.
# Here we are introducing a Slider which can be used to change the shape of the line.

# Setting values to be plotted. Setting similar values for x and y, this will plot a straight line.

x = [x * 0.005 for x in range(0, 200)]
y = x

source = ColumnDataSource(data=dict(x=x, y=y))

# Plotting the line on the plot.

plot = figure(plot_width=600, plot_height=400)
plot.line('x', 'y', source=source, line_width=2, line_alpha=0.8)

# Creating the callback function responsible for changing the shape of the line.
# In the function we are just changing the value of y by giving some power to x using the Python's Math.pow function.
# The power given to x is equal to the value on the slider.

callback = CustomJS(args=dict(source=source), 
                    code="""
                    var data = source.data; 
                    var f = cb_obj.value 
                    var x = data['x'] 
                    var y = data['y']
                    for (var i = 0; i < x.length; i++) {
                        y[i] = Math.pow(x[i], f)}
                    source.change.emit();"""
                    )

# Creating a Slider object which we will use to provide input to the callback object.
# Using the js_on_change function to add callback to the Slider object. 

slider = Slider(start=0.1, end=4, value=1, step=.1, title='power')
slider.js_on_change('value', callback)

layout = column(slider, plot)

show(layout)


# __Using another dataset__

# In[35]:


footballers = pd.read_csv("https://raw.githubusercontent.com/insaid2018/Term-1/master/Data/Casestudy/CompleteDataset.csv", 
                          index_col=0)

# Preprocessing a few data features

footballers['Unit'] = footballers['Value'].str[-1]
footballers['Value (M)'] = np.where(footballers['Unit'] == '0', 0, footballers['Value'].str[1:-1].replace(r'[a-zA-Z]',''))
footballers['Value (M)'] = footballers['Value (M)'].astype(float)
footballers['Value (M)'] = np.where(footballers['Unit'] == 'M', footballers['Value (M)'], footballers['Value (M)'] / 1000)
footballers = footballers.assign(Value=footballers['Value (M)'], Position=footballers['Preferred Positions'].str.split().str[0])


# In[36]:


footballers.head()


# - In the given football data, we gonna use the __Position feature__ for further intractive data visualization with __bokeh__.
# 
# 
# - Significantly all the feature expains its meaning very neatly But in case you didn't have better understanding, dont't worry we gonna explain this __Position feature__ (which is our current focus point).
# 
# 

# In[37]:


footballers['Position'].value_counts()


# - __CB__ ( Central Back)
# - __ST__ ( Striker)
# - __GK__ ( Goal Keeper)
# - __CM__ ( Central Midfield)
# - __CDM__ ( Central Defence midfield)
# - __RM__ ( Right Midfield)
# - __LM__ ( Left Midfield)
# - __LB__ ( Left Back)
# - __RB__ ( Right Back)
# - __CAM__ ( Central Attaking Midfield)
# - __RW__ ( Right Wing)
# - __LW__ ( Left Wing)
# - __CF__ ( Central Forward)
# - __LWB__ ( Left wing back)
# - __RWB__ ( Right wing back)
# 
# 
# __Let's visualize it though infographics:__
# 
# <img src="https://raw.githubusercontent.com/insaid2018/Term-2/master/images/football.png"/>

# In[38]:


# features to plot 

source = ColumnDataSource(dict(x=footballers[footballers['Position']=='ST'].Strength.tolist(), 
                             y=footballers[footballers['Position']=='ST'].Vision.tolist(), 
                             nationality=footballers[footballers['Position']=='ST'].Nationality.tolist(), 
                             position=footballers[footballers['Position']=='ST'].Position.tolist()))

# define the plot size 

plot = Figure(plot_width=900, plot_height=700, tools=[HoverTool(tooltips='@nationality',show_arrow=False)], 
              x_axis_label='Strength',y_axis_label='Vision')

#unit_list = footballers.Unit.unique().tolist()
# plot 

plot.circle(x='x', y='y', fill_alpha=5, source=source, color='blue', legend='position')
plot.legend.location = 'top_left'


# In[39]:


def update_plot(position):
    positions = ['GK', 'LB', 'CB', 'RB', 'LWB', 'CDM', 'RWB', 'LM', 'CM', 'RM', 'CAM', 'LW', 'RW', 'ST', 'CF']
    new_data = dict(x=footballers[footballers['Position'] == positions[position]].Strength.tolist(), 
                  y=footballers[footballers['Position'] == positions[position]].Vision.tolist(), 
                  nationality=footballers[footballers['Position'] == positions[position]].Nationality.tolist(), 
                  position=footballers[footballers['Position'] == positions[position]].Position.tolist())
    source.data = new_data
    push_notebook()


# In[40]:


# Bring the plot in to action 

from ipywidgets import interact
interact(update_plot, position=(0,14,1))
show(plot, notebook_handle=True)


# - The above graph is basically between two feature __Vision__ and __Strength__ on a scale of 0-100.
# 
# 
# - The __slider at the top-left__ is for different playing positions, and as your move the slider it switches the positions and w.r.t that particular postion __player plot of vision vs strength__ comes to your display.
# 
# 
# - When you __move the curser (hover)__ over any data point it __pops up__ the __nationality of the player__.
# 
# 

# <a id=section5></a>
# ## 5. Plotting Geographical Data using Plotly

# In[41]:


# Making plotly specific imports. These imports are necessary to use plotly offline without signing in to their website.

from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go
import chart_studio.plotly as py
from plotly import tools
init_notebook_mode(connected=True)


# In[42]:


df = pd.read_csv('https://github.com/insaid2018/Term-1/raw/master/Data/Casestudy/adult_census_income.csv')
df.head()


# ### Dataset Description
# 
# - In this dataset we will only focus on the **fnlwgt, education.num, native.country** columns.
# 
# 
# | Column Name                    | Description                                                                                |
# | -------------------------------|:------------------------------------------------------------------------------------------:| 
# | **fnlwgt**                     | The weights are prepared monthly by Population Division at the Census Bureau. People with similar demographic characteristics should have similar weights.                                                              | 
# | **education-num**              | Number of years of Education obtained by the individual.                                   | 
# | **native-country**             | Native Country of the individual from the following list of countries: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.                                                                                                     | 

# In[43]:


# Creating the data object.
# This object is used to specify the data to be plotted and its properties.
# In plotly, the data object must be a list object hence its enclosed in [].
# Here we are plotting the mean final weight value of each country on the map, which is set using the z parameter in data.
# The locations to be plotted are specified using the location parameter in data.

data = [go.Choropleth(colorscale='Viridis', autocolorscale=False, locations=sorted(df['native.country'].unique())[1:], 
                      locationmode='country names', z=df.groupby(['native.country'])['fnlwgt'].mean()[1:], 
                      text='Mean Final Weight', colorbar=go.choropleth.ColorBar(title="Mean Final Weight"), 
                      marker=go.choropleth.Marker(line=go.choropleth.marker.Line(color='rgb(255,255,255)', width=2)))]


# In[44]:


# Creating the layout object.
# This object is used to set the layout of the plot (here we are setting the title of the plot).

layout = go.Layout(title=go.layout.Title(text='Mean of the Final Weight of different Countries'))


# In[45]:


# Creating the fig object from the data and layout objects.

fig = go.Figure(data=data, layout=layout)


# In[46]:


# Plotting the data onto a world map.

iplot(fig, filename='d3-cloropleth-map')


# - We can use the **mouse** to **zoom in and out** of the map, to **pan** through the map.
# 
# 
# - We can also select different options provided on the **top-right** corner of the map like **Download, Pan, Box Select, Lasso Select, Zoom In, Zoom Out, Reset** etc.
# 
# 
# - Also on **hover** the plot shows the **mean** of **fnlwgt** value of the country.
# 
# 
# - Here we have plotted the **mean** value of the **fnlwgt** column after grouping it on the basis of **native.country**.
# 
#   - Countries **Mexico, Nicaragua, Peru** have the **highest** values of the **mean** of **final weight**.

# In[47]:


# Creating the data object.
# Here we are plotting the mean education.num value of each country on the map, set by z parameter in data.

data = [go.Choropleth(colorscale='Jet', autocolorscale=False, locations=sorted(df['native.country'].unique())[1:], 
                      locationmode='country names', z=df.groupby(['native.country'])['education.num'].mean()[1:], 
                      text='Mean Years of Education', colorbar=go.choropleth.ColorBar(title="Mean Years of Education"), 
                      marker=go.choropleth.Marker(line=go.choropleth.marker.Line(color='rgb(255,255,255)', width=2)))]


# In[48]:


# Creating the layout object.
# Setting the title of the plot in the layout object.

layout = go.Layout(title=go.layout.Title(text='Mean of the Years of Education of different Countries'))


# In[49]:


# Creating the fig object from the data and layout objects.

fig = go.Figure(data=data, layout=layout)


# In[50]:


# Plotting the data onto a world map.

iplot(fig, filename='d3-cloropleth-map')


# - Here we have plotted the **mean** value of the **education.num** column after grouping it on the basis of **native.country**.
# 
# 
# - We can see that the **mean education.num** value is **highest** in countries **Taiwan, India, Iran and France** (its greater than 12 in these countries), implying that the people from these countries obtain **much higher education** as compared to other countries.
# 
# 
# - Also countries like **Mexico, Guatemala, El-Salvador, Portugal and Dominican Republic** have very **low** values (its less than or equal to 7 in these countries), which implies that people from these countries don't get much **higher education**.
