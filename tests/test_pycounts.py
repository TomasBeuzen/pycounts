from pycounts.pycounts import count_words
from pycounts.plotting import plot_words
from pycounts.datasets import get_flatland
import matplotlib
from collections import Counter
import pytest

@pytest.fixture
def einstein_counts():
    return Counter({'insanity': 1, 'is': 1, 'doing': 1, 
                    'the': 1, 'same': 1, 'thing': 1, 
                    'over': 2, 'and': 2, 'expecting': 1,
                    'different': 1, 'results': 1})

def test_count_words(einstein_counts):
    """Test word counting from a file."""
    expected = einstein_counts
    actual = count_words("tests/einstein.txt")
    assert actual == expected, "Einstein quote words counted incorrectly!"

def test_plot_words(einstein_counts):
    """Test plotting of word counts."""
    fig = plot_words(einstein_counts)
    assert isinstance(fig, matplotlib.container.BarContainer), "Wrong plot type"
    assert len(fig.datavalues) == 10, "Incorrect number of bars plotted"

@pytest.mark.parametrize(
    "obj",
    [
        3.141,
        "test.txt",
        ["list", "of", "words"]
    ]
)
def test_plot_words_error(obj):
    """Check TypeError raised when Counter not used."""
    with pytest.raises(TypeError):
        plot_words(obj)

def test_integration():
    """Test count_words() and plot_words() workflow."""
    counts = count_words("tests/einstein.txt")
    fig = plot_words(counts)
    assert isinstance(fig, matplotlib.container.BarContainer), "Wrong plot type"
    assert len(fig.datavalues) == 10, "Incorrect number of bars plotted"
    assert max(fig.datavalues) == 2, "Highest word count should be 2"

def test_regression():
    """Regression test for Flatland"""
    top_word = count_words(get_flatland()).most_common(1)
    assert top_word[0][0] == "the", "Most common word is not 'the'"
    assert top_word[0][1] == 2245, "'the' count has changed"