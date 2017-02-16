from bs4 import BeautifulSoup
from urllib.request import urlopen


def main():
    url = input('Enter the URL of the website to search: ')
    word = input('Enter the word(s) to search: ')
    maxPages = int(input('Enter the max no of pages to search: '))

    Links = [url]
    numberVisited, i = 0, 0
    foundWord = []

    # Run loop until the max number of pages are visited or no more links are there to visit
    while numberVisited < maxPages and i < len(Links):
        numberVisited = numberVisited + 1
        # Get the ith url in the Links list
        url = Links[i]
        i = i + 1
        try:
            print(numberVisited, 'Visiting: ', url)
            # Parse the html in the given url
            soup = BeautifulSoup(urlopen(url), 'html.parser')
            # Get the text in head and body
            head = soup.find('head')
            text = head.get_text()
            body = soup.find('body')
            text = text + '\n' + body.get_text()
            # Find the word in the text and if found, store the url
            if (text.find(word) != -1) and (url not in foundWord):
                foundWord.append(url)
            # Add all the urls on the page to the Links list
            Links.extend(page['href'] for page in soup.find_all('a', href=True) if page['href'] not in Links
                                                                                and page['href'].startswith(Links[0]))

            print('**Success!**')
        except:
            print('**Failed!**')

    if foundWord != []:
        print('\nThe word', word, 'was found at:')
        print(*foundWord, sep='\n')
    else:
        print('\nWord never found')


if __name__ == '__main__':
    main()
