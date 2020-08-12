import numpy as np

def calculate(list):
    
    if len(list) < 9:
      
        raise ValueError("List must contain nine numbers.")
           
    else:
    
        array_1 = np.array(list)
        array_1 = array_1.reshape(3,3)  
        
        
        calculations = dict.fromkeys(['mean', 'variance', 'standard deviation', 'max', 'min', 'sum'])
        
        calculations['mean'] = [np.mean(array_1,axis=0).tolist(),np.mean(array_1,axis=1).tolist(),np.mean(array_1)]
        calculations['variance'] = [np.var(array_1,axis=0).tolist(),np.var(array_1,axis=1).tolist(),np.var(array_1)]
        calculations['standard deviation'] = [np.std(array_1,axis=0).tolist(),np.std(array_1,axis=1).tolist(),np.std(array_1)]
        calculations['max'] = [np.max(array_1,axis=0).tolist(),np.max(array_1,axis=1).tolist(),np.max(array_1)]
        calculations['min'] = [np.min(array_1,axis=0).tolist(),np.min(array_1,axis=1).tolist(),np.min(array_1)]
        calculations['sum'] = [np.sum(array_1,axis=0).tolist(),np.sum(array_1,axis=1).tolist(),np.sum(array_1)]
        
        return calculations 