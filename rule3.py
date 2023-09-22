##Check for suspicious characters in URL hostname
import csv #Library to handle csv files(read/write)
import matplotlib.pyplot as plt #library used to plot graphs for EDA

suspicious_characters = ["-", "#", "_", "@"]  #define the suspicious characters list

def check_suspicious_characters(hostname): #define the function to check suspicious chars availability
    return any(char in hostname for char in suspicious_characters) #iterate through hostname chars to match any char in defined list

input_csv = r'D:\phishing\phishing\accessible_urls.csv'
urls_with_sus_chars = [] #empty list
urls_without_sus_chars = [] #empty list

with open(input_csv, 'r', newline='', encoding='utf-8') as csvfile: #open csv in read mode
    csvreader = csv.reader(csvfile) 
    next(csvreader) #exclude header row

    for row in csvreader: #iterate through rows
        url = row[0] #select each row with first column
        hostname = url.split('//', 1)[-1].split('/', 1)[0] #split url and extract hostname
        if check_suspicious_characters(hostname): #call the function using hostname as input
            urls_with_sus_chars.append(url) #if return true add the url to urls_with_sus_chars list
        else:
            urls_without_sus_chars.append(url) #if return false add the url to urls_without_sus_chars list
#calculations
total_with_suspicious_chars = len(urls_with_sus_chars)
total_without_suspicious_chars = len(urls_without_sus_chars)
total_urls = total_with_suspicious_chars + total_without_suspicious_chars

percentage_with_suspicious_chars = (total_with_suspicious_chars / total_urls) * 100
percentage_without_suspicious_chars = (total_without_suspicious_chars / total_urls) * 100

print('Percentage with suspicious characters:', percentage_with_suspicious_chars)
print('Percentage without suspicious characters:', percentage_without_suspicious_chars)

labels = ['With Suspicious Chars', 'Without Suspicious Chars']
percentages = [percentage_with_suspicious_chars, percentage_without_suspicious_chars]
#Plot the graph based on the values obtain
plt.bar(labels, percentages)
plt.ylabel('Percentage of URLs')
plt.title('Presence of Suspicious Characters in Hostname (legitimate)')
for label, percentage in zip(labels, percentages): #combine two varibles and use using zip()
    plt.text(label, percentage, f"{percentage:.2f}%", ha='center', va='bottom')
plt.show()