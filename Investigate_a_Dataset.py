#!/usr/bin/env python
# coding: utf-8

# > **Tip**: Welcome to the Investigate a Dataset project! You will find tips in quoted sections like this to help organize your approach to your investigation. Once you complete this project, remove these **Tip** sections from your report before submission. First things first, you might want to double-click this Markdown cell and change the title so that it reflects your dataset and investigation.
# 
# # Project: Investigate a Dataset - [No-Show appointments]
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# ### Dataset Description 
# 
# This dataset collects information from 100k medical appointments in Brazil and is focused on the question of whether or not patients show up for their appointment. A number of characteristics about the patient are included in each row.
# ● ‘ScheduledDay’ tells us on what day the patient set up their appointment.
# ● ‘Neighborhood’ indicates the location of the hospital.
# ● ‘Scholarship’ indicates whether or not the patient is enrolled in Brasilian welfare program Bolsa Família.
# ● Be careful about the encoding of the last column: it says ‘No’ if the patient showed up to their appointment, and ‘Yes’ if they did not show up.
# 
# 
# ### Question(s) for Analysis
# What factors are important for us to know in order to predict if a patient will show up for their scheduled appointment?
# 

# In[1]:


# Use this cell to set up import statements for all of the packages that you
#   plan to use.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

# Remember to include a 'magic word' so that your visualizations are plotted
#   inline with the notebook. See this page for more:
#   http://ipython.readthedocs.io/en/stable/interactive/magics.html


# In[2]:


# Upgrade pandas to use dataframe.explode() function. 
#!pip install --upgrade pandas==0.25.0


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# 
# 
# 
# ### Summary And General Properties:-
# 

# In[3]:


df = pd.read_csv("Database_No_show_appointments/noshowappointments-kagglev2-may-2016.csv", sep=',')
df.head()


# In[4]:


df.describe()


# The minimum age is -1 which is most likely an error in the entry, as 50% of the ages are betwwen 18 and 55 years.

# In[5]:


df.shape


# In[6]:


df.info()


# we don't have any missing values

# In[7]:


df.duplicated().sum()


# there is no dublicate rows

# In[8]:


df["PatientId"].duplicated().sum()


# there is 48228 duplicated Patient Id and the rest of numbers are unique values

# In[9]:


df.duplicated(['PatientId','No-show']).sum()


# There are 38710 Patient Id have the same status of showing or no.

# 
# ### Data Cleaning
# 
#  

# # rename columns

# In[10]:


df.rename(columns={'No-show':'No_show', 'Handcap':'Handicap', 'Hipertension':'Hypertension'},inplace = True)


# # apply zero for value that has age = -1

# In[11]:


df['Age']=df['Age'].replace([-1],0)


# In[12]:


df.describe()


# In[13]:


df.info()


# # remove dublicated

# In[14]:


df.drop_duplicates(['PatientId', 'No_show'],inplace=True)
df.shape


# # remove columns that i will not use it

# In[15]:


df.drop(['AppointmentID', 'AppointmentDay', 'ScheduledDay'], axis=1, inplace=True)


# In[16]:


df.head()


# In[17]:


df.info()


# # general view

# In[18]:


df.hist(figsize=(15,6.5));


# # make 2 groups to showing and not showing

# In[19]:


show=df.No_show=='No'
noshow=df.No_show=='Yes'
df[show].count(), df[noshow].count()


# number of showed patient is 54154 is greater than non showed 17663

# In[20]:


df[show].mean()


# In[21]:


df[noshow].mean()


# In[22]:


ax=df['Age'].hist(alpha=1,color='yellow')
ax.set_ylabel('No_show_Ratio')
ax.set_xlabel('Age')
ax.set_title('overview')
pd.DataFrame(df['Age'].describe())


# # <a id='eda'></a>
# ## Exploratory Data Analysis

# #  Research Question 1 (does age affect patient attendance?)

# In[23]:


df.Age[show].hist(alpha=.7, label='show',color='red')
df.Age[noshow].hist(alpha=.7, label='noshow',color='green')
plt.xlabel('Age')
plt.ylabel('show')
plt.title('Age patient attendance')
plt.legend();


# we see that age from 0:5 and from 45:55 are the most patient attendance, as opposed to from 60 to higer

# # Research Question 2  (does the type of disease affect the paitent's attendance?)

# In[24]:


df[show].groupby(['Hypertension','Diabetes']).mean()['Age'],df[noshow].groupby(['Hypertension','Diabetes']).mean()['Age']


# In[25]:


df.groupby(['Hypertension'])['No_show'].count().plot(kind='bar').set_ylabel('No_show_Ratio')
df.groupby(['Hypertension'])[['No_show']].count()
plt.title('The effect of Hypertension on the attendance of patients');


# Hypertension diseases don't affect the attendance rate of patients. 

# In[26]:


df.groupby(['Diabetes'])['No_show'].count().plot(kind='bar').set_ylabel('No_show_Ratio')
df.groupby(['Diabetes'])[['No_show']].count()
plt.title('The effect of Diabetes on the attendance of patients');


# Diabetes diseases don't affect the attendance rate of patients. 

# In[27]:


df[show].groupby(['Alcoholism','Handicap']).median()['Age'],df[noshow].groupby(['Alcoholism','Handicap']).median()['Age']


# In[28]:


df.groupby(['Alcoholism'])['No_show'].count().plot(kind='bar').set_ylabel('No_show_Ratio')
df.groupby(['Alcoholism'])[['No_show']].count(),
plt.title('The effect of Alcoholism on the attendance of patients');


# Alcoholism diseases don't affect the attendance rate of patients. 

# In[29]:


df.groupby(['Handicap'])['No_show'].count().plot(kind='bar').set_ylabel('No_show_Ratio')
df.groupby(['Handicap'])[['No_show']].count()
plt.title('The effect of Handicap on the attendance of patients');


# Handicap don't affect the attendance rate of patients. 

# #  Research Question 3  (does the gender affect the paitent's attendance?

# In[30]:


df.groupby(['Gender'])['Age'].median()


# In[31]:


df.groupby(['Gender'])['Age'].mean()


# In[32]:


df.groupby(['Gender'])['Age'].std()


# The Gender don't affect the attendance rate of patients.

# In[33]:


df['PatientId']=df['PatientId'].astype(int)
df.info()


# In[34]:


df.groupby(['Gender'])['PatientId'].count().plot(kind='bar').set_ylabel('count')
df.groupby(['Gender'])[['PatientId']].count()
plt.title('The effect of Gender on the attendance of patients');


# Male attendance rate less than female attendance rate.

# # Research Question 4  (does the SMS_received affect the paitent's attendance?)

# In[35]:


df.SMS_received[show].hist(alpha=.7, label='show',color='grey')
df.SMS_received[noshow].hist(alpha=.7, label='noshow',color='blue')
plt.xlabel('SMS_received')
plt.ylabel('show')
plt.title('SMS_received patient attendance')
plt.legend(); 


# the proportion of patients who didn't receive SMS messages is more in the proportion of thier attendace than those who received messages.

# # Research Question 5  (does the Scholarship affect the paitent's attendance?)

# In[36]:


df.Scholarship[show].hist(alpha=.7, label='show',color='red')
df.Scholarship[noshow].hist(alpha=.7, label='noshow',color='green')
plt.xlabel('Scholarship')
plt.ylabel('show')
plt.title('Scholarship patient attendance')
plt.legend();


# Scholarship not Affect in patient attendance.

# # # Research Question 6  (does the Neighbourhood affect the paitent's attendance?)

# In[37]:


df.Neighbourhood[show].value_counts().plot(alpha=2, label='show',color='red')
df.Neighbourhood[noshow].value_counts().plot(alpha=2, label='show',color='black')
plt.xlabel('Neighbourhood')
plt.ylabel('show')
plt.title('Neighbourhood patient attendance')
plt.legend();


# Place of Neighbourhood Affect in patient attendance.

# # Limitations
# 
# -There was a challenge in the validity of the data, as I found that there is a negative and zero age, so I addressed this matter and also changed the data type of the patients ID to be used in the rates.
# 
# -For the code used, it is useful to break the code into small parts. Lots of useful tips found on the Datatofish website.
# 
# -Another challenge I faced was in the direction of analysis. I wasn't really sure where to go when I started my analysis. In fact, the final step-by-step path was formulated instead of a general plan that I already knew.

# <a id='conclusions'></a>
# ## Conclusions
# *patient data must be updated, especially phone numbers, and we can replaced with a call to ensure that the patient will come on time.
# 
# *Gender, alcohol,  and scholarship are not afactor in whether apatient is present at the appointment.
# 
# *Making an appointment in advance with the patient isn't evidence that he will attend on time.
# 
# *Age and Neighbourhood is the most influence factor in the presence of the patient or not, as the attendance rate rises.
# 
# *The types of diseases does not affect the attendance rate.
# 
# *References to the entered data should be set to avoid problems with the information.
# 
# *It is necessary to focus on the districts where the attendance rate is weak by conducting awareness programs and collecting correct data on patients to facilitate communication with them.
# 
# ## Submitting your Project 
# 
# > **Tip**: Before you submit your project, you need to create a .html or .pdf version of this notebook in the workspace here. To do that, run the code cell below. If it worked correctly, you should get a return code of 0, and you should see the generated .html file in the workspace directory (click on the orange Jupyter icon in the upper left).
# 
# > **Tip**: Alternatively, you can download this report as .html via the **File** > **Download as** submenu, and then manually upload it into the workspace directory by clicking on the orange Jupyter icon in the upper left, then using the Upload button.
# 
# > **Tip**: Once you've done this, you can submit your project by clicking on the "Submit Project" button in the lower right here. This will create and submit a zip file with this .ipynb doc and the .html or .pdf version you created. Congratulations!

# In[38]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])

