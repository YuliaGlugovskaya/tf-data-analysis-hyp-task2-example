#Вторая
import numpy as np
import pandas as pd
import scipy.stats as st

chat_id = 625123880 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
  pv = st.anderson_ksamp([x, y]).significance_level 
  if pv > 0.09:
    return False
  else:
    return True 
