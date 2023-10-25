

英文下的

**Text Data：Flattening, Filtering, and Chunk**
_bag-of-words

- A very much related transformation is _tf-idf_, which is essentially a feature scaling technique.

- The current chapter first talks about **text extraction features**, then delves into **how to filter and clean those features**.
- ![[词袋.png]]
- Bag-of-words converts a text document into a flat vector. It is “flat” because it doesn’t contain any of the original textual structures
- What is important in Bag-of-words is the geometry of data in feature space, In a bag-of-words vector, each word becomes a dimension of the vector.

![[feature.png]]
document space
![[document space.png]]
- （n元词袋）Bag-of-_n_-Grams, or bag-of-_n_-grams, is a natural extension of bag-of-words. An _n_-gram is a sequence of _n_ tokens. A word is essentially a 1-gram, also known as a _unigram_. After tokenization, the counting mechanism can collate individual tokens into word counts, or count overlapping sequences as _n_-grams. For example, the sentence “Emma knocked on the door” generates the _n_-grams “Emma knocked,” “knocked on,” “on the,” and “the door.”
- _n_-grams retain **more of the original sequence structure of the text,** and therefore the bag-of-_n_-grams representation can be more informative.

## Filtering for Cleaner Features
With words, how do we cleanly separate the signal from the noise? Through filtering, techniques that use raw tokenization and counting to generate lists of simple words or _n_-grams become more usable.
###  Stopwords
Classification and retrieval do not usually require an in-depth understanding of the text.

## Frequency-Based Filtering
- [ ] Stopword lists are a way of weeding out common words that make for vacuous features.There are other, more statistical ways of getting at the concept of “common words.”
### Frequent words
Frequency statistics are great for filtering out corpus-specific common words as well as general-purpose stopwords.

Frequency statistics helps to combine frequency-based filtering with a stopword list. There is also the tricky question of where to place the cutoff. Unfortunately there is no universal answer.

### Rare words
Depending on the task, one might also need to filter out rare words. These might be truly obscure words, or misspellings of common words.

Not only are rare words unreliable as predictors, they also generate computational overhead.
## Stemming
One problem with simple parsing is that different variations of the same word get counted as separate words.
# Atoms of Meaning: From Words to n-Grams to Phrases
- A text document is represented digitally as a string, which is basically a sequence of characters. One might also run into semi-structured text in the form of JSON blobs or HTML pages. But even with the added tags and structure, the basic unit is still a string.
- How does one turn a string into a sequence of words ：_parsing_ and _tokenization_,
## Parsing and Tokenization
Parsing is necessary when the string contains more than plain text
After light parsing, the plain-text portion of the document can go through tokenization.

## Collocation Extraction for Phrase Detection
In the words of Manning and Schütze (1999: 151), “A collocation is an expression consisting of two or more words that correspond to some conventional way of saying things.”

Collocations are more meaningful than the sum of their parts.

### Frequency-based methods
 A simple hack is to look at the most frequently occurring _n_-grams. The problem with this approach is that the most frequently occurring ones may not be the most useful ones.

### Hypothesis testing for collocation extraction
Raw popularity count is too crude of a measure.

Hypothesis testing is a way to boil noisy data down to “yes” or “no” answers.

In the context of collocation extraction, many hypothesis tests have been proposed over the years. One of the most successful methods is based on the likelihood ratio test (Dunning, 1993).

### Chunking and part-of-speech tagging

Chunking is a bit more sophisticated than finding _n_-grams, in that it forms sequences of tokens based on parts of speech, using rule-based models.









