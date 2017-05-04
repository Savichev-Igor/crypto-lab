from collections import Counter
import operator

def get_probs(block_file, probs_file):
    cnt = Counter()
    with open(block_file, 'r') as f_block:
        with open(probs_file, 'w') as f_probs:
            for block in f_block:
                for number in block.split(' '):
                    cnt[number] += 1
            sorted_probs = sorted(cnt.items(), key=operator.itemgetter(1), reverse=True)
            for el, count in sorted_probs:
                f_probs.write(str(el) + ' ' + str(count) + '\n')
if __name__ == "__main__":
    b_file = 'blocks/all_blocks.txt'
    probs_file = 'all_blocks_probs.txt'
    get_probs(b_file, probs_file)