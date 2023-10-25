# Nonlinear Featurization via K-Means Model Stacking

A flat *plane* (linear subspace) can be generalized to a _manifold_(nonlinear subspace), which can be thought of as a surface that gets stretched and rolled in various ways.

# _K_-MEANS FEATURIZATION

Clustering algorithms analyze the spatial distribution of data. Therefore, _k_-means featurization creates a compressed spatial index of the data which can be fed into the model in the next stage.  This is an example of _model stacking_.

Using _k_-means to turn spatial data into features is an example of _model stacking_, where the input to one model is the output of another. Another example of stacking is to use the output of a decision tree–type model (random forest or gradient boosting tree) as input to a linear classifier. Stacking has become an increasingly popular technique in recent years. Nonlinear classifiers are expensive to train and maintain. The key intuition with stacking is to push the nonlinearities into the features and use a very simple, usually linear model as the last layer.

# KEY INTUITION FOR MODEL STACKING
Use sophisticated base layers (often with expensive models) to generate good (often nonlinear) features, combined with a simple and fast top-layer model. This often strikes the right balance between model accuracy and speed.