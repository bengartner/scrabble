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
    'w' : 4,
    'x' : 8,
    'y' : 4,
    'z' : 10
}

def score_word_naive(word):
    sum_ = 0
    for letter in word:
        sum_ += score_lookup[letter]
    return sum_
