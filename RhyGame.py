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

# 加載圖像與音效
blackimg = pygame.image.load('resource/image/黑屏.png')
music_choose = pygame.image.load('resource/image/選歌介面.png')
choosen = pygame.image.load('resource/image/指示選歌.png')
music1_draw = pygame.image.load('resource/image/music1_draw.jpg')
music2_draw = pygame.image.load('resource/image/music2_draw.jpg')
music3_draw = pygame.image.load('resource/image/music3_draw.png')
track = pygame.image.load('resource/image/軌道.png')  
ending = pygame.image.load('resource/image/結算畫面.png')
rank_F = pygame.image.load('resource/image/評級F.png')
rank_Cm = pygame.image.load('resource/image/評級C-.png')
rank_C = pygame.image.load('resource/image/評級C.png')
rank_Cp = pygame.image.load('resource/image/評級C+.png')
rank_Bm= pygame.image.load('resource/image/評級B-.png')
rank_B = pygame.image.load('resource/image/評級B.png')
rank_Bp = pygame.image.load('resource/image/評級B+.png')
rank_Am = pygame.image.load('resource/image/評級A-.png')
rank_A = pygame.image.load('resource/image/評級A.png')
rank_Ap = pygame.image.load('resource/image/評級A+.png')
rank_S = pygame.image.load('resource/image/評級S.png')
rank_P = pygame.image.load('resource/image/評級P.png')
rank_X = pygame.image.load('resource/image/評級X.png')
judge_line = pygame.image.load('resource/image/判定線.png')
game_background = pygame.image.load('resource/image/遊戲背景.png')
note_img = pygame.image.load('resource/image/音符.png')
hold_img = pygame.image.load('resource/image/長壓.png')
perfect_hit_img = pygame.image.load('resource/image/perfect擊.png').convert_alpha()
good_hit_img = pygame.image.load('resource/image/good擊.png').convert_alpha()
miss_hit_img = pygame.image.load('resource/image/miss擊.png').convert_alpha()
no_hit_img = pygame.image.load('resource/image/空擊.png').convert_alpha()
choose_music_background = pygame.image.load('resource/image/選歌背景.png')
start_music_background = pygame.image.load('resource/image/開始背景.png')
music1_draw = pygame.transform.scale(music1_draw , (350, 350))
music2_draw = pygame.transform.scale(music2_draw , (350, 350))
music3_draw = pygame.transform.scale(music3_draw , (350, 350))
try:
    pygame.mixer.init()
    perfect_hit = pygame.mixer.Sound('resource/sound/perfect.mp3')
    good_hit = pygame.mixer.Sound('resource/sound/good.mp3')
    miss_hit = pygame.mixer.Sound('resource/sound/miss.mp3')
    dbdoll_music = pygame.mixer.Sound('resource/sound/dbdoll.mp3')
    crossover_music = pygame.mixer.Sound('resource/sound/CROSSOVER.mp3')
    nighttheater_music = pygame.mixer.Sound('resource/sound/NightTheater.mp3')
    R_dbdoll_music = pygame.mixer.Sound('resource/sound/R_dbdoll.mp3')
    R_crossover_music = pygame.mixer.Sound('resource/sound/R_CROSSOVER.mp3')
    R_nighttheater_music = pygame.mixer.Sound('resource/sound/R_NightTheater.mp3')
    start_music = pygame.mixer.Sound('resource/sound/start.mp3')
    ending_music = pygame.mixer.Sound('resource/sound/ending.mp3')
    space_music = pygame.mixer.Sound('resource/sound/space_tap.mp3')
    start_music.set_volume(0.05)
    ending_music.set_volume(0.05)
    space_music.set_volume(0.05)
    R_nighttheater_music.set_volume(0.05)
    R_crossover_music.set_volume(0.05)
    R_dbdoll_music.set_volume(0.05)
    nighttheater_music.set_volume(0.05)
    crossover_music.set_volume(0.05)
    dbdoll_music.set_volume(0.05)
    perfect_hit.set_volume(0.05)
    good_hit.set_volume(0.05)
    miss_hit.set_volume(0.05)
    mixer_ready=True
except:
    mixer_ready=False
    pass

#一堆東西
music_played = False
stage = 0
selected_music = 0
channel=0
times=0
start_time = pygame.time.get_ticks()  
note_active = True  
judge_line_y = 485
effect_duration = 200  
note_speed = 22.5#60/15
target_time = 0
time_tolerance = 75
notes_start_x = 0
note_start_y = -25
offset_start=0
offset_note=0
bpm=0
advance_time_ms = float((judge_line_y - note_start_y) / (note_speed*45) * 1000)  
lanes = {"D": 0,"F": 127,"J": 254,"K": 381}
notes_d = []
notes_f = []
notes_j = []
notes_k = []
hold_notes_d = []
hold_notes_f = []
hold_notes_j = []
hold_notes_k = []
perfect_effects = []  
good_effects = []  
miss_effects = []  
perfect_effect_rect = perfect_hit_img.get_rect()
good_effect_rect = good_hit_img.get_rect()
miss_effect_rect = miss_hit_img.get_rect()
perfect=0
good=0
miss=0
combo=0
maxcombo=0
score=0
total_note=0
music_len=0
music1_high_score=0
music2_high_score=0
music3_high_score=0

def start():  # ST0
    global channel,times
    if mixer_ready==True:
        channel=pygame.mixer.Channel(5)
        if not channel.get_busy():
            channel.play(start_music,fade_ms=500)
 
           
    if times==0:
        screen.blit(blackimg, (0, 0))
        pygame.display.flip()
        start_time_wait = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start_time_wait < 1800:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()  
        times+=1
    text = font.render('Press Space To Start', True, (154, 228, 247))
    screen.blit(start_music_background, (0, 0))
    screen.blit(text, (240, 500))
    pygame.display.flip()

def before_choose():  # ST1
    if mixer_ready==True:
        start_music.stop()
        ending_music.stop()
    screen.blit(blackimg, (0, 0))
    pygame.display.flip()
    start_time_wait = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time_wait < 1500:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()  
    screen.blit(music_choose, (-10, 50))
    pygame.display.flip()

def choose_music():  # ST2
    global perfect,good,miss,maxcombo,combo,score,total_note,music_len,music1_high_score,\
        music2_high_score,music3_high_score,offset_start,bpm,offset_note,music_played,channel,times
    times=0
    score=0
    total_note=0
    perfect=0
    good=0
    miss=0
    maxcombo=0
    combo=0
    screen.blit(choose_music_background, (0, 0))
    screen.blit(music_choose, (0, 0))
    if mixer_ready==True:
        ending_music.stop()
        channel= pygame.mixer.Channel(selected_music)
    if selected_music == 0:     
        if mixer_ready==True: 
            R_crossover_music.stop()
            R_nighttheater_music.stop()
            if not channel.get_busy():
                channel.play(R_dbdoll_music)
        text_score = font.render(str(int(music1_high_score)), True, (255, 255, 255))
        music_len=102000
        screen.blit(choosen, (0, 0))
        screen.blit(music1_draw, (440, 180))
        screen.blit(text_score, (600, 65))
        score_rank(music1_high_score)
        offset_start=0
        offset_note=3.04
        bpm=128.2
    elif selected_music == 1:
        if mixer_ready==True:
            R_dbdoll_music.stop()
            R_nighttheater_music.stop()
            if not channel.get_busy():
                channel.play(R_crossover_music)
        text_score = font.render(str(int(music2_high_score)), True, (255, 255, 255))
        music_len=157000
        screen.blit(choosen, (0, 156))
        screen.blit(music2_draw, (440, 180))
        screen.blit(text_score, (600, 65))
        score_rank(music2_high_score)
        offset_start=0.778
        offset_note=3.04
        bpm=200
    elif selected_music == 2: 
        if mixer_ready==True: 
            R_crossover_music.stop()
            R_dbdoll_music.stop()
            if not channel.get_busy():
                channel.play(R_nighttheater_music)
        text_score = font.render(str(int(music3_high_score)), True, (255, 255, 255))
        music_len=133000
        screen.blit(choosen, (0, 312))
        screen.blit(music3_draw, (440, 180))
        screen.blit(text_score, (600, 65))
        score_rank(music3_high_score)
        offset_start=1.63
        offset_note=3.04
        bpm=151.0

def before_gameing():  # ST3
    global start_time,music_played
    pygame.mixer.stop()

    notes_generate()
    screen.blit(blackimg, (0, 0))
    pygame.display.flip()
    start_time = pygame.time.get_ticks() 
    start_time_wait = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time_wait < 1500:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

def gameing():  # ST4
    global score,combo,selected_music, music_played,stage,start_time

    text_score = font.render(str(int(score)), True, (255, 255, 255))
    screen.blit(text_score, (350, 133))
    text_combo = font.render(str(combo), True, (154, 228, 247))
    screen.blit(text_combo, (350, 222))
    note_move()
    current_time = pygame.time.get_ticks()
    if not music_played and current_time - start_time >= 3100: 
        if mixer_ready==True: 
            if selected_music == 0:
                dbdoll_music.play() 
            elif selected_music == 1:
                crossover_music.play()                
            else:
                nighttheater_music.play()       
            music_played = True 
        else:music_played = True 
        
    if pygame.time.get_ticks()-start_time>= music_len: 
        stage = 5

def after_gameing():  # ST5
    global notes_start_x,perfect,good,miss,maxcombo,combo,score,music_played,selected_music,music1_high_score,\
        music2_high_score,music3_high_score,channel,times
    music_played = False
    if mixer_ready==True:
        crossover_music.stop()
        dbdoll_music.stop()
        nighttheater_music.stop()
    if times==0:
        screen.blit(blackimg, (0, 0))
        pygame.display.flip()
        start_time_wait = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start_time_wait <1500:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()  
        times+=1
    if mixer_ready==True:
        channel=pygame.mixer.Channel(7)
        if not channel.get_busy():
            channel.play(ending_music,fade_ms=500)
    screen.blit(ending, (0, 0))
    score_rank(score)
    text_score = font.render(str(int(score)), True, (255, 255, 255))
    screen.blit(text_score, (650, 113))
    text_maxcombo = font.render(str(maxcombo), True, (154, 228, 247))
    screen.blit(text_maxcombo, (670, 222))
    text_perfect = font.render(str(perfect), True, (154, 228, 247))
    screen.blit(text_perfect, (670, 311))
    text_good = font.render(str(good), True, (154, 228, 247))
    screen.blit(text_good, (670, 397))
    text_miss = font.render(str(miss), True, (154, 228, 247))
    screen.blit(text_miss, (670, 485))
    notes_start_x = 0  
    if selected_music==0:
        if score>music1_high_score:
            music1_high_score=score
    if selected_music==1:
        if score>music2_high_score:
            music2_high_score=score
    if selected_music==2:
        if score>music3_high_score:
            music3_high_score=score           
    pygame.display.flip()

# 判定函式
def judgement(pressed_key, current_time):
    global notes_d, notes_f, notes_j, notes_k, hold_notes_d, hold_notes_f, hold_notes_j, hold_notes_k
    global perfect, good, miss, combo, maxcombo, score, total_note

    target_notes = {"D": notes_d, "F": notes_f, "J": notes_j, "K": notes_k}
    notes_list = target_notes[pressed_key]
    
    for note in notes_list[:]:
        if note["active"]:
            time_difference = abs(current_time - note["target_time"])
            if time_difference <= time_tolerance:
                trigger_perfect(note["key"])
                notes_list.remove(note)
                perfect += 1
                combo += 1
                if combo > maxcombo:
                    maxcombo = combo
                    score +=100000 / total_note
                if mixer_ready==True:
                    perfect_hit.play(loops=0, maxtime=0, fade_ms=0)
                score += 900000 / total_note
                break
            elif time_difference <= time_tolerance + 50:    
                trigger_good(note["key"])    
                notes_list.remove(note)
                good += 1
                combo += 1
                if combo > maxcombo:
                    maxcombo = combo
                    score +=100000 / total_note
                if mixer_ready==True:
                    good_hit.play(loops=0, maxtime=0, fade_ms=0)
                score += 450000 / total_note
                break
            elif time_tolerance + 75 > time_difference > time_tolerance + 50:
                trigger_miss(note["key"])
                notes_list.remove(note)
                miss += 1
                combo = 0
                if mixer_ready==True:
                    miss_hit.play(loops=0, maxtime=0, fade_ms=0)
                break

def update_notes(current_time):
    global notes_d, notes_f, notes_j, notes_k, miss, combo

    for notes_list in [notes_d, notes_f, notes_j, notes_k]:
        for note in notes_list[:]:
            if note["active"]:
                time_difference = current_time - note["target_time"]
                if time_difference > time_tolerance + 50:
                    trigger_miss(note["key"])
                    notes_list.remove(note)  
                    miss += 1  
                    combo = 0
                    if mixer_ready==True:  
                        miss_hit.play(loops=0, maxtime=0, fade_ms=0)

def note_move():
    global notes_d, notes_f, notes_j, notes_k, hold_notes_d, hold_notes_f, hold_notes_j, hold_notes_k
    
    current_time = pygame.time.get_ticks() - start_time
    for notes_list in [notes_d, notes_f, notes_j, notes_k, hold_notes_d, hold_notes_f, hold_notes_j, hold_notes_k]:
        for note in notes_list[:]:
            if not note["active"] and current_time >= note["generate_time"]:
                note["active"] = True  
            if note["active"]:
                note["y"] += note_speed  
                screen.blit(note_img, (note["x"], note["y"]))  
 
        notes_list[:] = [note for note in notes_list if note["active"] or note["y"] < screen.get_height()+800]

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
        print(f"Error: Failed to parse JSON in {file_path}.")

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
        load_notes_from_json(file_path)

def score_rank(score_get):
    ranks = [
        (1000000, rank_P),
        (950000, rank_S),
        (900000, rank_Ap),
        (850000, rank_A),
        (800000, rank_Am),
        (770000, rank_Bp),
        (730000, rank_B),
        (700000, rank_Bm),
        (670000, rank_Cp),
        (630000, rank_C),
        (600000, rank_Cm),
        (1, rank_F),
        (0, rank_X)
    ]
    for threshold, rank_image in ranks:
        if score_get >= threshold:
            if stage==5:
                screen.blit(rank_image, (0, 0))
                break
            else:
                 screen.blit( pygame.transform.scale(rank_image , (200, 200)), (465, -5))
                 break

def trigger_perfect(key):
    if key in lanes:
        perfect_effects.append({
            "position": lanes[key],
            "start_time": pygame.time.get_ticks()
        })
def trigger_good(key):
    if key in lanes:
        good_effects.append({
            "position": lanes[key],
            "start_time": pygame.time.get_ticks()
        })
def trigger_miss(key):
    if key in lanes:
        miss_effects.append({
            "position": lanes[key],
            "start_time": pygame.time.get_ticks()
        })

def show_perfect_effects():
    current_time = pygame.time.get_ticks()
    for effect in perfect_effects[:]:
        elapsed_time = current_time - effect["start_time"]
        if elapsed_time < effect_duration:
            alpha = int(255 * (1 - elapsed_time / effect_duration))
            temp_image = perfect_hit_img.copy()
            temp_image.set_alpha(alpha)
            perfect_effect_rect.x = effect["position"]
            screen.blit(temp_image, perfect_effect_rect)
        else:
            perfect_effects.remove(effect)
def show_good_effects():
    current_time = pygame.time.get_ticks()
    for effect in good_effects[:]:  
        elapsed_time = current_time - effect["start_time"]
        if elapsed_time < effect_duration:
            alpha = int(255 * (1 - elapsed_time / effect_duration))
            temp_image =good_hit_img.copy()
            temp_image.set_alpha(alpha)
            good_effect_rect.x = effect["position"]
            screen.blit(temp_image, good_effect_rect)
        else:
            good_effects.remove(effect)
def show_miss_effects():
    current_time = pygame.time.get_ticks()
    for effect in miss_effects[:]:  
        elapsed_time = current_time - effect["start_time"]
        if elapsed_time < effect_duration:
            alpha = int(255 * (1 - elapsed_time / effect_duration))
            temp_image = miss_hit_img.copy()
            temp_image.set_alpha(alpha)
            miss_effect_rect.x = effect["position"]
            screen.blit(temp_image, miss_effect_rect)
        else:
            miss_effects.remove(effect)

while running:
    if stage == 4: 
        screen.blit(game_background, (0, 0))  
        screen.blit(judge_line, (0, 0)) 
        screen.blit(track, (0, 0))  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False 
        elif event.type == pygame.KEYDOWN:
            if stage == 0 and event.key == pygame.K_SPACE:
                stage = 1  
            elif stage == 2:
                if event.key == pygame.K_UP:
                    selected_music = (selected_music - 1) % 3  
                elif event.key == pygame.K_DOWN:
                    selected_music = (selected_music + 1) % 3  
                elif event.key == pygame.K_SPACE:
                    stage = 3  
            elif stage == 4:       
                if event.key == pygame.K_d:
                    judgement("D", pygame.time.get_ticks() - start_time)
                elif event.key == pygame.K_f:
                    judgement("F", pygame.time.get_ticks() - start_time)
                elif event.key == pygame.K_j:
                    judgement("J", pygame.time.get_ticks() - start_time)
                elif event.key == pygame.K_k:
                    judgement("K", pygame.time.get_ticks() - start_time)
                elif event.key == pygame.K_SPACE :
                    stage = 5
            elif stage == 5 and event.key == pygame.K_SPACE:
                stage = 1

    if stage == 0:
        start()
    elif stage == 1:
        before_choose()
        stage = 2
    elif stage == 2:
        choose_music()     
    elif stage == 3:
        before_gameing()
        stage = 4
    elif stage == 4:
        current_time = pygame.time.get_ticks()- start_time
        gameing()
    elif stage == 5:
        after_gameing()
    show_perfect_effects()
    show_good_effects()
    show_miss_effects()
    update_notes(pygame.time.get_ticks()- start_time)
    pygame.display.flip()  
    clock.tick(45)  
pygame.quit()
