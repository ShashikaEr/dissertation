##Number of sub domains

import csv #Library to handle csv files(read/write)
import matplotlib.pyplot as plt #library used to plot graphs for EDA
from urllib.parse import urlparse #urlparse function for parse URLs and for break into individual components
def no_of_subdomains(url): #define function to get no of subdomains
    parsed_url = urlparse(url) #parse the URL into its components
    subdomains = parsed_url.netloc.split('.') #split into parts seperate by '.'
    return len(subdomains) - 2 #return calculated number of elements in subdomains and remove TLD and domain
def get_url_no_of_subdomains(input_csv, column_index): #define function to get no_of_subdomains
    subdomain_counts = [] #empty list to save subdomain count
    with open(input_csv, 'r', newline='', encoding='utf-8') as csvfile: #open csv with read mode
        csvreader = csv.reader(csvfile) #csv reader object
        next(csvreader) #exclude header row
        for row in csvreader: #iterate through rows
            url = row[column_index] #select the url from row and the 'column_index' column
            subdomain_count = no_of_subdomains(url) #call for the function
            subdomain_counts.append(subdomain_count) #append subdomain count to subdomain_counts list
    return subdomain_counts

input_csv = r'D:\phishing\phishing\accessible_urls.csv'  #csv location
column_index = 0 #initialized the column index
subdomain_counts = get_url_no_of_subdomains(input_csv, column_index)
#Plot the graph based on the values obtain
def subdomain_count_histo(subdomain_counts): #define function to plot histogram
    plt.hist(subdomain_counts, bins=range(max(subdomain_counts)+2), edgecolor='black', alpha=0.7)
    plt.xlabel('Number of Subdomains')
    plt.ylabel('Number of URLs')
    plt.title('Distribution of Number of Subdomains')
    plt.xticks(range(max(subdomain_counts)+1))
    plt.show()
subdomain_count_histo(subdomain_counts) #call subdomain_count_histo function