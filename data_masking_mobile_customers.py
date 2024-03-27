import pandas as pd
import numpy as np
import faker 

# Load the .xlsx file
df = pd.read_excel('/Users/yashwanthreddymaddi/Data_Cleaning/mobile_customers.xlsx')

#Faker istance
fake = faker.Faker()

#Remove unnecessary columns
df.drop(['customer_id','current_location'], axis = 1, inplace = True)

#Mask username
df['username'] = df['username'].apply(lambda x: fake.user_name())

#Replace orginal name with fake names
df['name'] = df['name'].apply(lambda x: fake.name())

#Mask email addresses
df['username'] = df['username'].apply(lambda x: fake.user_name())

#Add noise to date_registered and birthday columns
df['date_registered'] = df['date_registered'] + pd.to_timedelta(np.random.randint(-365,365,size=len(df)), unit='D')
df['birthdate'] = df['birthdate'] + pd.to_timedelta(np.random.randint(-365*50,365*50,size=len(df)), unit='D')

#Categorize salary and age column into bins
df['salary'] = pd.cut(df['salary'], bins=5, labels=['Low', 'Medium-Low','Medium','Medium-High','High'])
df['age'] = pd.cut(df['age'], bins=5, labels=['Young', 'Young Adult', 'Adult','Middle-aged','Elderly'])

#Tokenize credit_card_provider and credit_card_expire_date
df['credit_card_provider'] = df['credit_card_provider'].apply(lambda x: fake.credit_card_provider())
df['credit_card_expire'] = df['credit_card_expire'].apply(lambda x : fake.future_date(end_date='+10y'))

#Mask credit_card_number and credit_card_security_code
df['credit_card_number'] = df['credit_card_number'].apply(lambda x : fake.credit_card_number())
df['credit_card_security_code'] = df['credit_card_security_code'].apply(lambda x : fake.credit_card_security_code())

