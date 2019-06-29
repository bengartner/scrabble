import scrabble
import pytest

# 0: ?×2
# 1: E×12 A×9 I×9 O×8 N×6 R×6 T×6 L×4 S×4 U×4
# 2: D×4 G×3
# 3: B×2 C×2 M×2 P×2
# 4: F×2 H×2 V×2 W×2 Y×2
# 5: K
# 8: J X
# 10: Q Z


@pytest.mark.parametrize(
    "word,score",
    [
        ("aa", 2),
        ("aah", 6),
        ("theater", 10),
        ("zodiac", 18),
        ("quiter", 15),
        ("boy", 8),
        ("lazy", 16),
        ("quick", 20),
        ("jumps", 16),
        ("fox", 13),
        ("brown", 10),
        ("dog", 5),
    ],
)
def test_naive_word_score(word, score):
    assert scrabble.score_word_naive(word) == score

