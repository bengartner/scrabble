import argparse
import functools

# 0: ?×2
# 1: E×12 A×9 I×9 O×8 N×6 R×6 T×6 L×4 S×4 U×4
# 2: D×4 G×3
# 3: B×2 C×2 M×2 P×2
# 4: F×2 H×2 V×2 W×2 Y×2
# 5: K
# 8: J X
# 10: Q Z

score_lookup = {
    'a' : 1,
    'b' : 3,
    'c' : 3,
    'd' : 2,
    'e' : 1,
    'f' : 4,
    'g' : 2,
    'h' : 4,
    'i' : 1,
    'j' : 8,
    'k' : 5,
    'l' : 1,
    'm' : 3,
    'n' : 1,
    'o' : 1,
    'p' : 3,
    'q' : 10,
    'r' : 1,
    's' : 1,
    't' : 1,
    'u' : 1,
    'v' : 4,
    'w' : 4,
    'x' : 8,
    'y' : 4,
    'z' : 10
}

word_list = []
with open('enable1.txt', 'r') as f:
    for line in f.readlines():
        word_list.append(line.strip())

@functools.lru_cache(maxsize=1000000)
def score_word_naive(word):
    sum_ = 0
    for letter in word:
        sum_ += score_lookup[letter]
    return sum_

@functools.lru_cache(maxsize=1000000)
def iterate_over_subwords(word):
    for i in range(0,len(word)+1):
        for j in range(2,len(word)+1-i):
            yield word[i:i+j]

@functools.lru_cache(maxsize=1000000)
def score_word_complex(word):
    subwords = set()
    for subword in iterate_over_subwords(word):
        if subword in word_list:
            subwords.add(subword)
    sum_ = sum([score_word_naive(subword) for subword in subwords])
    return sum_

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("threshold")
    args = parser.parse_args()
    for word in word_list:
        score = score_word_complex(word)
        if score > int(args.threshold):
            print(f"{word} : {score}")