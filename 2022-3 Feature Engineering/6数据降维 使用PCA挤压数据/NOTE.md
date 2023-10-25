# Dimensionality Reduction: Squashing the Data Pancake with PCA
Model-based techniques, on the other hand, require information from the data.

## Intuition
Dimensionality reduction is about getting rid of “uninformative information” while retaining the crucial bits. There are many ways to define “uninformative.” PCA focuses on the notion of linear dependency.

The key idea here is to _replace redundant features with a few new features that adequately summarize information contained in the original feature space_.

One way to mathematically define “adequately summarize information” is to say that the new data blob should retain as much of the original volume as possible.
![[SVD.png]]


![[PCA PROCESSING.png]]
![[Implementing PCA.png]]
The two main things to remember about PCA are its mechanism (**linear projection**) and
objective (to **maximize the variance of projected data**).