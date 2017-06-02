from collections import Counter


def get_ngrams(blocks_file, num):
    ngrams_array = []

    with open(blocks_file, 'r') as f_block:
        for block in f_block:
            block_array = block.strip().split(' ')[1:]

            for counter in range(len(block_array) - num + 1):
                ngram = []

                for offset in range(num):
                    ngram.append(block_array[counter + offset])

                ngram = ' '.join(ngram)
                ngrams_array.append(ngram)

    return Counter(ngrams_array)
