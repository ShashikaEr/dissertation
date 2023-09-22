##Display cookie preferences/settings for user by banner, popup
import csv #Library to handle csv files(read/write)
import requests #library used to handle HTTP GET requests to fetch web pages
from bs4 import BeautifulSoup #Library used to extract relevant features
import matplotlib.pyplot as plt #library used to plot graphs for EDA

def check_cookie_banner(htmlcontent): #define the function to check the cookie preference banner
    soup = BeautifulSoup(htmlcontent, 'html.parser') #parse HTML content using BeautifuleSoup
    popup_elements = soup.find_all(lambda tag: #search for the tags, lambda function takes tag as argument
        ('id' in tag.attrs and 'cookie' in tag['id']) or ('cookie' in tag.text) #tag, id can contain cookie or text can contain cookie
    )
    return len(popup_elements) > 0 #if find elememts return true
def fetch_htmlcontent(url): 
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException:
        return None
#input_csv = r'D:\phishing\legitimate\legitimate_urls.csv'
input_csv = r'D:\phishing\phishing\accessible_urls.csv'

results = []
with open(input_csv, 'r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        url = row[0]
        htmlcontent = fetch_htmlcontent(url)

        if htmlcontent:
            with_popup = check_cookie_banner(htmlcontent)
            results.append([url, with_popup])
total_with_popup = sum(1 for _, with_popup in results if with_popup)
total_without_popup = len(results) - total_with_popup
total_urls = total_with_popup + total_without_popup
percentage_with_popup = (total_with_popup / total_urls) * 100
percentage_without_popup = (total_without_popup / total_urls) * 100

print('Percentage with popup:', percentage_with_popup)
print('Percentage without popup:', percentage_without_popup)

labels = ['With Popup', 'Without Popup']
percentages = [percentage_with_popup, percentage_without_popup]
#Plot the graph based on the values obtain
plt.bar(labels, percentages)
plt.ylabel('Percentage of URLs')
plt.title('Presence of Cookie Popup in Phishing sites')
for label, percentage in zip(labels, percentages): #combine two varibles and use using zip()
    plt.text(label, percentage, f"{percentage:.2f}%", ha='center', va='bottom')
plt.show()
