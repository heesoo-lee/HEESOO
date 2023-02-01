import csv
import json
from datetime import datetime


data = []
with open('플랫폼별 주요 프로모션 출판사 레이블 명 ᄀ 660fba1474174dd9bd62720ba2b53df9.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    data = list(reader)
today = datetime.today()
with open(f'before_after_{today}.json', 'w') as json_file:
    json.dump(data, json_file, ensure_ascii=False)
