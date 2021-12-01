import time
import random
import concurrent.futures
from hashlib import md5

threads_count = int(input())
start_time = time.time()

def generate_coin():
    while True:
        s = "".join(random.choices("0123456789", k=50))
        h = md5(s.encode('utf8')).hexdigest()
        if h.endswith("00000"):
            return s, h

with concurrent.futures.ThreadPoolExecutor(threads_count) as executor:
    futures = [executor.submit(generate_coin) for i in range(4)]
    for future in concurrent.futures.as_completed(futures):
        print(*future.result())

end_time = time.time()
print(f"Время выполнения программы при параллельном выполнении {end_time - start_time} при {threads_count} тредов")
# Время выполнения программы при параллельном выполнении 25.375209093093872 при 2 тредов
# Время выполнения программы при параллельном выполнении 35.797523021698 при 4 тредов
# Время выполнения программы при параллельном выполнении 5.786075115203857 при 5 тредов
# Время выполнения программы при параллельном выполнении 20.78507161140442 при 10 тредов
# Время выполнения программы при параллельном выполнении 49.57002353668213 при 100 тредов