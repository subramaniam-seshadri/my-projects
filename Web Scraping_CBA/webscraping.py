import requests
from bs4 import BeautifulSoup
from string import digits
import string as str
import re
import csv

def scrape_data(url, department):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    table = soup.findAll("table", {"class": "table table-condensed table-hover table-bordered"})
    header = soup.find_all('h2')


    header = header[0].text
    header = header.strip().lower()
    #if(department in header):
    list_Email = []
    searchMail = "@csulb.edu"
    for link in table[0].find_all('a'):
        if(searchMail in link.get('href')):
            match = re.search(r'[\w\.-]+@[\w\.-]+', link.get('href'))
            list_Email.append(match.group(0))
    result ={header:list_Email}
    #print(result)
    return result

def main():
    '''
    try:
        department = input("Enter the department you want to search for: ")
    except SyntaxError:
        pass
    '''
    with open("test.csv", "w") as empty_csv:
        # now we have an empty csv file
        pass
    for i in range(1,17):
        url_to_scrape = 'http://web.csulb.edu/colleges/cba/contact/index.php?dept=%d' % (i,)
        try:
            result = scrape_data(url_to_scrape, 0)
            with open('test.csv','a') as f:
                writer = csv.writer(f,dialect='excel')
                key = next(iter(result))
                f.write(key)
                f.write('\n')
                [f.write(x+'\n') for x in result[key]]
                #writer.writerow()
                f.write('\n')
                print("Write Done for :", key)

        except:
            pass
if __name__ == '__main__': main()