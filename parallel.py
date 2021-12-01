import time
import concurrent.futures
from urllib.request import Request, urlopen

def check_correct_url(url):
    try:
        request = Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
        )
        resp = urlopen(request, timeout=5)
        code = resp.code
        print(code)
        resp.close()
    except Exception as e:
        print(url, e)

start_time = time.time()
threads_count = int(input())
with open('res.txt', "r", encoding='utf8') as f:
    links_array = f.readlines()
with concurrent.futures.ThreadPoolExecutor(threads_count) as executor:
    futures = [executor.submit(check_correct_url, url=url) for url in links_array]
    for future in concurrent.futures.as_completed(futures):
        future.result()
end_time = time.time()
print(f"Время выполнения программы при параллельном выполнении {end_time - start_time} при {threads_count} тредов")
# Время выполнения программы при параллельном выполнении 8.939356327056885 при 1 тредов (делал на 10 ссылках)
# Время выполнения программы при параллельном выполнении 3.6746127605438232 при 5 тредов (делал на 10 ссылках)
# Время выполнения программы при параллельном выполнении 3.5990450382232666 при 10 тредов (делал на 10 ссылках)
# Время выполнения программы при параллельном выполнении 3.601682662963867 при 100 тредов (делал на 10 ссылках)
# При увеличении количества тредов увеличивается нагрузка на процессор (пока количество тредов <= количества ядер)
