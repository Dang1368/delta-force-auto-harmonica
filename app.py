import webview
import os
import sys
import tempfile
import json

class Api:
    def __init__(self):
        self.db_path = os.path.join(os.path.expanduser('~'), 'DeltaForceHarmonica_Library.json')
        self.init_default_library()

    def init_default_library(self):
        # Tự động tạo bài hát mẫu mặc định nếu người dùng mở app lần đầu
        try:
            data = []
            if os.path.exists(self.db_path):
                with open(self.db_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
            
            # Nếu danh sách trống, thêm bài mẫu vào
            if not data:
                default_song = {
                    "name": "Bản Nhạc Mẫu Mặc Định",
                    "score": "1:0.5 2:0.5 3:2 5':3 #4:2 0:0.5 1, 1' 2' 3':2.5",
                    "bpm": 120
                }
                data.append(default_song)
                with open(self.db_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception:
            pass

    def run_script(self, code):
        try:
            temp_dir = tempfile.gettempdir()
            ahk_path = os.path.join(temp_dir, "delta_force_macro.ahk")
            with open(ahk_path, "w", encoding="utf-8-sig") as f:
                f.write(code)
            os.startfile(ahk_path)
            return "ok"
        except Exception as e:
            return str(e)

    def save_song(self, name, score, bpm):
        try:
            data = []
            if os.path.exists(self.db_path):
                with open(self.db_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
            for item in data:
                if item['name'] == name:
                    item['score'] = score
                    item['bpm'] = bpm
                    break
            else:
                data.append({"name": name, "score": score, "bpm": bpm})
            with open(self.db_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            return True
        except Exception:
            return False

    def load_songs(self):
        try:
            if os.path.exists(self.db_path):
                with open(self.db_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            return []
        except Exception:
            return []

    def delete_song(self, name):
        try:
            if os.path.exists(self.db_path):
                with open(self.db_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                data = [item for item in data if item['name'] != name]
                with open(self.db_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
            return True
        except Exception:
            return False

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

if __name__ == '__main__':
    html_file = resource_path('index.html')
    window = webview.create_window(
        'Delta Force Auto Harmonica', 
        url=html_file, 
        js_api=Api(), 
        width=1200, 
        height=800,
        background_color='#0a0e17'
    )
    webview.start()