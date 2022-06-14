import numpy as np

def calculate(list):
    if len(list) < 9:
         raise ValueError("List must contain nine numbers.")
        
    l = np.asarray(list)
    shape = (3,3)
    m = l.reshape(shape)
    n = m.flatten()
    calculations = {
            'mean': [np.mean(m,axis=0).tolist(), np.mean(m,axis=1).tolist(), np.mean(n).tolist()],
            'variance': [np.var(m,axis=0).tolist(), np.var(m,axis=1).tolist(), np.var(n).tolist()],
            'standard deviation': [np.std(m,axis=0).tolist(), np.std(m,axis=1).tolist(), np.std(n).tolist()],
            'max': [np.max(m,axis=0).tolist(), np.max(m,axis=1).tolist(), np.max(n).tolist()],
            'min': [np.min(m,axis=0).tolist(), np.min(m,axis=1).tolist(), np.min(n).tolist()],
            'sum': [np.sum(m,axis=0).tolist(), np.sum(m,axis=1).tolist(), np.sum(n).tolist()]
            }
    return calculations