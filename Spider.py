from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse
# from sys import argv


class LinkParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    # Get all the links on the page
                    newUrl = parse.urljoin(self.baseUrl, value)
                    # Add only the new links to self.links
                    if newUrl not in self.links:
                        self.links = self.links + [newUrl]

    def getLinks(self, url):
        self.links = []
        self.baseUrl = url
        response = urlopen(url)
        # Only access if the file is html
        if response.getheader('Content-Type') == 'text/html':
            # Read the html data on the page
            htmlBytes = response.read()
            htmlString = htmlBytes.decode('utf-8')
            # feed only reads strings and not bytes
            self.feed(htmlString)
            # Called handle_starttag and get links on the page
            return htmlString, self.links
        else:
            return '', []


def spider(url, word, maxPages):
    pagesToVisit = [url]
    numberVisited = 0
    i = 0
    foundWord = []
    while numberVisited < maxPages and pagesToVisit != []:
        numberVisited = numberVisited + 1
        url = pagesToVisit[i]
        i = i + 1
        # pagesToVisit = pagesToVisit[1:]
        try:
            print(numberVisited, 'Visiting: ', url)
            parser = LinkParser()
            data, links = parser.getLinks(url)
            # Find the word in the html data of the page
            if data.find(word) > -1:
                foundWord.append(url)
            # Add the links in the Links List to pagesToVisit after removing duplicates
            pagesToVisit.extend(page for page in links if page not in pagesToVisit)
            print('**Success!**')
        except:
            print('**Failed!**')

    if foundWord is not []:
        print('The word', word, 'was found at:')
        print(*foundWord, sep='\n')
    else:
        print('Word never found')


if __name__ == '__main__':
    url = input('Enter the URL of the website to search: ')
    word = input('Enter the word(s) to search: ')
    maxPages = input('Enter the max no of pages to search: ')
    #script, url, word, maxPages = argv
    spider(url, word, int(maxPages))
