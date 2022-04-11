import numpy as np 


def momento(v, x, n=0):

    x_mean = np.mean(x, 0, keepdims=True)
    b = x - x_mean
    
    N = x.shape[0]

    mu = [ ]

    for i in range(N):
        
        bn = np.array(1)
        
        vi = v[i, None]        
        bi = b[i, None]

        for j in range(n):
            bn = np.outer(bi, bn)

        m = vi*bn
        mu.append(m)

    mu = np.array(mu)
    mu = np.sum(mu, 0)

    return mu 