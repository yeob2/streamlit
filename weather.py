import streamlit as st
import datetime
import requests
import pandas as pd

st.title("일일 기온 변화 차트")

# 날짜 선택 (오늘부터 7일 이내만 선택)
today = datetime.date.today()
selected_date = st.date_input(
    "날짜를 선택하세요", 
    today, 
    min_value=today, 
    max_value=today + datetime.timedelta(days=7)
)

# Visual Crossing API 설정
api_key = "KKKJST8JNTLCF29HCNYDL5BKB"  # 발급받은 API 키 입력
location = "Seoul"
url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{selected_date}?unitGroup=metric&key={api_key}&contentType=json"

response = requests.get(url)
data = response.json()

# 데이터 확인
if "days" not in data:
    st.error(f"API 호출 실패: {data.get('message', 'Unknown error')}")
else:
    hours_data = data['days'][0]['hours']
    
    # 시간별 기온 데이터 추출
    records = []
    for hour in hours_data:
        records.append({
            '시간': hour['datetime'],
            '온도': hour['temp']
        })

    # 데이터프레임으로 변환 후 차트 출력
    df = pd.DataFrame(records)
    df = df.set_index('시간')
    st.line_chart(df)
