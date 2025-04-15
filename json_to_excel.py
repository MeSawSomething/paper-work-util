import pandas as pd
import json
import tkinter as tk
from tkinter import filedialog, messagebox

def convert_json_to_excel():
    # 파일 선택창 열기
    json_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if not json_path:
        return

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # JSON을 DataFrame으로 변환
        df = pd.json_normalize(data)

        # 저장 경로 설정
        save_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                 filetypes=[("Excel files", "*.xlsx")],
                                                 initialfile="output.xlsx")
        if not save_path:
            return

        df.to_excel(save_path, index=False)
        messagebox.showinfo("완료", f"Excel 파일 저장 완료:\n{save_path}")
    except Exception as e:
        messagebox.showerror("오류", str(e))

# GUI 실행
root = tk.Tk()
root.title("JSON to Excel 변환기")
root.geometry("300x150")

label = tk.Label(root, text="JSON 파일을 선택하세요", font=("Arial", 12))
label.pack(pady=20)

btn = tk.Button(root, text="변환 시작", command=convert_json_to_excel)
btn.pack()

root.mainloop()
