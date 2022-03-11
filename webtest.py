import re
import requests
import json

lv3_url = 'https://seantour.com/seantour_map/travel/'
# document.querySelector("head > script:nth-child(43)")

page_source = requests.get(lv3_url).text
print(page_source)
matched = re.search(r'var cources = (.*?);' ,page_source, re.S)
# json_string = matched.group(1)

course_list = json.loads(matched)
# for course in course_list:


