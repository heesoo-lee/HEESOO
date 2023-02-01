import json
from datetime import datetime

platform = '카카오페이지'
file_path = "KAKAOPAGE/kakao24test_2023-01-17_1(1-199).json"
notion_file_path = "before_after.json"

data = None
notion_data = None
platform_data = []
changed = []
unchanged = []
with open(file_path, 'r') as file:
    data = json.load(file)

with open(notion_file_path, 'r') as file:
    notion_data = json.load(file)

for i in range(len(notion_data)) :
    if notion_data[i]["﻿플랫폼"] == platform :
        platform_data.append(notion_data[i])
        

for i in range(len(data)) :
    unchanged.append(data[i])
    for x in range(len(platform_data)) :
        if data[i]['label'] == platform_data[x]['데이터 교정 전'] :
            data[i]['label'] = platform_data[x]['교정 후']
            print(f"{data[i]['title']} : {platform_data[x]['데이터 교정 전']} --> {platform_data[x]['교정 후']}")
            changed.append(data[i])
            unchanged.remove(data[i])

        elif data[i]['label'] == 'kwbooks' :
            data[i]['label'] = 'KW Books'
            print(f"{data[i]['title']} : kwbooks --> KW Books")
            changed.append(data[i])
            unchanged.remove(data[i])
        else :
            pass
    

today = datetime.today().strftime("%Y-%m-%d")  
with open(f'{platform}Crawling_Edit_Changed_{today}.json','w') as f:
    json.dump(changed, f, ensure_ascii=False, indent=4)

with open(f'{platform}Crawling_Edit_Unchanged_{today}.json','w') as f:
    json.dump(unchanged, f, ensure_ascii=False, indent=4)


