#Вторая
import numpy as np
import pandas as pd
import scipy.stats as st

chat_id = 625123880 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
  pv = st.cramervonmises_2samp(x, y)[1]
  print(pv)
  if pv > 0.09:
    return False
  else:
    return True 
