import time
from urllib.request import Request, urlopen

start_time = time.time()
with open('res.txt', "r", encoding='utf8') as f:
    links_array = f.readlines()

for link in links_array:
    try:
        request = Request(
            link,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
        )
        resp = urlopen(request, timeout=5)
        code = resp.code
        print(code)
        resp.close()
    except Exception as e:
        print(link, e)
end_time = time.time()
print(f"Время выполнения программы при синхронном выполнении {end_time - start_time}")
#Время выполнения программы при синхронном выполнении 6.117567300796509 (делал на 10 ссылках)
