# Categorical Variables: Counting Eggs in the Age of Robotic Chickens
A _categorical variable_, as the name suggests, is used to represent categories or labels.

A simple question can serve as litmus test for whether something should be a categorical variable: “**Does it matter  _how_ different  two values are, or only that they _are_ different?” **

## One-Hot Encoding

If a category (e.g., word) appears multiple times in a data point (document), then we can represent it as a count, and represent all of the categories through their count statistics. This is called _bin_。

An encoding method is needed to turn these nonnumeric categories into numbers.It is tempting to simply assign an integer, say from 1 to _k_, to each of _k_ possible categories—but the resulting values would be orderable against each other, which should not be permissible for categories. So, let’s look at some alternatives.
![[one-hot encoding.png]]

A better method is to use a group of bits.  If the variable cannot belong to multiple categories at once, then only one bit in the group can be “on”.

Linear dependent features,  are slightly annoying because they mean that the trained linear models will not be unique.Different linear combinations of the features can make the same predictions, so we would need to jump through extra hoops to understand the effect of a feature on the prediction.



## Dummy Coding

The problem with one-hot encoding is that it allows for _k_ degrees of freedom, while the variable itself needs only _k_–1. _Dummy coding_[2](ch05.html#idm140610098631008)removes the extra degree of freedom by using only _k_–1 features in the representation below. One feature is thrown under the bus and represented by the vector of all zeros. This is known as the **reference category**. Dummy coding and one-hot encoding are both implemented in Pandas as [`pandas.get_dummies`](http://bit.ly/2mBNeJx).
![[dummy coding.png]]
The outcome of modeling with dummy coding is more interpretable than with one-hot encoding.


```python
# Convert the categorical variables in the DataFrame to one-hot encoding
# Specify the 'drop_first' flag to get dummy coding
```
## Effect Coding
Yet another variant of categorical  variable encoding is _effect coding_. Effect coding is very similar to dummy coding, with the difference that the reference category is now represented by the vector of all –1’s.![[effect Coding.png]]
Effect coding is very similar to dummy coding, but results in linear regression models that are even simpler to interpret.


## Pros and Cons of Categorical Variable Encodings
One-hot, dummy, and effect coding are very similar to one another. They each have pros and cons. One-hot encoding is redundant, which allows for multiple valid models for the same problem.The nonuniqueness is sometimes problematic for interpretation, but the advantage is that each feature clearly corresponds to a category.Moreover, missing data can be encoded as the all-zeros vector, and the output should be the overall mean of the target variable.


Dummy coding and effect coding are not redundant. They give rise to unique and interpretable models. The downside of dummy coding is that it cannot easily handle missing data, since the all-zeros vector is already mapped to the **reference category**. It also encodes the effect of each category relative to the reference category, which may look strange.


Effect coding avoids this problem by using a different code for the **reference category**, but **the vector of all –1’s is a dense vector, which is expensive for both storage and computation**. For this reason, popular ML software packages such as Pandas and scikit-learn have opted for **dummy coding or one-hot encoding instead of effect coding.**

# Dealing with Large Categorical Variables

Automated data collection on the internet can generate large categorical variables. This is common in applications such as **targeted advertising and fraud detection.**

Existing solutions can be categorized (haha) thus:
1.  Do nothing fancy with the encoding. Use a simple model that is cheap to train. Feed one-hot encoding into a linear model (logistic regression or linear support vector machine) on lots of machines.
2.  Compress the features. There are two choices:
    1.  Feature hashing, popular with linear models
    2.  Bin counting, popular with linear models as well as trees 
## Feature Hashing
A _hash function_ is a deterministic function that maps a potentially unbounded integer to a finite integer range [1, _m_].Since the input domain is potentially larger than the output range, multiple numbers may get mapped to the same output. This is called a _collision_. A _uniform hash function_ ensures that roughly the same number of numbers are mapped into each of the _m_ bins.
![[hash function.png]]
Another variation of feature hashing adds a sign component, so that counts are either added to or subtracted from the hashed bin .Statistically speaking, this ensures that the inner products between hashed features are equal in expectation to those of the original features.

One downside to feature hashing is that the hashed features, being aggregates of original features, are no longer interpretable.

## Bin Counting
Bin counting is one of the perennial rediscoveries in machine learning. It has been reinvented and used in a variety of applications, from ad click-through rate prediction to hardware branch prediction (Yeh and Patt, 1991; Lee et al., 1998; Chen et al., 2009; Li et al., 2010).

The idea of bin counting is deviously simple: rather than using the _value_ of the categorical variable as the feature, instead use the _conditional probability_ of the target under that value. In other words, instead of encoding the identity of the categorical value, we compute the association statistics between that value and the target that we wish to predict.

Bin counting assumes that historical data is available for computing the statistics.In short, bin counting converts a categorical variable into statistics about the value. It turns a large, sparse, binary representation of the categorical variable, such as that produced by one-hot encoding, into a very small, dense, real-valued numeric representation![[bin.png]]
### What about rare categories?
One way to deal with this is through _back-off_, a simple technique that accumulates the counts of all rare categories in a special bin![[back-off.png]]
There is another way to deal with this problem, called the _count-min sketch_
### Guarding against data leakage
Since bin counting relies on historical data to generate the necessary statistics, it requires waiting through a data collection period, incurring a slight delay in the learning pipeline. Also, when the data distribution changes, the counts need to be updated. The faster the data changes, the more frequently the counts need to be recomputed.

Using the output to compute the input features leads to a pernicious problem known as _leakage_. In short, leakage means that information is revealed to the model that gives it an unrealistic advantage to make better predictions.![[time-window.png]]
It turns out that there is another solution, based on differential privacy. A statistic is _approximately leakage-proof_ if its distribution stays roughly the same with or without any one data point