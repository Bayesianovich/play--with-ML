# 该函数每次返回大小为Batch_size的批量
# x和y分别为输入和标签
#若shuffle = True,则每次遍历时会将数据重新随机划分
def batch_generator(x, y, batch_size, shuffle=True):
    """
    Generate batches of data from input arrays x and y.

    Parameters:
    x (ndarray): Input array of features.
    y (ndarray): Input array of labels.
    batch_size (int): Size of each batch.
    shuffle (bool, optional): Whether to shuffle the data. Defaults to True.

    Yields:
    tuple: A tuple containing the batch of features and labels.

    """
    counter = 0
    if shuffle:
        indices = np.arange(len(x))
        np.random.shuffle(indices)
        x = x[indices]
        y = y[indices]
        
    while True:
        start = batch_size * counter
        end = min(start + batch_size, len(x))
        if start >= end:
            break
        counter += 1
        yield x[start:end], y[start:end]
