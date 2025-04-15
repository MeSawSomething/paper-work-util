import json
import tkinter as tk
from tkinter import filedialog, messagebox
import os

def convert_txt_to_json():
    txt_path = filedialog.askopenfilename(
        filetypes=[("Text files", "*.txt")]
    )
    if not txt_path:
        return

    try:
        with open(txt_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # JSON 형식인지 검증
        data = json.loads(content)

        # 저장 경로 지정
        default_name = os.path.splitext(os.path.basename(txt_path))[0] + ".json"
        save_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json")],
            initialfile=default_name
        )
        if not save_path:
            return

        # JSON으로 저장
        with open(save_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        messagebox.showinfo("완료", f"JSON 파일 저장 완료:\n{save_path}")

    except json.JSONDecodeError as e:
        messagebox.showerror("형식 오류", f"JSON 형식 오류:\n{e}")
    except Exception as e:
        messagebox.showerror("오류", str(e))

# GUI 생성
root = tk.Tk()
root.title("TXT → JSON 변환기")
root.geometry("300x160")

label = tk.Label(root, text="JSON 형식의 .txt 파일을 선택하세요", font=("Arial", 11))
label.pack(pady=20)

btn = tk.Button(root, text="변환 시작", command=convert_txt_to_json)
btn.pack()

root.mainloop()
