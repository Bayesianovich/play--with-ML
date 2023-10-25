# The Effects of Feature Scaling: From Bag-of-Words to Tf-Idf

A bag-of-words representation is simple to generate but far from perfect.

The main characters do not stand out by simple frequency count alone. This is problematic.

we’d like a representation that highlights _meaningful_ words.

Tf-idf is a simple twist on the bag-of-words approach. It stands for _term frequency_–_inverse document frequency_.  Instead of looking at the raw counts of each word in each document in a dataset, tf-idf looks at a normalized count where each word count is divided by the number of documents this word appears in. That is:

bow(_w_, _d_) = # times word _w_ appears in document _d_

tf-idf(_w_, _d_) = bow(_w_, _d_) * _N_ / (# documents in which word _w_ appears)

_N_ is the total number of documents in the dataset. The fraction _N_ / (# documents ...) is what’s known as the _inverse document frequency_. If a word appears in many documents, then its inverse document frequency is close to 1. If a word appears in just a few documents, then the inverse document frequency is much higher.

Alternatively, we can take a log transform instead using the raw inverse document frequency.

If we define tf-idf as:

tf-idf(_w_, _d_) = bow(_w_, _d_) * log (_N_ / # documents in which word _w_ appears)

then a word that appears in every single document will be effectively zeroed out, and a word that appears in very few documents will have an even larger count than before.

# INTUITION BEHIND TF-IDF
Tf-idf makes rare words more prominent and effectively ignores common words.

Tf-idf transforms word count features through multiplication with a constant. Hence, it is an example of _feature scaling。

 To save on training time, we can take a subset of the reviews. In this case, there is a large difference in review count between the two categories. This is called a _class-imbalanced dataset_. Imbalanced datasets are problematic for modeling because the model will expend most of its effort fitting to the larger class. a good way to resolve the problem is to    **downsample the larger class** (restaurants) to be roughly the same size as the smaller class (nightlife).

When we use **training statistics to scale test data**, the result will look a little fuzzy. Min-max scaling on the test set no longer neatly maps to 0 and 1. $l ^ { 2 }$  norms, mean, and variance statistics will all look a little off. This is less problematic than missing data.The common solution is to simply drop the new words in the test set.A slightly less hacky option would be to explicitly learn a “garbage” word and map all low-frequency words to it, even within the training set, as discussed in [“Rare words”](ch03.html#sec-basic-text-rare-words).

## Tuning Logistic Regression with Regularization
When the number of features is greater than the number of data points, the problem of finding the best model is said to be _underdetermined_. One way to fix this problem is by placing additional constraints on the training process. This is known as _regularization_。

Regularization parameters are _hyperparameters_ that are not learned automatically in the model training process. Rather, they must be tuned on the problem at hand and given to the training algorithm. This process is known as hyperparameter tuning.

 One basic method for tuning hyperparameters is called _grid search_: you specify a grid of hyperparameter values and the tuner programmatically searches for the best hyperparameter setting in the grid.


The data matrix contains data points represented as fixed-length flat vectors. With bag-of-words vectors, the data matrix is also known as the _document-term matrix_.

![[文档-词袋矩阵.png]]
Feature scaling methods are essentially column operations on the data matrix. In particular, tf-idf and _ℓ_2 normalization both multiply the entire column (an _n_-gram feature, for example) by a constant.

Where feature scaling—both ℓ_2 and tf-idf—**does have a telling effect** is on t**he convergence speed of the solver**. This is a sign that the data matrix now has a much smaller condition number (**the ratio between the largest and smallest singular values**。 In fact, ℓ_2 normalization makes the condition number nearly 1. But it’s not the case that the better the condition number, the better the solution. During this experiment, ℓ_2normalization converged much faster than either BoW or tf-idf. But it is also more sensitive to overfitting: it requires much more regularization and is more sensitive to the number of iterations during optimization.


特征值和奇异值的区别?
特征值是方阵所有，奇异值是所有矩阵。

特征值可正可负可为0，奇异值是非负的。

特征值对应着到自身空间的变换，及缩放尺度，而奇异值则表示着到另一个空间的变换。

To summarize, the lesson is: the _right_ feature scaling can be helpful for classification. The right scaling accentuates the informative words and downweights the common words. It can also reduce the condition number of the data matrix. The right scaling is not necessarily uniform column scaling.
![[sig eng.png]]
