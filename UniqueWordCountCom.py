import sys

def count_unique_words(input_file):
    word_count = {}
    
    try:
        with open(input_file, 'r') as file: # taking the input file defined 
            for line in file:
                words = line.strip().split()
                for word in words:
                    word = word.lower() 
                    if word not in word_count:
                        word_count[word] = 1
                    else:
                        word_count[word] += 1
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    return word_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python word_count.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    word_count = count_unique_words(input_file)

    for word, count in word_count.items():
        print(f'"{word}" {count}')

if __name__ == "__main__":
    main()
