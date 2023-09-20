import re
from collections import defaultdict
import sys


def map_function(line):
    word_list = re.findall(r"[\w']+", line)  
    for i in range(len(word_list) - 1):
        bigram = f"{word_list[i]},{word_list[i + 1]}"
        yield (bigram, 1)


def reduce_function(bigrams): #creating the bigrams
    bigram_counts = defaultdict(int)
    for bigram, count in bigrams:
        bigram_counts[bigram] += count
    return bigram_counts.items()


if len(sys.argv) != 2:
    print("Usage: python word_count.py <input_file>")
    sys.exit(1)
else:
    input_file = sys.argv[1]


with open(input_file, 'r') as file:
    input_lines = file.readlines()

mapped_results = []
for line in input_lines:
    mapped_results.extend(map_function(line))

reduced_results = reduce_function(mapped_results)

for bigram, count in reduced_results:
    print(f'"{bigram}" {count}')