# Data_Cleaning
With a data set named “mobile_customers.csv.” This contains information about customers that have signed up for the mobile app in the last three years.  We need you to anonymise this data to hide personal details while preserving any useful information for the data scientists at a company.


**Data Cleaning Script**
This script demonstrates how to clean and manipulate data in a pandas DataFrame using Faker library to generate fake data. It performs various data cleaning tasks such as removing unnecessary columns, masking sensitive information, adding noise to date columns, categorizing numerical columns into bins, and tokenizing categorical columns.

Usage
Installation:

Ensure you have Python installed on your system.
Install the required libraries using pip:
Copy code
pip install pandas numpy Faker
Running the Script:

Download the script file data_cleaning_script.py.
Replace the file path in the pd.read_excel() and df.to_csv() functions with the path to your Excel file and desired CSV output file.
Open a terminal or command prompt.
Navigate to the directory containing the script file.
Run the script:
Copy code
python data_cleaning_script.py
Output:

The script will read the data from the Excel file, perform data cleaning and manipulation tasks, and save the manipulated data to a CSV file specified in the script.
Dependencies
pandas: Python library for data manipulation and analysis.
numpy: Python library for numerical computing.
Faker: Python library for generating fake data.
