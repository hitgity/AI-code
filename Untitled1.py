#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import pandas as pd

def search_value_in_excel_files(folder_path):
    search_value = input("검색할 값을 입력하세요: ")

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".xlsx"):
                file_path = os.path.join(root, file)
                try:
                    excel_data = pd.read_excel(file_path, sheet_name=None)
                    print(f"파일: {file_path}")
                    found = False
                    for sheet_name, df in excel_data.items():
                        search_result = df.applymap(lambda x: search_value.lower() in str(x).lower())
                        if search_result.any().any():
                            found = True
                            print(f"시트: {sheet_name}")
                            print(df[search_result].dropna(how='all'))
                    if not found:
                        print(f"검색한 값 '{search_value}'을(를) 포함한 데이터 없음")
                    print("---")
                except Exception as e:
                    print(f"파일 '{file_path}'을(를) 열 수 없음 - 오류: {str(e)}")

# 폴더 경로를 지정합니다.
folder_path = "C://Users//psho81//Documents//23년"

# 엑셀 파일에서 값을 검색합니다.
search_value_in_excel_files(folder_path)

pause()

