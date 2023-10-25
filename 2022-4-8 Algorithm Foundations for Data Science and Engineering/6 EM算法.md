**Bernoulli mixture models (BMMs)**
First experiment
- We choose 5 times one of the coins;
- We toss the chosen coin 10 times.

![[COINS.png]]
### Unobserved Variable
A variable can be **unobserved (latent)** because:
- It is an imaginary quantity meant to provide some simplified and abstractive view of the data generation process,e.g., speech recognition models,mixture models;
- It is a real-world object and/or phenomena,but difficult or impossible to measure,e.g.,the temperature of a star, causes of a disease,evolutionary ancestors;
- It is a real-world object and/or phenomena,but sometimes was not measured,because of faulty sensors;or was measure with a noisy channel,etc.,e.g.,traffic radio,aircraft signal on a radar screen.
Discrete latent variables can be used to partition/cluster data  into sub-groups(mixture models).

###### Mixed models
![[Mixed models.png]]
- A density model p(x) may be multi-modal;
- We may be able to model it as a mixture of uni-modal distributions (e.g.,Bernoulli or Gaussians,etc).
- Each mode may correspond to a different sub-population e.g.,male and female).


例 $6.10$ 是一个混合高斯模型。假设每一个样本都对应一个隐变量 $C_{i}$ (随机变量), 其取值为 $\mathrm{M}$ (男生) 或 $\mathrm{F}$ (女生), 那么观测到样本值 $x_{i}$ 的概率为
$$
P\left(x_{i}, C_{i}\right)=\left(P\left(x_{i} \mid \mathrm{M}\right) P(\mathrm{M})\right)^{I_{C_{i}=\mathrm{M}}}\left(P\left(x_{i} \mid \mathrm{F}\right) P(\mathrm{~F})\right)^{I_{C_{i}=\mathrm{F}}}
$$
其中 $I_{C_{i}=\mathrm{M}} 、 I_{C_{i}=\mathrm{F}}$ 为取 0,1 值的伯努利随机变量, 当该样本表示男生或女生的身高时, 其值为 1 , 否则为 0 。因此, 对数似然函数表示为
$$
\begin{aligned}
&l\left(\mu_{\mathrm{M}}, \mu_{\mathrm{F}} \mid x_{1}, x_{2}, \cdots, x_{n}, C_{1}, C_{2}, \cdots, C_{n}\right) \\
&=\sum_{i=1}^{n}\left[C_{C_{\mathrm{i}}=\mathrm{M}} \log P\left(x_{i} \mid \mathrm{M}\right) P(\mathrm{M})+I_{C_{i}=\mathrm{F}} \log P\left(x_{i} \mid \mathrm{F}\right) P(\mathrm{~F})\right]
\end{aligned}
$$
由于对数似然函数中含有随机变量, 其极值是不确定的, 因此无法直接求解函数的极值点。也就是说, 此时的对数似然函数是多个随机变量的函数, 它也是一个随机变量, 无法直接求解函数的极值点。*如果知道了这些随机变量的后验分布, 那么可以求对数似然函数的后验期望, 然后再求对数似然函数后验期望的极值*。**这就是 EM 算法的做法**。
因 $I_{C_{i}=\mathrm{M}}$ 是伯努利随机变量, 可以求解观测到的样本值 $x_{i}$ 的后验概率 $P\left(C_{i}=\right.$ $\left.\mathrm{M} \mid x_{i}\right)$ :
$$
\begin{aligned}
P\left(C_{i}=\mathrm{M} \mid x_{i}\right) &=\frac{P\left(x_{i} \mid C_{i}=\mathrm{M}\right) P\left(C_{i}=\mathrm{M}\right)}{P\left(x_{i} \mid C_{i}=\mathrm{M}\right) P\left(C_{i}=\mathrm{M}\right)+P\left(x_{i} \mid C_{i}=\mathrm{F}\right) P\left(C_{i}=\mathrm{F}\right)} \\
&=\frac{\pi_{\mathrm{M}} N\left(x_{i} \mid \mu_{\mathrm{M}}, \sigma^{2}\right)}{\pi_{\mathrm{M}} N\left(x_{i} \mid \mu_{\mathrm{M}}, \sigma^{2}\right)+\pi_{\mathrm{F}} N\left(x_{i} \mid \mu_{\mathrm{F}}, \sigma^{2}\right)} \\
& \doteq q(\mathrm{M}) \\
P\left(C_{i}=\mathrm{F} \mid x_{i}\right) &=1-P\left(C_{i}=\mathrm{M} \mid x_{i}\right) \\
&=1-q(\mathrm{M})
\end{aligned}
$$
一旦求得了这个概率, 就可以通过求解对数似然函数后验期望的极值点来估计模 型的参数。但是其中的概率 $P\left(x_{i} \mid C_{i}=\mathrm{M}\right)$ 与模型参数有关, 这正是需要估计的。









### EM算法

EM算法是一种**迭代优化方法**，以上一轮的参数估计为新一轮迭代的参数先验值，其中每轮迭代由两步组成,**第一步是对似然函数求后验期望**，**第二步是最大化似然函数的后验期望**，从而获得模型的参数估计。

令 $l(\theta \mid x, C)$ 为不完全数据的对数似然函数, 其中 $x$ 为观测到的样本值, $C$ 为模型中的隐变量, $\theta$ 为待估参数。假设当前为第 $k+1$ 轮迭代, 上一轮得到的参数 $\theta$ 的估计 值为 $\theta^{(k)}$, 初始状态参数的先验值 $\theta^{(0)}=\left(\mu_{\mathrm{M}}^{(0)}, \mu_{\mathrm{F}}^{(0)}\right)$, 以及 $\pi_{\mathrm{M}}^{(0)}=1 / 2$ 。EM 算法主要由 $\mathrm{E}$ 步和 $\mathrm{M}$ 步组成。
**(1) $\mathrm{E}$ 步**
在计算了后验概率 $P\left(C_{i}=\mathrm{M} \mid x_{i}, \theta^{(k)}\right)$ 后, 求解对数似然函数的后验期望
$$
E_{C \mid \theta^{(k)}}(l(\theta \mid \boldsymbol{x}))
$$
这样**对数似然函数中的隐变量就由其后验期望所代替**, 此时它仅仅是关于 $\theta$ 的函数。基 于上一轮参数的估计值 $\theta^{(k)}=\left(\mu_{\mathrm{M}}^{(k)}, \mu_{\mathrm{F}}^{(k)}\right)$, 隐变量 $C_{i}=\mathrm{M}$ 的后验概率可以计算为
$$
\begin{aligned}
q_{i}(\mathrm{M})^{(k+1)} &=P\left(C_{i}=\mathrm{M} \mid x_{i}, \mu^{(k)}\right) \\
&=\frac{\pi_{\mathrm{M}}^{(k)} N\left(x_{i} \mid \mu_{\mathrm{M}}^{(k)}, \sigma^{2}\right)}{\pi_{\mathrm{M}}^{(k)} N\left(x_{i} \mid \mu_{\mathrm{M}}^{(k)}, \sigma^{2}\right)+\pi_{\mathrm{F}}^{(k)} N\left(x_{i} \mid \mu_{\mathrm{F}}^{(k)}, \sigma^{2}\right)}
\end{aligned}
$$
其中, $\pi_{\mathrm{M}}^{(k)}=1-\pi_{\mathrm{F}}^{(k)}=\left(\sum_{i=1}^{n} q_{i}(\mathrm{M})^{(k)}\right) / n$ 。
**(2) $M$ 步**
通过最大化 $E_{\left.C \mid \theta^{(k)}\right)}(l(\theta \mid x))$ 获取参数 $\theta$ 的新一轮估计值 $\theta^{(k+1)}$ :
$$
\theta^{(k+1)}=\arg \max _{\theta} E_{\left.C \mid \theta^{(k)}\right)}(l(\theta \mid x))
$$
为了估计参数 $\theta$ 的新一轮估计值 $\theta^{(k+1)}$, 计算 $E_{C \mid \theta(k)}(l(\theta \mid x))$ 对 $\theta$ 的偏导数, 并令 其为 0 , 得到
$$
\begin{gathered}
\frac{\partial}{\partial \mu_{\mathrm{M}}} l\left(\mu_{\mathrm{M}}, \mu_{\mathrm{F}} \mid \boldsymbol{x}\right)=\sum_{i=1}^{n} q(\mathrm{M})^{(k+1)} \frac{x_{i}-\mu_{\mathrm{M}}}{\sigma^{2}}=0 \\
\frac{\partial}{\partial \mu_{\mathrm{F}}} l\left(\mu_{\mathrm{M}}, \mu_{\mathrm{F}} \mid \boldsymbol{x}\right)=\sum_{i=1}^{n} q(\mathrm{~F})^{(h+1)} \frac{x_{i}-\mu_{\mathrm{F}}}{\sigma^{2}}=0
\end{gathered}
$$
因此, 得到第 $k+1$ 轮参数 $\theta^{(k+1)}=\left(\mu_{\mathrm{M}}^{(k+1)}, \mu_{\mathrm{F}}^{(k+1)}\right)$ 为
$$
\begin{aligned}
\mu_{\mathrm{M}}^{(k+1)} &=\frac{\sum_{i=1}^{n} q_{i}^{(k+1)}(\mathrm{M}) x_{i}}{\sum_{i=1}^{n} q_{i}^{(k+1)}(\mathrm{M})} \\
\mu_{\mathrm{F}}^{(k+1)} &=\frac{\sum_{i=1}^{n}\left(1-q_{i}^{(k+1)}(\mathrm{M})\right) x_{i}}{\sum_{i=1}^{n}\left(1-q_{i}^{(k+1)}(\mathrm{M})\right)}=\frac{\sum_{i=1}^{n} q_{i}^{(k+1)}(\mathrm{F}) x_{i}}{\sum_{i=1}^{n} q_{i}^{(k+1)}(\mathrm{F})}
\end{aligned}
$$
### EM算法的收敛性
EM算法使用启发式迭代法求出模型分布的参数。在混合模型中虽然不知道样本的来源，但可以先猜测样本的来源(**EM算法的E步**)，接着基于观察数据和猜测的样本来源最大化对数似然，求解模型的参数(**EM算法的M步**)。由于之前的隐含变量是猜测的，所以此时得到的模型参数一般还不是最终想要的结果。不过可以基于当前得到的模型参数，继续更新对隐含变量的猜测(EM算法的E步)，然后继续最大化对数似然，求解下一轮的模型参数(EM算法的M步)。以此类推，不断地迭代下去，直到模型分布参数基本无变化，算法收敛。
EM算法的流程并不复杂，但是还有两个问题需要思考:
- EM算法能否保证收敛
- 如果EM算法收敛，那么能否保证收敛到全局最优解？

首先来看第一个问题。假设 $l(\theta \mid x, C)$ 为**不完全数据的对数似然函数**, 其中 $x$ 和 $C$ 分别为观测到的样本值和模型中的隐变量。因此,
$$
\begin{aligned}
l(\theta \mid \boldsymbol{x}) &=\log L(\theta \mid \boldsymbol{x})=\log \prod_{i=1}^{n} p\left(x_{i} ; \theta\right) \\
&=\sum_{i=1}^{n} \log p\left(x_{i} ; \theta\right)=\sum_{i=1}^{n} \log \sum_{C} p\left(x_{i}, C ; \theta\right) \\
& \geqslant \sum_{i=1}^{n} \sum_{C} p\left(C ; \theta^{(k)}\right) \log \frac{p\left(x_{i}, C ; \theta\right)}{p\left(C ; \theta^{(k)}\right)} \\
&=\sum_{C} p\left(C ; \theta^{(k)}\right) \sum_{i=1}^{n} \log \frac{p\left(x_{i}, C ; \theta\right)}{p\left(C ; \theta^{(k)}\right)}
\end{aligned}
$$
上式推导中不等号成立是由 Jensen 不等式保证的。因为 $\log x$ 是一个凹函数, 当 $\lambda_{j} \geqslant 0$ 且 $\sum_{f} \lambda_{j}=1$ 时, 有
$$
\log \sum_{j} \lambda_{j} y_{j} \geqslant \sum_{j} \lambda_{j} \log y_{j}
$$
由于 $\sum_{C} p\left(C ; \theta^{(k)}\right)=1$ 且概率 $p\left(C ; \theta^{(k)}\right) \geqslant 0$ 。因此, 函数 $\sum_{i=1}^{n} \log \frac{p\left(x_{i}, C ; \theta\right)}{p\left(C ; \theta^{(k)}\right)}$ 的后验 期望为对数似然函数的下界, 而且
$$
\begin{aligned}
&\sum_{C} p\left(C ; \theta^{(k)}\right) \sum_{i=1}^{n} \log \frac{p\left(x_{i}, C ; \theta\right)}{p\left(C ; \theta^{(k)}\right)} \\
&=\sum_{C} p\left(C ; \theta^{(k)}\right) \sum_{i=1}^{n} \log p\left(x_{i}, C ; \theta\right)-n \sum_{C} p\left(C ; \theta^{(k)}\right) \log p\left(C ; \theta^{(k)}\right)
\end{aligned}
$$ 
其中上式等号右边的第一项为给定第$k$轮参数估计$\theta^{(k)}$时不完全数据的后验期望。即第 $k$ 轮 $\mathrm{EM}$ 算法的 $\mathrm{E}$ 步计算结果, 而等号右边的第二项是关于参数 $\theta$ 的一个常函数。这两部分分别记为 $Q\left(\theta \mid \theta^{(k)}\right)$ 和 $H\left(P\left(C ; \theta^{(k)}\right)\right)$, 即
$$
\begin{aligned}
&\sum_{C} p\left(C ; \theta^{(k)}\right) \sum_{i=1}^{n} \log p\left(x_{i}, C ; \theta\right)-n \sum_{C} p\left(C ; \theta^{(k)}\right) \log p\left(C ; \theta^{(k)}\right) \\
&\equiv Q\left(\theta \mid \theta^{(k)}\right)+H\left(P\left(C ; \theta^{(k)}\right)\right) \\
&\equiv F\left(p\left(C ; \theta^{(k)}\right), \theta\right)
\end{aligned}
$$
其中 $Q\left(\theta \mid \theta^{(k)}\right)$ 为 $\mathrm{EM}$ 算法中第 $k$ 轮不完全数据似然函数的后验条件期望, 即 $\mathrm{E}$ 步的计算结果。注意到 $H\left(P\left(C ; \theta^{(k)}\right)\right)$ 与参数 $\theta$ 无关, 于是 $\mathrm{EM}$ 算法的 $\mathrm{M}$ 步估计的参 数值为
$$
\theta^{(k+1)}=\arg \max _{\theta} Q\left(\theta \mid \theta^{(k)}\right)
$$
也就是说, 对参数 $\theta$ 的所有可能取值, 有
$$
Q\left(\theta^{(k+1)} \mid \theta^{(k)}\right) \geqslant Q\left(\theta \mid \theta^{(k)}\right)
$$
因此,
$$
Q\left(\theta^{(k+1)} \mid \theta^{(k)}\right) \geqslant Q\left(\theta^{(k)} \mid \theta^{(k)}\right)
$$

![[学习过程.png]]
EM算法一定是收敛的，但它不一定是全局最优的。

**take aways:**
EM算法常用来估计非监督学习模型中的参数。如果有多个高斯分布混合在一起，也可以通过EM算法分别估开多个高斯分布的参数，这个过程和K-Means算法非常相似。实际上，**K-Means算法是EM算法思想的体现，E步为聚类过程，M步为更新类簇中心**。不仅多个高斯混合可以利用EM算法进行求解，任意指数族分布的混合都可以运用EM算法进行求解。EM算法另外一类重要的应用是缺失值的处理，它是常用的缺失值填充技术。
EM算法**对模型初始值较为敏感**，初始化参数的选择直接影响收敛效率以及能否得
到全局最优解。为了克服这一缺点，应用中常常诹多次初始值，选择比较好的模型参数
估计。