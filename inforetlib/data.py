import os
import json
import xmltodict

class LoadData:
    def __init__(self):
        """
        Allows the user to load data from the included sample of the TREC covid database.
        """
        self.__path = os.path.dirname(os.path.realpath(__file__)) 
    
    def _printpath(self):
        print(self.__path)

    @staticmethod
    def chunks(l,n):
        n = max(1,n)
        return [l[i:i+n] for i in range(0,len(l),n)]

    def load_corpus(self):
        f = open('{}/files/TRECcovid/corpus_small.jsonl'.format(self.__path)).readlines()
        corpus = [json.loads(i) for i in json.loads(json.dumps(f))]
        return corpus

    def load_query_results(self):
        qrel = open('{}/files/TRECcovid/qrel_small.txt'.format(self.__path)).read().split('\n')
        qrel = [i.split('\t') for i in qrel if i != '']
        qtopicn,idn,label = list(zip(*qrel)) 
        return qtopicn,idn,label

    def load_topics(self):
        topics = open('{}/files/TRECcovid/topics_round5.xml'.format(self.__path)).read().split('\n')[1:-1]
        topics = LoadData.chunks(topics,5)
        topics = [xmltodict.parse(''.join(i)) for i in topics]
        topicn = [i['topic']['@number'] for i in topics]
        query = [i['topic']['query'] for i in topics]
        return topicn,query