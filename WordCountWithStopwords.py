from mrjob.job import MRJob
import re

stopwords = set(["the", "and", "of", "a", "to", "in", "is", "it"])

class WordCountWithStopwords(MRJob):

    def mapper(self, _, line):
        words = re.findall(r'\b\w+\b', line.lower()) # finding the stopwords defined
        
        for word in words:
            if word not in stopwords:
                yield (word, 1)

    def reducer(self, word, counts):
        total_count = sum(counts)
        
        yield (word, total_count)

if __name__ == '__main__':
    WordCountWithStopwords.run()