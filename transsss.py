import json

# 讀取 JSON 文件
with open('crossover.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 獲取需要排序的資料區塊
notes = data.get("notes", [])

# 按 offset 排序
sorted_notes = sorted(notes, key=lambda x: x.get("offset", 0))

# 更新原始數據結構
data["notes"] = sorted_notes

# 將排序結果寫入新文件
with open('crossover.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("排序完成，結果已存入 sorted_nighttheater.json")
