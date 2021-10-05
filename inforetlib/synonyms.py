import requests
from bs4 import BeautifulSoup
import nltk

class Synonyms:
    def __init__(self):
        """
        Allows you to get synonyms for a word by scraping off the thesaurus.com website

        NOTE:
        CSS class elements that contain relevant synonyms were found through examination of 
        webpage, they are:
        - 1kg1yv8 
        - 1n6g4vv 
        - 1gyuw4i 
        """
        self.__url = 'https://www.thesaurus.com/browse/{}'

    def get(self,word,stem):
        response = requests.get(self.__url.format(word))
        soup = BeautifulSoup(response.text,'html.parser')
        raw_synonyms = soup.find_all('a',{"data-linkid":"nn1ov4","font-weight":"inherit"})
        try:
            synonyms = [i.getText().strip() for i in raw_synonyms if i['class'][0] in ['css-1kg1yv8','css-1n6g4vv','css-1gyuw4i']]
            synonyms = [i for i in synonyms if len(i.split()) == 1]
            if stem:
                ps = nltk.stem.PorterStemmer()
                synonyms = [ps.stem(w) for w in synonyms]
            return synonyms
        except:
            return []