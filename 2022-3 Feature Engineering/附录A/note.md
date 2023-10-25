# Linear Modeling and Linear Algebra Basics
When we have a labeled dataset, the feature space is strewn with data points from different classes. It is the job of the classifier to separate the data points from different classes. It can do so by producing an output that is very different for data points from one class versus another. For instance, when there are only two classes, then a good classifier should produce large outputs for one class, and small ones for another. The points right on the cusp of being in one class versus another form a _decision surface_
![[decision surface.png]]
we’re willing to sacrifice some training accuracy in order to have a simpler decision surface that can achieve better test accuracy. The principle of **minimizing complexity and maximizing usefulness** is called “**Occam’s razor,**” and is widely applicable in science and engineering.


One of the most fascinating theorems of linear algebra proves that e**very square matrix, no matter what numbers it contains, must map a certain set of vectors back to themselves with some scaling. In the general case of a rectangular matrix, it maps a set of input vectors into a corresponding set of output vectors, and its _transpose_ maps those outputs back to the original inputs.** The technical terminology is that square matrices have eigenvectors with eigenvalues, and rectangular matrices have left and right singular vectors with singular values.![[附录A/SVD.png]]
Algebraically, the SVD of a matrix looks like this:

$A$= **$UΣV^{T}$

where the columns of the matrices _**U**_ and _**V**_ form orthonormal bases of the input and output space, respectively. _**Σ**_ is a diagonal matrix containing the singular values.

Geometrically, a matrix performs the following sequence of transformations:
1.  Map the input vector onto the right singular basis vector.
2.  Scale each coordinate by the corresponding singular values.
3.  Multiply this score with each of the left singular vectors.
4.  Sum up the results.![[interpretation.png]]