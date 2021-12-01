from hashlib import md5
from random import choice
import time

coins_count = 4
current_coin_number = 0
start_time = time.time()
while current_coin_number != coins_count:
    s = "".join([choice("0123456789") for i in range(50)])
    h = md5(s.encode('utf8')).hexdigest()

    if h.endswith("00000"):
        print(s, h)
        current_coin_number += 1
res_time = time.time() - start_time
end_time = time.time()
print(f"Время выполнения программы при синхронном выполнении {end_time - start_time}")
# Время выполнения программы при синхронном выполнении 14.20104193687439