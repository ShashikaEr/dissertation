#Number of URL characters group by 20 categories

import csv #Library to handle csv files(read/write)
import matplotlib.pyplot as plt #library used to plot graphs for EDA


def get_url_length(input_csv, column_index): #define function to get url lengths
    url_lengths = [] #empty list to store url length
    with open(input_csv, 'r', newline='', encoding='utf-8') as csvfile: #open csv with read mode
        csvreader = csv.reader(csvfile) #csv reader object
        next(csvreader)  #exclude header row
        for row in csvreader: #iterate through rows
            url = row[column_index] #select the url from row and the 'column_index' column
            url_length = len(url) #calculate the length of the url
            url_lengths.append(url_length) #append the url lenth to url_lengths list
    return url_lengths #return the url_lengths list
input_csv = r'D:\phishing\phishing\accessible_urls.csv' #csv location
column_index = 0 #initialized the column index
url_lengths = get_url_length(input_csv, column_index) #call for the function get_url_length
#Plot the graph based on the values obtain
def url_length_histogram(url_lengths): 
    plt.hist(url_lengths, bins=20, edgecolor='black', alpha=0.7)
    plt.xlabel('URL Length')
    plt.ylabel('Number of URLs')
    plt.title('Distribution of URL Lengths')
    plt.show()
url_length_histogram(url_lengths) #call for the function url_length_histogram