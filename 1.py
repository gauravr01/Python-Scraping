import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv


url = 'https://en.wikipedia.org/wiki/Cricket'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.title) #For Printing the title of Web Page

blog_titles = soup.find_all('th', class_='infobox-label')
a=[]
for title in blog_titles:
    #print(title.text)
    
    a.append(title.text)
#print(a)
b=[]
plog_titles = soup.find_all('td', class_='infobox-data')
for title in plog_titles:
    # print(title.text)
    
    b.append(title.text)
#print(b)

res_dct = dict(zip(a, b))
print(res_dct)

# Create a DataFrame from the dictionary
data = pd.DataFrame([res_dct])

# Transpose the DataFrame if you want the data in row-wise format
data = data.transpose().reset_index()
data.columns = ['Key', 'Value']

print(data)
data.to_csv('data.csv', index=False)  # Specify the filename and don't write the index

# # Define the CSV file name
# csv_file = "data.csv"

# # Open the CSV file in write mode and create a DictWriter object
# with open(csv_file, mode='w', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=res_dct.keys())
    
#     # Write the dictionary data as a single row to the CSV file
#     writer.writerow(res_dct)

# print(f"Data has been written to {csv_file}")
