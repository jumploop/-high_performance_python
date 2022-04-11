import itertools
import codecs
import glob

# Clean the raw wordlists into a unique 500,000(ish) word single file

# "Moby Words lists by Grady Ward"
# http://www.gutenberg.org/ebooks/3201
LONG_FILES = glob.glob('mword10/*')
SUMMARISED_FILE = "all_unique_words.txt"


def read_words(filename):
    # return words from filename using a generator
    try:
        with codecs.open(filename, 'r', 'Windows-1252') as f:
            for line_nbr, line in enumerate(f):
                yield from line.strip().split()
    except UnicodeDecodeError:
        print(
            f"UnicodeDecodeError for {filename} near line {line_nbr} and word {line}"
        )

readers = itertools.chain(*(read_words(lf) for lf in LONG_FILES))

if __name__ == "__main__":
    words_set = set(readers)
    print(f"Summarising input files into one output set of {len(words_set)} words")
    with codecs.open(SUMMARISED_FILE, 'w', 'Windows-1252') as f:
        for word in words_set:
            f.write(word + "\n")

