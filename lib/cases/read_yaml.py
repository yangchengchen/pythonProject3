"""
@Function:读取yaml文件内容为字典
"""
import yaml
with open('./cases.yaml',encoding='utf-8') as f:
    datas=yaml.safe_load(f)
print(datas)