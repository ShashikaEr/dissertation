#Check the @ and // availability in the url
import csv #Library to handle csv files(read/write)
import matplotlib.pyplot as plt #library used to plot graphs for EDA

def check_special_chars(url): #define the function to check the availability of redirection chars
    protocol = url.find("://")  #find :// from the begining
    if protocol != -1: #if :// found
        skip_protocol = url[protocol + 3:] #eliminate :// and take the remaining after ://
        return "@" in skip_protocol or "//" in skip_protocol #looking for @ or // in skip_protocol
    return False 

input_csv = r'D:\phishing\phishing\accessible_urls.csv'
availability_data = [] #empty list to store url and availability status

with open(input_csv, 'r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

    for row in csvreader:
        url = row[0]
        has_special_chars = check_special_chars(url)
        availability_data.append([url, 'With Special Chars' if has_special_chars else 'Without Special Chars'])

#calculations
total_with_special_chars = sum(1 for entry in availability_data if entry[1] == 'With Special Chars') 
total_without_special_chars = len(availability_data) - total_with_special_chars
total_with_special_chars_percentage = (total_with_special_chars/len(availability_data))*100
total_without_special_chars_percentage = (total_without_special_chars/len(availability_data))*100
print(total_with_special_chars_percentage)
print(total_without_special_chars_percentage)
labels = ['With Special Chars', 'Without Special Chars']
values = [total_with_special_chars_percentage, total_without_special_chars_percentage]
#Plot the graph based on the values obtain
plt.bar(labels, values)
plt.ylabel('Percentage of URLs')
plt.title('Presence of Special Characters in URLs After Protocol (Redirect) for phishing sites')
for label, percentage in zip(labels, values):  #combine two varibles and use using zip()
    plt.text(label, percentage, f"{percentage:.2f}%", ha='center', va='bottom')
plt.show()