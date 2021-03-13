# 2.	*(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из
# предыдущего задания.

import requests

# link to log data
log_link = "https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs"

# list for parsed data
spammers = {}

list_of_top_spammers = []

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
    # completing dict with spammers
    if spammers.get(line_parced[0]) is None:
        spammers[line_parced[0]] = 1
    else:
        spammers[line_parced[0]] = spammers.get(line_parced[0]) + 1

log_txt.closed
log_parsed_txt.closed
# making dict with top spammers
list_of_top_spammers = {top_spammer: request_qnty for top_spammer, request_qnty in spammers.items() if
                        request_qnty == max(spammers.values())}

print(f"top spammer(s) with quantity of requests:\n{list_of_top_spammers}")
