import yaml
with open('./yuanting.yaml',encoding='utf-8') as f:
    datas=yaml.safe_load(f)
print(datas)