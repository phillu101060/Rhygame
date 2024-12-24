# RhyGame: 音樂節奏遊戲

**RhyGame** 是一款基於`pygame`開發的音樂節奏遊戲。玩家根據下落音符與音樂節奏進行互動，挑戰最高分與最佳評級！

---

## (1 )遊戲功能特點

1. **多首音樂可選**：
   - 包括 3 首音樂：`Db Doll`, `CROSSOVER`, `Night Theater`
   - 每首歌曲擁有專屬的譜面

2. **高精度節奏判定**：
   - 判定範圍分為 `Perfect`, `Good`, `Miss`，對應節奏點的誤差距離(±75ms,±125ms,+125~150ms或-125ms以下)
   
3. **結算與歷史記錄**：
   - 顯示當次遊玩分數（包括最大連擊 MaxCombo 和判定分佈）
   - 紀錄遊戲中每首歌的歷史最高分

---

## (2) 使用方式 

遵循以下步驟使用RhyGame:

### 1.安裝與設定

1. 安裝遊戲所需的依賴套件：

```bash

pip install pygame
pip install json

```

2. 確保RhyGame.py和resource在同一資料夾內

3. 戴上耳機以獲得最好體驗

### 2.開始遊戲

Here’s how to Start your game using RhyGame:

遊戲流程

1. (開始畫面)： 按下空白鍵開始遊戲
2. (進入選曲界面)： 預覽三首可選曲目，按上下箭頭選擇曲目，按空白鍵開始遊戲
3. (遊戲進行中)： 鍵盤按鍵對應：D, F, J, K 對應不同的下落軌道。根據節奏按下對應按鍵來擊中音符。按空白鍵直接進入結算界面
4. (結算界面)： 顯示分數、MaxCombo 、評級與詳細判定。按空白鍵返回選曲界面

## (3) 程式的架構 Program Architecture

The project is organized as follows:

```
RhyGame/
├── RhyGame.py                # 主程式碼
├── transsss.py               # 排序json
├── resource/
│   ├── image/                # 遊戲資源圖像
│   │   ├── 黑屏.png
│   │   ├── 選歌介面.png
│   │   └── ...
│   ├── sound/                # 音效資源
│   │   ├── perfect.mp3
│   │   ├── dbdoll.mp3
│   │   └── ...
│   └── judgement/            # 音符資料 JSON 文件
│       ├── dbdoll.json
│       ├── crossover.json
│       └── nighttheater.json
└── README.md                 # 遊戲說明文檔
```

## (4) 開發過程 

RhyGame 的開發經歷了以下階段，逐步構建並優化遊戲的核心功能與玩家體驗：

1. **概念與設計**: 確立核心遊戲概念，設計遊戲架構與規劃音樂及美術資源需求
2. **遊戲系統開發**: 建立音符系統與判定邏輯，設計遊戲介面
3. **測試與調試**: 測試遊戲流程與校準音符下落速度與判定範圍
4. **優化與增強**: 添加歷史分數保存功能與打擊特效，更改部分UI

## (5) 參考資料來源

1. bangbangboom editor(https://bbb-editor.pages.dev/#mapping)-用於編寫和整理歌曲的音符數據

2. 官方文檔(https://www.pygame.org/docs/ref/music.html)-基於 Pygame 的 pygame.mixer 函式庫開發

3. 使用 Python 和 PyGame 遊戲製作入門教學(https://blog.techbridge.cc/2019/10/19/how-to-build-up-game-with-pygame-tutorial/)-用於Pygame的初始設置

4. ChatGPT -修改load_notes_from_json函數，由原先讀取時間變成直接讀取json:

```

我想使用python 讀取這裡面的offset和lane
ChatGPT 說：
ChatGPT
看起來你的文件中包含大量的 "offset" 和 "lane" 的數據。如果你想用 Python 讀取它們，可以使用以下方法來解析這些 JSON 數據：

確認文件格式為 JSON，用 json 模組讀取文件。
訪問文件中的數據結構。文件中似乎有一個 "notes" 部分，每個條目包含 offset 和 lane。
以下是示範程式碼：

python
複製程式碼
import json

# 讀取 JSON 文件
with open('path/to/your/file.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 獲取 "notes" 中的 offset 和 lane
if "notes" in data:
    notes = data["notes"]
    offsets_and_lanes = [(note["offset"], note["lane"]) for note in notes if "offset" in note and "lane" in note]

    # 輸出結果
    for offset, lane in offsets_and_lanes:
        print(f"Offset: {offset}, Lane: {lane}")
else:
    print("找不到 'notes' 部分")
說明：
with open：
確保文件正常關閉。
json.load：
將 JSON 文件轉為 Python 資料結構（如字典）。
遍歷 notes：
確保每個 note 包含 offset 和 lane，並將其提取為二元組 (offset, lane)。
輸出結果：
遍歷輸出所有的偏移量和車道數據。
將其轉換為 DataFrame（可選）：
如果需要進一步分析數據，可以使用 pandas：

python
複製程式碼
import pandas as pd

# 將數據轉換為 DataFrame
df = pd.DataFrame(offsets_and_lanes, columns=["Offset", "Lane"])

# 輸出為 CSV（如果需要）
df.to_csv("output.csv", index=False)
print("數據已存為 CSV 文件")
你可以將上述程式碼根據具體需求進行調整。如果有任何進一步的需求，請告訴我！

你說：
Load Notes From File
我想將下方程式碼修改成剛剛的東西:
def load_notes_from_file(file_path, lane, key):
    global total_note
    notes = []
    try:
        with open(file_path, "r") as file:
            times = [float(line.strip())+offset for line in file if line.strip()]
            for time in times:
                total_note+=1
                notes.append({
                    "x": lane,
                    "y": note_start_y,
                    "target_time": time * 1000,
                    "generate_time": time * 1000 - advance_time_ms,
                    "key": key,
                    "active": False,
                    "end_time": time * 1000 - advance_time_ms 
                })
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    return notes

def notes_generate():
    global notes_d, notes_f, notes_j, notes_k, hold_notes_d, hold_notes_f, hold_notes_j, hold_notes_k
    notes_d, notes_f, notes_j, notes_k = [], [], [], []
    hold_notes_d, hold_notes_f, hold_notes_j, hold_notes_k = [], [], [], []
    music_files = {
        0: {
            "d": "resource/judgement/d_dbdoll.txt",
            "f": "resource/judgement//f_dbdoll.txt",
            "j": "resource/judgement/j_dbdoll.txt",
            "k": "resource/judgement/k_dbdoll.txt",
        },
        1: {
            "d": "resource/judgement/d_crossover.txt",
            "f": "resource/judgement//f_crossover.txt",
            "j": "resource/judgement/j_crossover.txt",
            "k": "resource/judgement/k_crossover.txt",
        },
        2: {
            "d": "resource/judgement/d_dbdoll.txt",
            "f": "resource/judgement//f_dbdoll.txt",
            "j": "resource/judgement/j_dbdoll.txt",
            "k": "resource/judgement/k_dbdoll.txt",
        }
    }
    selected_files = music_files.get(selected_music, {})
    notes_d = load_notes_from_file(selected_files.get("d", ""), lanes["D"], "D")
    notes_f = load_notes_from_file(selected_files.get("f", ""), lanes["F"], "F")
    notes_j = load_notes_from_file(selected_files.get("j", ""), lanes["J"], "J")
    notes_k = load_notes_from_file(selected_files.get("k", ""), lanes["K"], "K")

ChatGPT 說：
ChatGPT
下面是對你的程式進行修改，以讀取 JSON 文件中的 offset 和 lane 資料，並將其適配到原程式的框架中：

進行了 1 次編輯
我已將程式修改為可以讀取 JSON 文件中包含 offset 和 lane 的資料。現在，load_notes_from_json 函式會處理這些數據，並生成與你框架兼容的結構。如果需要進一步調整或解釋修改的邏輯，請告訴我！

你說：
請保留，其原本"D"對應到"lane"0，其原本"F"對應到"lane"2，其原本"J"對應到"lane"4，其原本"K"對應到"lane"6
ChatGPT 說：
import json

def load_notes_from_json(file_path):
    global total_note
    notes = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            # 假設 JSON 結構中的 "notes" 部分包含 offset 和 lane
            for note in data.get("notes", []):
                offset = note.get("offset", 0)
                lane = note.get("lane", 0)
                total_note += 1
                notes.append({
                    "x": lane,
                    "y": note_start_y,
                    "target_time": offset * 1000,  # 將 offset 視為秒，轉換為毫秒
                    "generate_time": offset * 1000 - advance_time_ms,
                    "key": None,  # 如果有需要可以增加鍵位映射
                    "active": False,
                    "end_time": offset * 1000 - advance_time_ms
                })
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to parse JSON in {file_path}.")
    return notes

def notes_generate():
    global notes_d, notes_f, notes_j, notes_k, hold_notes_d, hold_notes_f, hold_notes_j, hold_notes_k
    notes_d, notes_f, notes_j, notes_k = [], [], [], []
    hold_notes_d, hold_notes_f, hold_notes_j, hold_notes_k = [], [], [], []
    music_files = {
        0: {
            "d": "resource/judgement/d_dbdoll.json",
            "f": "resource/judgement/f_dbdoll.json",
            "j": "resource/judgement/j_dbdoll.json",
            "k": "resource/judgement/k_dbdoll.json",
        },
        1: {
            "d": "resource/judgement/d_crossover.json",
            "f": "resource/judgement/f_crossover.json",
            "j": "resource/judgement/j_crossover.json",
            "k": "resource/judgement/k_crossover.json",
        },
        2: {
            "d": "resource/judgement/d_dbdoll.json",
            "f": "resource/judgement/f_dbdoll.json",
            "j": "resource/judgement/j_dbdoll.json",
            "k": "resource/judgement/k_dbdoll.json",
        }
    }
    selected_files = music_files.get(selected_music, {})
    notes_d = load_notes_from_json(selected_files.get("d", ""))
    notes_f = load_notes_from_json(selected_files.get("f", ""))
    notes_j = load_notes_from_json(selected_files.get("j", ""))
    notes_k = load_notes_from_json(selected_files.get("k", ""))

ChatGPT
我們需要根據你提供的要求，將 "D", "F", "J", 和 "K" 分別與 lane 的 0、2、4 和 6 綁定。以下是針對你的程式進一步的修改：

在 load_notes_from_json 函式中，根據文件對應到的鍵，篩選與其對應的 lane。
每個鍵只處理屬於它的 lane 資料。
進行了 1 次編輯
已經將程式更新，使每個鍵 ("D", "F", "J", "K") 對應到特定的 lane 值 (分別為 0, 2, 4, 6)。這確保每個鍵只會處理匹配的車道資料。如果還需要進一步調整或有其他需求，請告訴我！

你說：
標籤"key"為原本的DFJK
ChatGPT 說：
import json

def load_notes_from_json(file_path, expected_lane):
    global total_note
    notes = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            # 假設 JSON 結構中的 "notes" 部分包含 offset 和 lane
            for note in data.get("notes", []):
                offset = note.get("offset", 0)
                lane = note.get("lane", 0)
                if lane == expected_lane:  # 只處理與期望 lane 匹配的資料
                    total_note += 1
                    notes.append({
                        "x": lane,
                        "y": note_start_y,
                        "target_time": offset * 1000,  # 將 offset 視為秒，轉換為毫秒
                        "generate_time": offset * 1000 - advance_time_ms,
                        "key": None,  # 如果有需要可以增加鍵位映射
                        "active": False,
                        "end_time": offset * 1000 - advance_time_ms
                    })
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to parse JSON in {file_path}.")
    return notes

def notes_generate():
    global notes_d, notes_f, notes_j, notes_k, hold_notes_d, hold_notes_f, hold_notes_j, hold_notes_k
    notes_d, notes_f, notes_j, notes_k = [], [], [], []
    hold_notes_d, hold_notes_f, hold_notes_j, hold_notes_k = [], [], [], []
    music_files = {
        0: {
            "d": "resource/judgement/d_dbdoll.json",
            "f": "resource/judgement/f_dbdoll.json",
            "j": "resource/judgement/j_dbdoll.json",
            "k": "resource/judgement/k_dbdoll.json",
        },
        1: {
            "d": "resource/judgement/d_crossover.json",
            "f": "resource/judgement/f_crossover.json",
            "j": "resource/judgement/j_crossover.json",
            "k": "resource/judgement/k_crossover.json",
        },
        2: {
            "d": "resource/judgement/d_dbdoll.json",
            "f": "resource/judgement/f_dbdoll.json",
            "j": "resource/judgement/j_dbdoll.json",
            "k": "resource/judgement/k_dbdoll.json",
        }
    }
    selected_files = music_files.get(selected_music, {})
    notes_d = load_notes_from_json(selected_files.get("d", ""), 0)  # D 對應 lane 0
    notes_f = load_notes_from_json(selected_files.get("f", ""), 2)  # F 對應 lane 2
    notes_j = load_notes_from_json(selected_files.get("j", ""), 4)  # J 對應 lane 4
    notes_k = load_notes_from_json(selected_files.get("k", ""), 6)  # K 對應 lane 6

ChatGPT
進行了 1 次編輯
我已更新程式碼，將每個鍵 "D", "F", "J", "K" 與對應的 lane 綁定，並將標籤 "key" 更新為其鍵位的字母值 ("D", "F", "J", "K")。如果有其他需求或修改，隨時告訴我！

你說：
我得json檔案只有一個，我要讀取裡面的offset和lane 
ChatGPT 說：
import json

def load_notes_from_json(file_path, expected_lane, key_label):
    global total_note
    notes = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            # 假設 JSON 結構中的 "notes" 部分包含 offset 和 lane
            for note in data.get("notes", []):
                offset = note.get("offset", 0)
                lane = note.get("lane", 0)
                if lane == expected_lane:  # 只處理與期望 lane 匹配的資料
                    total_note += 1
                    notes.append({
                        "x": lane,
                        "y": note_start_y,
                        "target_time": offset * 1000,  # 將 offset 視為秒，轉換為毫秒
                        "generate_time": offset * 1000 - advance_time_ms,
                        "key": key_label,  # 標記為對應的鍵
                        "active": False,
                        "end_time": offset * 1000 - advance_time_ms
                    })
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to parse JSON in {file_path}.")
    return notes

def notes_generate():
    global notes_d, notes_f, notes_j, notes_k, hold_notes_d, hold_notes_f, hold_notes_j, hold_notes_k
    notes_d, notes_f, notes_j, notes_k = [], [], [], []
    hold_notes_d, hold_notes_f, hold_notes_j, hold_notes_k = [], [], [], []
    music_files = {
        0: {
            "d": "resource/judgement/d_dbdoll.json",
            "f": "resource/judgement/f_dbdoll.json",
            "j": "resource/judgement/j_dbdoll.json",
            "k": "resource/judgement/k_dbdoll.json",
        },
        1: {
            "d": "resource/judgement/d_crossover.json",
            "f": "resource/judgement/f_crossover.json",
            "j": "resource/judgement/j_crossover.json",
            "k": "resource/judgement/k_crossover.json",
        },
        2: {
            "d": "resource/judgement/d_dbdoll.json",
            "f": "resource/judgement/f_dbdoll.json",
            "j": "resource/judgement/j_dbdoll.json",
            "k": "resource/judgement/k_dbdoll.json",
        }
    }
    selected_files = music_files.get(selected_music, {})
    notes_d = load_notes_from_json(selected_files.get("d", ""), 0, "D")  # D 對應 lane 0
    notes_f = load_notes_from_json(selected_files.get("f", ""), 2, "F")  # F 對應 lane 2
    notes_j = load_notes_from_json(selected_files.get("j", ""), 4, "J")  # J 對應 lane 4
    notes_k = load_notes_from_json(selected_files.get("k", ""), 6, "K")  # K 對應 lane 6

ChatGPT
如果你只有一個 JSON 文件，而非分開的多個文件，那麼可以簡化並修改程式，只需要讀取一個文件並根據 lane 值將資料分配到正確的列表。以下是修改過的程式碼：

進行了 1 次編輯
現在程式已經簡化為只讀取一個 JSON 文件，並根據 lane 值自動將資料分配到 notes_d, notes_f, notes_j, 和 notes_k 中，並正確標記其對應的鍵 ("D", "F", "J", "K")。如果還有其他需求，隨時告訴我！

你說：
  "x": lane,這裡lanes_x = {"0": 0,"2": 127,"4": 254,"6": 381}
ChatGPT 說：
import json

def load_notes_from_json(file_path):
    global total_note
    global notes_d, notes_f, notes_j, notes_k

    notes_d, notes_f, notes_j, notes_k = [], [], [], []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            # 假設 JSON 結構中的 "notes" 部分包含 offset 和 lane
            for note in data.get("notes", []):
                offset = note.get("offset", 0)
                lane = note.get("lane", 0)
                total_note += 1

                note_data = {
                    "x": lane,
                    "y": note_start_y,
                    "target_time": offset * 1000,  # 將 offset 視為秒，轉換為毫秒
                    "generate_time": offset * 1000 - advance_time_ms,
                    "active": False,
                    "end_time": offset * 1000 - advance_time_ms
                }

                if lane == 0:
                    note_data["key"] = "D"
                    notes_d.append(note_data)
                elif lane == 2:
                    note_data["key"] = "F"
                    notes_f.append(note_data)
                elif lane == 4:
                    note_data["key"] = "J"
                    notes_j.append(note_data)
                elif lane == 6:
                    note_data["key"] = "K"
                    notes_k.append(note_data)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to parse JSON in {file_path}.")

def notes_generate():
    global notes_d, notes_f, notes_j, notes_k, hold_notes_d, hold_notes_f, hold_notes_j, hold_notes_k
    notes_d, notes_f, notes_j, notes_k = [], [], [], []
    hold_notes_d, hold_notes_f, hold_notes_j, hold_notes_k = [], [], [], []

    # 指定唯一的 JSON 文件
    file_path = "resource/judgement/notes.json"
    load_notes_from_json(file_path)

ChatGPT
你希望將 note_data["x"] 中的 lane 值轉換為 lanes_x 提供的實際數值。我將更新程式碼，添加一個 lanes_x 字典，並使用它來對應 lane 到具體的座標值。以下是更新的程式：

進行了 1 次編輯
程式碼已更新，加入了 lanes_x 字典來映射 lane 值到對應的 x 座標 (例如：0 對應 0，2 對應 127 等)。更新後，x 的值會自動基於 lane 轉換為對應座標。如果有進一步修改需求，請告訴我！

你說：
def load_notes_from_json(file_path):
    global total_note
    global notes_d, notes_f, notes_j, notes_k

    notes_d, notes_f, notes_j, notes_k = [], [], [], []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            lanes_x = {"0": 0, "2": 127, "4": 254, "6": 381}  # 定義 lane 對應的 x 座標
            # 假設 JSON 結構中的 "notes" 部分包含 offset_in_music 和 lane
            for note in data.get("notes", []):
                offset_in_note = note.get("offset", 0)*(1.25/bpm)+3.1
                
                lane=str(note.get("lane", 0))         
                total_note += 1
                note_data = {
                    "x": lanes_x.get("lane", 0),
                    "y": note_start_y,
                    "target_time": offset_in_note * 1000+offset_in_music,  # 將 offset_in_music 視為秒，轉換為毫秒
                    "generate_time": offset_in_note *  1000 +offset_in_music- advance_time_ms,
                    "active": False,
                    "end_time": offset_in_note * 1000 +offset_in_music- advance_time_ms
                }

                if lane == 0:
                    note_data["key"] = "D"
                    notes_d.append(note_data)
                elif lane == 2:
                    note_data["key"] = "F"
                    notes_f.append(note_data)
                elif lane == 4:
                    note_data["key"] = "J"
                    notes_j.append(note_data)
                elif lane == 6:
                    note_data["key"] = "K"
                    notes_k.append(note_data)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to parse JSON in {file_path}.")

def notes_generate():
    global notes_d, notes_f, notes_j, notes_k, hold_notes_d, hold_notes_f, hold_notes_j, hold_notes_k
    notes_d, notes_f, notes_j, notes_k = [], [], [], []
    hold_notes_d, hold_notes_f, hold_notes_j, hold_notes_k = [], [], [], []

    # 指定唯一的 JSON 文件
    file_path = "resource/judgement/notes.json"
    load_notes_from_json(file_path)
ChatGPT 說：
import json

def load_notes_from_json(file_path):
    global total_note
    global notes_d, notes_f, notes_j, notes_k

    notes_d, notes_f, notes_j, notes_k = [], [], [], []
    lanes_x = {"0": 0, "2": 127, "4": 254, "6": 381}  # 定義 lane 對應的 x 座標

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            # 假設 JSON 結構中的 "notes" 部分包含 offset 和 lane
            for note in data.get("notes", []):
                offset = note.get("offset", 0)
                lane = str(note.get("lane", 0))  # 確保鍵是字符串形式，與 lanes_x 匹配
                total_note += 1

                note_data = {
                    "x": lanes_x.get(lane, 0),  # 根據 lanes_x 映射 lane 值
                    "y": note_start_y,
                    "target_time": offset * 1000,  # 將 offset 視為秒，轉換為毫秒
                    "generate_time": offset * 1000 - advance_time_ms,
                    "active": False,
                    "end_time": offset * 1000 - advance_time_ms
                }

                if lane == "0":
                    note_data["key"] = "D"
                    notes_d.append(note_data)
                elif lane == "2":
                    note_data["key"] = "F"
                    notes_f.append(note_data)
                elif lane == "4":
                    note_data["key"] = "J"
                    notes_j.append(note_data)
                elif lane == "6":
                    note_data["key"] = "K"
                    notes_k.append(note_data)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to parse JSON in {file_path}.")

def notes_generate():
    global notes_d, notes_f, notes_j, notes_k, hold_notes_d, hold_notes_f, hold_notes_j, hold_notes_k
    notes_d, notes_f, notes_j, notes_k = [], [], [], []
    hold_notes_d, hold_notes_f, hold_notes_j, hold_notes_k = [], [], [], []

    # 指定唯一的 JSON 文件
    file_path = "resource/judgement/notes.json"
    load_notes_from_json(file_path)

ChatGPT
看起來你的要求是：

使用 offset_in_note 計算偏移時間：計算的方式基於 (1.25 / bpm) + 3.1，並且考慮到可能存在的 offset_in_music。
修正 x 對應的 Lane 映射：x 應根據 lanes_x 對應的值來映射，而不是直接用 "lane"。
處理 Lane 的字符串和數字問題：確保以一致的形式來進行匹配。
以下是整合這些修訂後的程式版本：

Load Notes From File
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
import json

def load_notes_from_json(file_path):
    global total_note
    global notes_d, notes_f, notes_j, notes_k

    notes_d, notes_f, notes_j, notes_k = [], [], [], []
    lanes_x = {"0": 0, "2": 127, "4": 254, "6": 381}  # 定義 lane 對應的 x 座標

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            # 假設 JSON 結構中的 "notes" 部分包含 offset 和 lane
            for note in data.get("notes", []):
                offset_in_note = note.get("offset", 0) * (1.25 / bpm) + 3.1
                lane = str(note.get("lane", 0))  # 確保鍵是字符串形式，與 lanes_x 匹配
                total_note += 1

                note_data = {
                    "x": lanes_x.get(lane, 0),  # 根據 lanes_x 映射 lane 值
                    "y": note_start_y,
                    "target_time": offset_in_note * 1000 + offset_in_music,  # 計算最終目標時間
                    "generate_time": offset_in_note * 1000 + offset_in_music - advance_time_ms,
                    "active": False,
                    "end_time": offset_in_note * 1000 + offset_in_music - advance_time_ms
                }

                if lane == "0":
                    note_data["key"] = "D"
                    notes_d.append(note_data)
                elif lane == "2":
                    note_data["key"] = "F"
                    notes_f.append(note_data)
                elif lane == "4":
                    note_data["key"] = "J"
                    notes_j.append(note_data)
                elif lane == "6":
                    note_data["key"] = "K"
                    notes_k.append(note_data)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to parse JSON in {file_path}.")

def notes_generate():
    global notes_d, notes_f, notes_j, notes_k, hold_notes_d, hold_notes_f, hold_notes_j, hold_notes_k
    notes_d, notes_f, notes_j, notes_k = [], [], [], []
    hold_notes_d, hold_notes_f, hold_notes_j, hold_notes_k = [], [], [], []

    # 指定唯一的 JSON 文件
    file_path = "resource/judgement/notes.json"
    load_notes_from_json(file_path)

進行了 1 次編輯
程式已更新，並實現以下修正：
import json

def load_notes_from_json(file_path):
    global total_note
    global notes_d, notes_f, notes_j, notes_k

    notes_d, notes_f, notes_j, notes_k = [], [], [], []
    lanes_x = {"0": 0, "2": 127, "4": 254, "6": 381}  # 定義 lane 對應的 x 座標

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            # 假設 JSON 結構中的 "notes" 部分包含 offset 和 lane
            for note in data.get("notes", []):
                offset_in_note = note.get("offset", 0) * (1.25 / bpm) + 3.1
                lane = str(note.get("lane", 0))  # 確保鍵是字符串形式，與 lanes_x 匹配
                total_note += 1

                note_data = {
                    "x": lanes_x.get(lane, 0),  # 根據 lanes_x 映射 lane 值
                    "y": note_start_y,
                    "target_time": offset_in_note * 1000 + offset_in_music,  # 計算最終目標時間
                    "generate_time": offset_in_note * 1000 + offset_in_music - advance_time_ms,
                    "active": False,
                    "end_time": offset_in_note * 1000 + offset_in_music - advance_time_ms
                }

                if lane == "0":
                    note_data["key"] = "D"
                    notes_d.append(note_data)
                elif lane == "2":
                    note_data["key"] = "F"
                    notes_f.append(note_data)
                elif lane == "4":
                    note_data["key"] = "J"
                    notes_j.append(note_data)
                elif lane == "6":
                    note_data["key"] = "K"
                    notes_k.append(note_data)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to parse JSON in {file_path}.")

def notes_generate():
    global notes_d, notes_f, notes_j, notes_k, hold_notes_d, hold_notes_f, hold_notes_j, hold_notes_k
    notes_d, notes_f, notes_j, notes_k = [], [], [], []
    hold_notes_d, hold_notes_f, hold_notes_j, hold_notes_k = [], [], [], []

    # 指定唯一的 JSON 文件
    file_path = "resource/judgement/notes.json"
    load_notes_from_json(file_path)

使用 offset_in_note 計算，包含 (1.25 / bpm) + 3.1 的公式。
正確映射 lane 值到 lanes_x 中對應的 x 座標。
確保對應的鍵 (D, F, J, K) 根據 lane 值正確分配。
如果還需要其他調整，請隨時告訴我！

```

5. ChatGPT-將offset順序不對的json重新以小到大排列，生成transsss.py:

```
如何讓json裡面的內容依數值大小排序，例如"offset","30","offset","10","offset","20"變為"offset","10","offset","20","offset","30",
ChatGPT 說：
ChatGPT
要將 JSON 中的數據按數值大小排序，可以使用程式來處理。以下是 Python 的解法，示範如何根據 key 和數值對 JSON 進行排序。

假設原始 JSON 是這樣的結構：

json
複製程式碼
[
    {"offset": 30},
    {"offset": 10},
    {"offset": 20}
]
以下是排序的範例程式碼：

Python 程式
python
複製程式碼
import json

# 原始資料
data = [
    {"offset": 30},
    {"offset": 10},
    {"offset": 20}
]

# 按照 'offset' 數值排序
sorted_data = sorted(data, key=lambda x: x['offset'])

# 排序後的結果
print(json.dumps(sorted_data, indent=4))
輸出結果
json
複製程式碼
[
    {
        "offset": 10
    },
    {
        "offset": 20
    },
    {
        "offset": 30
    }
]
如果你的 JSON 結構更複雜，請具體告知結構，這樣可以提供更精準的解法。

你說：
nighttheater.json
檔案
要將其中offset以小到大排序
ChatGPT
根據提供的 JSON 文件片段，其中包含多個 offset 欄位數值在物件內。要對 offset 進行排序（由小到大），可以使用 Python 腳本來實現。以下是解法步驟與範例程式碼：

Python 腳本
解析 JSON 文件。
按照 offset 值進行排序。
輸出排序後的 JSON 結果。
程式碼範例
python
複製程式碼
import json

# 讀取 JSON 文件
with open('nighttheater.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 獲取需要排序的資料區塊
notes = data.get("notes", [])

# 按 offset 排序
sorted_notes = sorted(notes, key=lambda x: x.get("offset", 0))

# 更新原始數據結構
data["notes"] = sorted_notes

# 將排序結果寫入新文件
with open('sorted_nighttheater.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("排序完成，結果已存入 sorted_nighttheater.json")
解釋
讀取與解析 JSON 文件：透過 json.load 方法加載數據。
提取數據進行排序：對 notes 內的物件，依照 offset 欄位進行升序排序，使用 sorted 函數和 lambda 運算子。
輸出排序結果：將結果重新寫回新的 JSON 文件中。
如果執行此腳本，notes 中的項目會按 offset 由小到大排列。需要任何其他調整，歡迎告知！
```

## (6) 程式修改或增強的內容

1. 由CGPT修改load_notes_from_json和notes_generate函數，由原先自己寫的讀取時間變成直接讀取json，並更改offset_in_notes的公式:

原始:
```
def load_notes_from_file(file_path, lane, key):
    global total_note
    notes = []
    try:
        with open(file_path, "r") as file:
            times = [float(line.strip())+3.0 for line in file if line.strip()]
            for time in times:
                total_note+=1
                notes.append({
                    "x": lane,
                    "y": note_start_y,
                    "target_time": time * 1000,
                    "generate_time": time * 1000 - advance_time_ms,
                    "key": key,
                    "active": False,
                    "end_time": time * 1000 - advance_time_ms 
                })
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    return notes

def notes_generate():
    global notes_d, notes_f, notes_j, notes_k, hold_notes_d, hold_notes_f, hold_notes_j, hold_notes_k
    notes_d, notes_f, notes_j, notes_k = [], [], [], []
    hold_notes_d, hold_notes_f, hold_notes_j, hold_notes_k = [], [], [], []
    music_files = {
        0: {
            "d": "resource/judgement/d_dbdoll.txt",
            "f": "resource/judgement//f_dbdoll.txt",
            "j": "resource/judgement/j_dbdoll.txt",
            "k": "resource/judgement/k_dbdoll.txt",
        },
        1: {
            "d": "resource/judgement/d_crossover.txt",
            "f": "resource/judgement//f_crossover.txt",
            "j": "resource/judgement/j_crossover.txt",
            "k": "resource/judgement/k_crossover.txt",
        },
        2: {
            "d": "resource/judgement/d_dbdoll.txt",
            "f": "resource/judgement//f_dbdoll.txt",
            "j": "resource/judgement/j_dbdoll.txt",
            "k": "resource/judgement/k_dbdoll.txt",
        }
    }
    selected_files = music_files.get(selected_music, {})
    notes_d = load_notes_from_file(selected_files.get("d", ""), lanes["D"], "D")
    notes_f = load_notes_from_file(selected_files.get("f", ""), lanes["F"], "F")
    notes_j = load_notes_from_file(selected_files.get("j", ""), lanes["J"], "J")
    notes_k = load_notes_from_file(selected_files.get("k", ""), lanes["K"], "K")

```
修改後:
```
def load_notes_from_json(file_path):
    global total_note
    global notes_d, notes_f, notes_j, notes_k

    notes_d, notes_f, notes_j, notes_k = [], [], [], []
    lanes_x = {"0": 0, "2": 127, "4": 254, "6": 381}  # 定義 lane 對應的 x 座標

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            # 假設 JSON 結構中的 "notes" 部分包含 offset 和 lane
            for note in data.get("notes", []):
                offset_in_note = note.get("offset", 0) * (1.25 / bpm) + offset_note
                lane = str(note.get("lane", 0))  # 確保鍵是字符串形式，與 lanes_x 匹配
                total_note += 1
                note_data = {
                    "x": lanes_x.get(lane, 0),  # 根據 lanes_x 映射 lane 值
                    "y": note_start_y,
                    "target_time": (offset_in_note + offset_start )* 1000,  # 計算最終目標時間
                    "generate_time":(offset_in_note + offset_start )* 1000 - advance_time_ms,
                    "active": False,
                    "end_time": (offset_in_note + offset_start )* 1000 - advance_time_ms
                }

                if lane == "0":
                    note_data["key"] = "D"
                    notes_d.append(note_data)
                elif lane == "2":
                    note_data["key"] = "F"
                    notes_f.append(note_data)
                elif lane == "4":
                    note_data["key"] = "J"
                    notes_j.append(note_data)
                elif lane == "6":
                    note_data["key"] = "K"
                    notes_k.append(note_data)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except json.JSONDecodeError:
def notes_generate():
    global notes_d, notes_f, notes_j, notes_k, hold_notes_d, hold_notes_f, hold_notes_j, hold_notes_k
    notes_d, notes_f, notes_j, notes_k = [], [], [], []
    hold_notes_d, hold_notes_f, hold_notes_j, hold_notes_k = [], [], [], []

    if selected_music==0:
        file_path = "resource/judgement/dbdoll.json"
        load_notes_from_json(file_path)
    if selected_music==1:
        file_path = "resource/judgement/crossover.json"
        load_notes_from_json(file_path)
    if selected_music==2:
        file_path = "resource/judgement/nighttheater.json"
```
   
2. Pygame的初始設置:

由參考資料第三點
```
import sys

import pygame
from pygame.locals import QUIT

# 初始化
pygame.init()
# 建立 window 視窗畫布，大小為 800x600
window_surface = pygame.display.set_mode((800, 600))
# 設置視窗標題為 Hello World:)
pygame.display.set_caption('Hello World:)')
# 清除畫面並填滿背景色
window_surface.fill((255, 255, 255))

# 宣告 font 文字物件
head_font = pygame.font.SysFont(None, 60)
# 渲染方法會回傳 surface 物件
text_surface = head_font.render('Hello World!', True, (0, 0, 0))
# blit 用來把其他元素渲染到另外一個 surface 上，這邊是 window 視窗
window_surface.blit(text_surface, (10, 10))

```
改為
```
import pygame
import json

# 初始化
pygame.init()
pygame.display.set_caption("RhyGame")
pygame.key.stop_text_input()
screen = pygame.display.set_mode((800, 600)) 
font = pygame.font.SysFont('agencyfb', 48,bold=False,italic=False)
clock = pygame.time.Clock()
running = True

```

3. 自己貢獻:選歌函數、結算函數、判定邏輯與特效、音符掉落函數、分數與連擊數計算邏輯、歷史紀錄、原始的譜面載入方式(就是除了上面兩點外的其他東西)

We encourage further modifications and look forward to community contributions to improve RhyGame further.
This README was made by ChatGPT.
