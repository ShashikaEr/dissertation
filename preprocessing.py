import csv #library used to read/write csv files
import requests #library used to use to send HTTP HEAD requests to URLs
def check_url(url): #function to check URL status
    try:
        response = requests.head(url, timeout=20) #sending HTTP HEAD request with a 20s timeout
        return response.status_code #if success ststus code will 200
    except requests.RequestException:
        return "Error" #if not success Error
if __name__ == "__main__":
    #change the location to read and write legitimate URLs.
    read_csv = r"D:\phishing\phishing\online_phishing_sites.csv" #read csv file from this location for phishing URLs
    saved_csv = r"D:\phishing\phishing\accessible_urls.csv"      #save csv file to this location for phishing URLs
    urls_accessible = set() #Used to save unique accessible URLs without duplicates
    with open(read_csv, "r", newline="") as csvfile:  #open csv with read mode
        csvreader = csv.reader(csvfile) 
        next(csvreader) #skip the header row
        for row in csvreader:   
            url = row[1] #select the url from row and the second column
            status_code = check_url(url) #check the url status
            
            if status_code == 200: 
                urls_accessible.add(url) # add urls which has status code of 200 to url_accessible
            if len(urls_accessible) >= 500: #after reach 500 urls break the loop
                    break
    with open(saved_csv, "w", newline="") as csvfile: #open csv with write mode
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["URL", "Status Code"])   #header row
        for url_info in urls_accessible:
            csvwriter.writerow([url_info, status_code])  #save the urls_accessible data to saved_csv file

    print(f"URLs saved in {saved_csv}")