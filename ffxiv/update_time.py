import json
import time

# 读取 JSON 文件
with open('dalamudrepo.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 获取当前时间戳
current_timestamp = int(time.time())

# 更新每个插件的 LastUpdate 字段
for plugin in data:
    plugin["LastUpdate"] = current_timestamp

# 将更新后的数据保存回 JSON 文件
with open('dalamudrepo.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
