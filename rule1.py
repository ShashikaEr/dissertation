#Check cookieconsent ignore

import csv #Library to handle csv files(read/write)
import requests #library used to handle HTTP GET requests to fetch web pages
from bs4 import BeautifulSoup #Library used to extract relevant features
import matplotlib.pyplot as plt #library used to plot graphs for EDA

def check_cookie_consent_ignore_tag(htmlcontent): #define the function to check the cookie consent ignore tag availability
    soup = BeautifulSoup(htmlcontent, 'html.parser') #parse HTML content using BeautifuleSoup
    return bool(soup.find('script', attrs={'data-cookieconsent': 'ignore'}))#return true if script tag with mentioned attribute available

def fetch_htmlcontent(url): #define the function to fetch html content
    try:
        response = requests.get(url) # make a HTTP get request to URL
        response.raise_for_status() #check the status of the request
        return response.text #if success return the html content
    except requests.RequestException:
        return None
#read_csv = r'D:\phishing\legitimate\legitimate_urls.csv' #csv location to legitimate URLs
read_csv = r'D:\phishing\phishing\accessible_urls.csv' #csv location to phishing URLs
ignore_urls = []  

with open(read_csv, 'r', newline='', encoding='utf-8') as csvfile: #open the csv file in read mode and iterate through its rows
    csvreader = csv.reader(csvfile)
    next(csvreader)  #ignore the header row

    for row in csvreader:
        url = row[0]
        htmlcontent = fetch_htmlcontent(url) #fetch the html content

        if htmlcontent:
            ignore_tag_available = check_cookie_consent_ignore_tag(htmlcontent)
            label = '1' if ignore_tag_available else '0' #assign 1 if tag available, assign 0 if tag is not available
            ignore_urls.append([url, label]) #append the url to ignore urls list with labels

total_with_ignore_tag = sum(1 for url_info in ignore_urls if url_info[1] == '1') #get the count of the urls with label as 1
total_without_ignore_tag = len(ignore_urls) - total_with_ignore_tag
with_ignore_percentage = (total_with_ignore_tag/len(ignore_urls))*100 #calculate percentage
without_ignore_percentage = (total_without_ignore_tag/len(ignore_urls))*100 #calculate percentage
print(total_with_ignore_tag)
print(total_without_ignore_tag)
labels = ['With Ignore Tag', 'Without Ignore Tag']
values2 = [with_ignore_percentage, without_ignore_percentage]

#Plot the graph based on the values obtain
plt.bar(labels, values2)
plt.ylabel('Percentage of URLs')
plt.title('Presence of <script data-cookieconsent="ignore"> Tag in Phishing sites')
for label, percentage in zip(labels, values2): #combine two varibles and use using zip()
    plt.text(label, percentage, f"{percentage:.2f}%", ha='center', va='bottom')
plt.show()