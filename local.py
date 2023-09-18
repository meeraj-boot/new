#!/usr/bin/env python
# coding: utf-8

# In[10]:


import streamlit as st




# In[11]:


# Reverse mapping dictionaries for categorical columns
country_reverse_mapping = {
    0: 'Turkey',
    1: 'Kenya',
    2: 'Peru',
    3: 'Japan',
    4: 'France',
    5: 'USA',
    6: 'Brazil',
    7: 'Spain',
    8: 'South Africa',
    9: 'Thailand',
    10: 'Mexico',
    11: 'Egypt',
    12: 'Germany',
    13: 'Australia',
    14: 'India',
    15: 'UK',
    16: 'Indonesia',
    17: 'Argentina',
    18: 'South Korea',
    19: 'Russia',
    20: 'Canada',
    21: 'Italy',
    22: 'UAE',
    23: 'Greece',
    24: 'China'
}


# In[12]:


attack_type_reverse_mapping = {
    0: 'Shooting',
    1: 'Bombing',
    2: 'Hijacking',
    3: 'Arson',
    4: 'Stabbing',
    5: 'Kidnapping',
    6: 'Assassination',
    7: 'Other'
}

perpetrator_reverse_mapping = {
    0: 'Group C',
    1: 'Group A',
    2: 'Group D',
    3: 'Group B'
}

target_type_reverse_mapping = {
    0: 'civilians',
    1: 'tourists',
    2: 'government officials',
    3: 'infrastructure',
    4: 'police'
}

weapon_used_reverse_mapping = {
    0: 'Blade Weapons',
    1: 'chemical',
    2: 'explosives',
    3: 'firearms',
    4: 'incendiary',
    5: 'melee',
    6: 'unknown'
}


# In[13]:


# Function to map encoded values back to original values
def map_encoded_to_original(encoded_value, reverse_mapping):
    return reverse_mapping.get(encoded_value, 'Unknown')

# Function to get user input features
def user_input_features():
    st.sidebar.subheader('Enter Attack Details:')
    
    # Selectboxes for categorical features (use reverse mapping)
    country = st.sidebar.selectbox('Country', list(country_reverse_mapping.values()))
    attack_type = st.sidebar.selectbox('Attack Type', list(attack_type_reverse_mapping.values()))
    perpetrator = st.sidebar.selectbox('Perpetrator Group', list(perpetrator_reverse_mapping.values()))
    target_type = st.sidebar.selectbox('Target Type', list(target_type_reverse_mapping.values()))
    weapon_used = st.sidebar.selectbox('Weapon Used', list(weapon_used_reverse_mapping.values()))
    
    # Number inputs for numeric features
    victims_injured = st.sidebar.number_input('Victims Injured', min_value=0.0, step=1.0)
    victims_deceased = st.sidebar.number_input('Victims Deceased', min_value=0.0, step=1.0)
    
    # Create a dictionary of user inputs with original numeric values
    data = {
        'country': country_reverse_mapping.get(country),
        'Attack_Type': attack_type_reverse_mapping.get(attack_type),
        'Perpetrator': perpetrator_reverse_mapping.get(perpetrator),
        'Victims_Injured': victims_injured,
        'Victims_Deceased': victims_deceased,
        'Target_Type': target_type_reverse_mapping.get(target_type),
        'Weapon_Used': weapon_used_reverse_mapping.get(weapon_used)
    }
    
    # Create a DataFrame from the user input
    features = pd.DataFrame(data, index=[0])
    return features


# In[14]:


# Streamlit UI
st.title('Terrorism Incident Classification (Random Forest)')
st.sidebar.header('User Input Parameters')


# In[15]:


# Get user input features
df = user_input_features()
st.subheader('User Input Parameters')
st.write(df)


# In[16]:


# Load your Random Forest model from the .pkl file
model = joblib.load('terror02.pkl')


# In[20]:


# Make predictions on the user input data
prediction = model.predict(df)


# In[18]:


st.subheader('Predicted Result')
if prediction[0] == 1:
    st.write('Major Incident')
else:
    st.write('Minor Incident')


# In[ ]:




