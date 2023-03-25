import json
with open("list.json","r",encoding="utf-8") as f:
  data=json.load(f)
with open("list.min.json","w+",encoding="utf-8") as f:
  json.dump(data,f, ensure_ascii=False)
