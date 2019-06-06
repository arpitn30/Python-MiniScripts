from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
import glob
ext = '.mp4'    # File Extension

def main():
    url = input('Enter the wiki url for the season: ')
    dir = input('Enter the path to the directory: ')
    tr = get_table(url)

    # Change the root directory of the program to that of the given directory
    os.chdir(dir)
    # Make a list of all the files with .mp4 file extension
    files = glob.glob('*'+ext)
    i = 0
    for file in files:
        # Find Table Heading and get the episode number
        th = tr[i].find('th')

        # Get episode no from the first column
        epno = th.get_text()
        # If episodes in th don't start from 1, get epno from the next column
        if(int(epno) > i + 1):
            th = tr[i].find('td')
            epno = th.get_text()
        
        # Find the table row and get the episode name
        td = tr[i].find('td', 'summary')
        epname = td.get_text()
        # Concatenate and pretty print the name
        name = get_name(epno, epname)
        # Rename the files in the directory
        os.rename(file, name)
        print("Episode " + str(i + 1) + " renamed")
        i += 1
    print('\nAll Files Renamed')


def get_table(url):
    """Find and make a list of the all the episode data"""
    soup = BeautifulSoup(urlopen(url), 'html.parser')
    table = soup.find('table', 'wikitable')
    tr = table.find_all('tr', 'vevent')
    return tr

def get_name(epno, epname):
        """Concatenate episode no and name and pretty print it"""
        if(int(epno) < 10):
            epno = "0" + epno
        # Only take the name between " " and convert it back into string
        epname = str((epname.split('\"'))[1])
        return epno + ' - ' + epname + ext

if __name__ == '__main__':
    main()
