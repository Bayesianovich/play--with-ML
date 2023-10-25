1- 对数值型数据进行合理性检查，首先要看看它的量级(magnitude).
- 在考虑下它的特征的尺度(scale). 如果模型是输入特征的平滑函数，那么它对输入的尺度是非常敏感的，它的输出尺度直接取决于出入输入尺度.对于像 所有使用欧式距离的方法：linear function、_k_-means clustering、 nearest neighbors methods、  radial basis function (RBF) kernels的模型，这类模型和模型成分，通常需要对特征进行标准化，以便将输出控制在期望的范围之内。
- **Logical functions**， on the other hand, are not sensitive to input feature scale. Their output is binary no matter what the inputs are.
- models based on space-partitioning trees (decision trees, gradient boosted machines, random forests) are not sensitive to scale.
- **Interaction features** are simple to formulate,but the combination of features results in many more being input into the model. In order to reduce the computational expense, it is usually necessary to prune the input features using automatic _feature selection_.
- 在数据世界中,抽象的向量和它的特征维度具有实际意义。
- collectively，a collection of data can be visualized in feature space as a point cloud.

# Dealing with Counts
 ## Binarization
 - 听歌次数  binarization
 Quantization or Binning
 - 原始的点评数量横跨若干个数量级，这对很多模型来说都是个问题 
 - 线性模型，会受异常值扰动的影响
 - k-means 它使用欧式距离作为相似度函数来测量数据点之间的相似度。数据向量某个元素过大的计数值对相似度的影响会远远超过其他元素，从而破坏整体的相似度测量。
 - One solution is to contain the scale by _quantizing_ the count.In other words, we group the counts into bins, and get rid of the actual count values. 
 - Quantization maps a continuous number to a discrete one. We can think of the discretized numbers as an ordered sequence of bins that represent a measure of intensity.
 - ### Fixed-width binning
     - can be linearly scaled or exponentially scaled.
- ### Quantile binning
     - Fixed-width binning is easy to compute. But if there are large gaps in the counts, then there will be many empty bins with no data. This problem can be solved by adaptively positioning the bins based on the distribution of the data. This can be done using the quantiles of the distribution.
     - 
pandas.DataFrame.quantile和pandas.Series.quantile可以计算分位数；pandas.qcut可以将数据映射为所需的分位数值.
## Log Transformation
- The log function compresses the range of large numbers and expands the range of small numbers. The larger x is, the slower log(x) increments.
- The log transform is a powerful tool for dealing with positive numbers with a heavy-tailed distribution. 
