import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np 
import textwrap

file_path = 'internal_consultant_survey.xlsx'
df = pd.read_excel(file_path)


# 한글 폰트 설정 (Windows용)
plt.rc('font', family='Malgun Gothic')

# 마이너스(-) 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False

# print(df.columns.tolist())

objective_columns =[
  '사용자에 따른 UI 분리', '정부사용자가 원하는 자원 현황 (다섯 가지)', '한달 평균 의뢰건수', '전원시 고려사항'
]

objective_df = df[objective_columns]


# ========================
# 1. 단일 선택 문항 그래프
# ========================

colors = ['#40b2e6', '#7d88ff', '#01dbab', '#98dffd']


# 1. 사용자에 따른 UI 분리 (파이차트)
plt.figure(figsize=(6,6))
objective_df['사용자에 따른 UI 분리'].value_counts().plot(
    kind='pie', 
    autopct='%1.1f%%', 
    startangle=90,
    textprops={'fontsize': 10},
    colors=colors
)

plt.title('사용자에 따른 UI 분리 선호도', fontsize=18)
plt.ylabel('')
plt.tight_layout()
plt.savefig('ui_preference_pie.png', dpi=300)
plt.show()


plt.figure(figsize=(6,6))
objective_df['한달 평균 의뢰건수'].value_counts().plot(
    kind='pie', 
    autopct='%1.1f%%', 
    startangle=90,
    textprops={'fontsize': 12},
    colors=colors
)
plt.title('한달 평균 전원 의뢰 건수 분포', fontsize=18)
plt.ylabel('')
plt.tight_layout()
plt.savefig('monthly_transfer_pie.png', dpi=300)
plt.show()

# ========================
# 2. 복수 선택 문항 그래프
# ========================

# 3. 정부 사용자가 원하는 자원 현황
gov_needs = objective_df['정부사용자가 원하는 자원 현황 (다섯 가지)'].dropna().str.split('|').explode()

plt.figure(figsize=(10,5))
ax = gov_needs.value_counts().plot(kind='bar', color='mediumseagreen')
plt.title('정부 사용자가 원하는 자원 현황', fontsize=18)
plt.xlabel('자원 항목', fontsize=14)
plt.ylabel('선택 횟수', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=12)

# 막대 위에 수치 표시
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='bottom', fontsize=11)

# 여백 조정
plt.subplots_adjust(bottom=0.5, left=0.3)

plt.tight_layout()
plt.savefig('gov_resources_bar.png', dpi=300)
plt.show()


# 4. 전원시 고려사항
transfer_considerations = objective_df['전원시 고려사항'].dropna().str.split('|').explode()

plt.figure(figsize=(10,5))
ax = transfer_considerations.value_counts().plot(kind='bar', color='lightcoral')
# plt.title('전원시 고려사항', fontsize=18)
# plt.xlabel('고려사항', fontsize=14)
plt.ylabel('선택 횟수', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.yticks(fontsize=12)

# 막대 위에 수치 표시
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='bottom', fontsize=11)


# 여백 조정
# plt.subplots_adjust(bottom=0.3)

plt.tight_layout()
plt.savefig('transfer_considerations_bar.png', dpi=300)
plt.show()


search_keywords = df['전원이 가능한 병원 조회를 위한 검색 키워드'].dropna().str.split('|').explode()

# 그래프 그리기
plt.figure(figsize=(10,5))
ax = search_keywords.value_counts().plot(kind='bar', color='lightskyblue')

plt.title('전원이 가능한 병원 조회를 위한 검색 키워드', fontsize=18)
plt.xlabel('검색 조건', fontsize=14)
plt.ylabel('선택 횟수', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=12)

# 막대 위에 수치 표시
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='bottom', fontsize=11)

# 여백 조정
plt.subplots_adjust(bottom=0.5, left=0.3)

plt.tight_layout()
plt.savefig('hospital_search_keywords_bar.png', dpi=300)
plt.show()


# ✅ 바뀐 데이터 컬럼명으로 변경
reason_col = '귀하가 중환자 전원을 의뢰받았을 때 수용하지 못하는 주된 이유는 다음 중 무엇입니까?(*)'
reasons = df[reason_col].dropna().str.split('|').explode()

# 📊 그래프 그리기
plt.figure(figsize=(10,5))
ax = reasons.value_counts().plot(kind='bar', color='mediumseagreen')

plt.title('중환자 전원 수용 불가 주된 이유', fontsize=18)
plt.xlabel('수용 불가 이유', fontsize=14)
plt.ylabel('선택 횟수', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=12)

# ✅ 막대 위에 수치 표시
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='bottom', fontsize=11)

# ✅ 여백 조정
plt.subplots_adjust(bottom=0.5, left=0.3)

plt.tight_layout()
plt.savefig('reason_for_transfer_rejection_bar.png', dpi=300)
plt.show()