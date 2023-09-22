##iframe availability

import csv #Library to handle csv files(read/write)
import requests #library used to handle HTTP GET requests to fetch web pages
import matplotlib.pyplot as plt #library used to plot graphs for EDA

def iframe_availability(htmlcontent): #define function to check iframe availability
    return "<iframe" in htmlcontent.lower() #convert html content to lowercase and search for <iframe element

def get_htmlcontent(url): #define function to fetch html content
    try:
        response = requests.get(url) # make a HTTP get request to URL
        response.raise_for_status() #check the status of the request
        return response.text #if success return the html content
    except requests.RequestException:
        return None

input_csv = r'D:\phishing\phishing\accessible_urls.csv'
availability_status = []

with open(input_csv, 'r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader) 

    for row in csvreader:
        url = row[0] 
        
        htmlcontent = get_htmlcontent(url)
        
        if htmlcontent is not None:
            has_iframe = iframe_availability(htmlcontent)
            availability_status.append([url, 'Iframe available' if has_iframe else 'No Iframe found'])
#Calculations
total_with_iframe = sum(1 for entry in availability_status if entry[1] == 'Iframe available')
total_without_iframe = len(availability_status) - total_with_iframe
with_iframe_percentage = (total_with_iframe/len(availability_status))*100
without_iframe_percentage = (total_without_iframe/len(availability_status))*100
labels = ['Iframe available', 'No Iframe found']
values = [with_iframe_percentage, without_iframe_percentage]
#Plot the graph based on the values obtain
plt.bar(labels, values)
plt.ylabel('Percentage of URLs')
plt.title('Availability of Iframes in URLs for phishing sites')
for label, percentage in zip(labels, values):#combine two varibles and use using zip()
    plt.text(label, percentage, f"{percentage:.2f}%", ha='center', va='bottom')
plt.show()
