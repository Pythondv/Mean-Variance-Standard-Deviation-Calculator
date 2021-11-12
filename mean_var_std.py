import numpy as np

def calculate(lst):
  if len(lst) == 9:
    arr = np.array(lst).reshape(3,3)
  elif len(lst) < 9:
    raise ValueError("List must contain nine numbers.")
  else:
    raise ValueError
  calculations = {
    'mean': [(np.mean(arr, axis=0)).tolist(), (np.mean(arr, axis=1)).tolist(), np.mean(lst).tolist()],
    'variance' : [(np.var(arr, axis=0)).tolist(), (np.var(arr, axis=1)).tolist(), np.var(lst).tolist()],
    "standard deviation" : [(np.std(arr, axis=0)).tolist(), (np.std(arr, axis=1)).tolist(), np.std(lst).tolist()],
    'max' : [(np.max(arr, axis=0)).tolist(), (np.max(arr, axis=1)).tolist(), np.max(lst).tolist()],
    'min' : [(np.min(arr, axis=0)).tolist(), (np.min(arr, axis=1)).tolist(), np.min(lst).tolist()],
    'sum' : [(np.sum(arr, axis=0)).tolist(), (np.sum(arr, axis=1)).tolist(), np.sum(lst).tolist()]
  }
  return calculations

print(calculate([0,1,2,3,4,5,6,7,8]))