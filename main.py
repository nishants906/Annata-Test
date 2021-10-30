import getopt
import sys
import requests
from bs4 import BeautifulSoup


def findWordsInHTMLString(html_str, word):
    words_list = list(html_str.lower().split())
    return words_list.count(word.lower())


def getHTMLString(url):
    url = url
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    html_string = ''.join(e for e in soup.get_text() if (e.isalnum()) or e == " ")
    return html_string


def main(argv):
    url = ''
    words_list = []
    try:
        opts, args = getopt.getopt(argv, '', ["url=", "words="])
    except:
        pass

    for opt, arg in opts:
        if opt in "--url":
            url = arg
        elif opt in "--words":
            words_list = arg.split(',')
    return url, words_list


if __name__ == "__main__":
    url, words_list = main(sys.argv[1:])
    html_str = getHTMLString(url)
    output_JSON = {}
    for word in words_list:
        output_JSON[word] = findWordsInHTMLString(html_str, word)

    for k in output_JSON:
        print(k + ' : ' + str(output_JSON[k]), end='\n')
