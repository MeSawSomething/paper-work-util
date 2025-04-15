import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

def merge_excel(file_a, file_b, save_path):
    # 엑셀 파일 읽기
    df_a = pd.read_excel(file_a)
    # print("엑셀 A의 컬럼 목록:", df_a.columns.tolist()) 
    df_b = pd.read_excel(file_b, header=11)
    print("엑셀 B의 컬럼 목록:", df_b.columns.tolist()) 
    
    coord_x_col='X'
    coord_y_col='Y'

    # 병원명, 요양기관명 공백 제거
    df_b['병원명'] = df_b['병원명'].astype(str).str.replace(r'\s+', '', regex=True)
    df_a['요양기관명'] = df_a['요양기관명'].astype(str).str.replace(r'\s+', '', regex=True)
    
    # 병합: 병원명(B) <-> 요양기관명(A)
    df_merged = pd.merge(df_b, df_a[['요양기관명', coord_x_col, coord_y_col]], how='left',
                         left_on='병원명', right_on='요양기관명')

    # 결과 정리: 원본 B 열 + 좌표X, 좌표Y
    df_result = df_merged[df_b.columns.tolist() + [coord_x_col, coord_y_col]]

    # 누락된 좌표 정보 확인
    missing = df_result[df_result[coord_x_col].isna() | df_result[coord_y_col].isna()]
    # if not missing.empty:
    #     missing_names = missing['병원명'].tolist()
    #     raise ValueError(f"다음 병원명에 해당하는 좌표를 찾을 수 없습니다:\n" +
    #                      "\n".join(missing_names[:10]) + 
    #                      ("\n...외 %d개" % (len(missing_names) - 10) if len(missing_names) > 10 else "")
    #                     )

    # 저장
    df_result.to_excel(save_path, index=False)
    return save_path


def select_file(entry_widget):
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    if file_path:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, file_path)

def save_file():
    return filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])

def run_merge():
    file_a = entry_a.get()
    file_b = entry_b.get()
    if not file_a or not file_b:
        messagebox.showerror("오류", "두 파일 모두 선택해주세요.")
        return

    save_path = save_file()
    if not save_path:
        return

    try:
        result_path = merge_excel(file_a, file_b, save_path)
        messagebox.showinfo("성공", f"병합 완료!\n결과 저장 위치: {result_path}")
    except Exception as e:
        messagebox.showerror("에러 발생", str(e))

# UI 구성
root = tk.Tk()
root.title("엑셀 병합 도구")
root.geometry("500x200")

ttk.Label(root, text="파일 A (요양기관명+좌표):").pack(pady=5)
entry_a = ttk.Entry(root, width=60)
entry_a.pack()
ttk.Button(root, text="파일 A 선택", command=lambda: select_file(entry_a)).pack(pady=2)

ttk.Label(root, text="파일 B (병원명만 있음):").pack(pady=5)
entry_b = ttk.Entry(root, width=60)
entry_b.pack()
ttk.Button(root, text="파일 B 선택", command=lambda: select_file(entry_b)).pack(pady=2)

ttk.Button(root, text="병합 및 저장", command=run_merge).pack(pady=10)

root.mainloop()
