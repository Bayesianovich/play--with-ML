Reservoir Sampling is an algorithm for sampling elements from a stream of data.

- The size of the stream is unknown;
- You only access the data single pass;
- All items have the same probability to be selected.

more complex option is **reservoir sampling**

-------------------
algorithm reservoir $(k, S)$
$/ *$ take $k$ random samples from the dataset $S *$ /
1. initialize an array samples of size $k$
2. for $i=1$ to $n=|S|$
3. $o=$ the $i$-th item
4. if $i \leq k$ then
5. samples $[i]=o$
6. else
7. generate a random integer from 1 to $i$
8. if $i \leq k$ then
9. $\quad$ samples $[i]=0$
    发生替换的概率为$k/i$
The reservoir algorithm is very efficient: it spends $O(1)$ time per item. Next, we will show that the algorithm is correct, namely:

- Every item of S has the same probability of being sampled
- For any two items $o_{1}$ and $o_{2}$ , the events they are sampled are independent from each other

eg.

Let $S=\{59,100,2,30,63, \cdots\}$, and $k=3$.
- The first $k$ items are directly added to the sample set. So samples $=(59,100,2)$.
- Given the 4th item, the algorithm generates a random integer $i$ from 1 to 4 . Assume that the generated $i=4$. As $i>k$, the item is ignored.
- Given the 5th item, again, the algorithm generates $i$ randomly, but now from 1 to 5 . Assume that $i=2$ this time. Hence, the item is added to samples, and replaces the 2 nd value there. Hence, samples becomes $(59,63,2)$.
- 当总体中的个体无限多且要求每个个体被抽中的概率相等时，水库抽样算法是不二选择。