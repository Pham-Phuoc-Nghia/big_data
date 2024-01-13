from mrjob.job import MRJob
import re

class WordCount(MRJob):
    def mapper(self, _, line):
        words = re.findall(r'\w', line.lower())

        for word in words:
            yield word,1
    def reducer(self, word, counts):
        total_count = sum(counts)

        yield word,total_count
if __name__ == '__main__':
    WordCount.run()