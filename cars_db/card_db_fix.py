import json
import random

f = open(r"\\10.10.100.88\s\tg9\Pythоn-2 Май-июнь 2021\CarsDatabase\auto.json", 'r', encoding='utf-8')

d1 = json.load(f)
del d1['data']

f2 = open(r"C:\Users\student\Documents\Леонов\задачник\cars_db\auto.json", 'w', encoding='utf-8')
json.dump(d1, f2, ensure_ascii=False, indent=2)
f2.close()

print(len(d1['records']))

random.shuffle(d1['records'])
d2 = {'meta': d1['meta'], 'records': d1['records'][:100]}
d2['meta']['records'] = len(d2['records'])  # чило записей


f3 = open(r"C:\Users\student\Documents\Леонов\задачник\cars_db\auto_small.json", 'w', encoding='utf-8')
json.dump(d2, f3, ensure_ascii=False, indent=2)
f3.close()