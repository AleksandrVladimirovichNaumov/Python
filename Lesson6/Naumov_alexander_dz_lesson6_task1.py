# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]
#
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

import requests

# link to log data
log_link = "https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs"
# list for parsed data
log_list = []

# write all logs to nginx_logs.txt
log_txt = open(r'nginx_logs.txt', 'w', encoding='utf-8')
log_txt.write(requests.get(log_link).content.decode(encoding=requests.get(log_link).encoding))
log_txt.closed

# parsing logs lines and writing to nginx_logs_parsed.txt
log_txt = open(r'nginx_logs.txt', 'r', encoding='utf-8')
log_parsed_txt = open(r'nginx_logs_parsed.txt', 'w', encoding='utf-8')
for n in log_txt:
    line_parced = n.split(" ")
    line_parced = (line_parced[0], line_parced[5].replace('"', ''), line_parced[6])
    log_parsed_txt.write(f'{line_parced}\n')
log_txt.closed
log_parsed_txt.closed
