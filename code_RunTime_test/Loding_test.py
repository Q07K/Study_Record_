import numpy as np
import time
def time_delay(add_time=0):
    """
    시간 지연
    """
    seed = np.random.randint(100)
    np.random.seed(seed)
    a = np.random.randint(5)
    sum_time = a + add_time
    print(f'{((sum_time)) *"-"} 로딩중 {0}/{sum_time}', end='\r')
    for i in range(sum_time):
        print(f'{((sum_time)) *"-"} 로딩중 {i+1}/{sum_time}', end='\r')
        print(f'{(i+1) * ">"}', end='\r', flush=True)
        time.sleep(1)        