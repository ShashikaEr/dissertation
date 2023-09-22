##Host part length 

import csv #Library to handle csv files(read/write)
import matplotlib.pyplot as plt #library used to plot graphs for EDA
from urllib.parse import urlparse #urlparse function for parse URLs and for break into individual components

def host_len(url): 
    parsed_url = urlparse(url)
    return len(parsed_url.netloc)

def get_host_len(input_csv, column_index):
    length_of_host = [] #empty list to store host length
    with open(input_csv, 'r', newline='', encoding='utf-8') as csvfile: #open csv with read mode
        csvreader = csv.reader(csvfile) #csv reader object
        next(csvreader)  #skip header row

        for row in csvreader:  #iterate through rows
            url = row[column_index] #select the url from row and the 'column_index' column
            length = host_len(url) #call for the function host_len
            length_of_host.append(length) #append the host length to length_of_host
    return length_of_host

input_csv = r'D:\phishing\phishing\accessible_urls.csv'  #csv location
column_index = 0  #initialized the column index
length_of_host = get_host_len(input_csv, column_index) #call for the function get_host_len
#Plot the graph based on the values obtain
def host_len_histo(length_of_host): #define function to generate histogram
    plt.hist(length_of_host, bins=20, edgecolor='black', alpha=0.7)
    plt.xlabel('Host Length')
    plt.ylabel('Number of URLs')
    plt.title('Distribution of Host Lengths')
    plt.show()
host_len_histo(length_of_host) #call for the function host_len_histo