import pandas as pd

df = pd.read_excel('em_save_TRAIN.xlsx')

# Transform gender
df['isMale'] = (df['Gender'] == 'Male')
df['isFemale'] = (df['Gender'] == 'Female')

df['isMale'] = df['isMale'].astype('int8')
df['isFemale'] = df['isFemale'].astype('int8')

# transform provider
for provider in ['Provider A', 'Provider B', 'Provider C', 'Provider D']:
    last = provider.split(' ')[-1]
    df[f'InsuranceProviderIs{last}'] = (df['IMP_Insurance_Provider'] == provider)
    df[f'InsuranceProviderIs{last}'] = df[f'InsuranceProviderIs{last}'].astype('int8')

# transform profession
workers = ['Businessperson', 'Lawyer', 'Teacher', 'Scientist', 'Engineer', 'Nurse', 'Artist', 'Doctor']
retired = ['Retired']
student = ['Student']

df['isWorker'] = df['Profession'].isin(workers).astype('int8')
df['isStudent'] = df['Profession'].isin(student).astype('int8')
df['isRetired'] = df['Profession'].isin(retired).astype('int8')

# transform marital status
k = df['Marital_Status'].unique().tolist()

for l in k:
    df[f'is{l}'] = (df['Marital_Status'] == l).astype('int8')
    
# transform family history
k = df[~df['Family_History'].isna()].loc[:, 'Family_History'].unique().tolist()

for l in k:
    df[f'FamilyHad{l.replace(' ', '')}'] = (df['Family_History'] == l).astype('int8')

# save output
new = df.drop(columns=['Gender', 'Profession', 'Family_History', 'Marital_Status', 'IMP_Insurance_Provider', '_WARN_'])
new.to_excel('transformed.xlsx')