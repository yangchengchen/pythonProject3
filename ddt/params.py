import yaml
# with open('./lib/cases/cases.yaml',encoding='utf-8') as f:
#     datas=yaml.safe_load(f)
# print(datas)
def workflow():
    with open('./lib/cases/yuanting.yaml',encoding='utf-8') as f:
        datas=yaml.safe_load(f)
    print(datas)
    return datas
def web():
    with open('./lib/cases/cases.yaml',encoding='utf-8') as f:
        datas=yaml.safe_load(f)
    print(datas)
    return datas