import requests
import pandas as pd
from datetime import datetime

# 1. API 주소 설정
url = "https://api.saveticker.com/api/news/list?page=1&page_size=20&sort=created_at_desc&sources=fivelines_news%2Cfinancial-juice%2Creuters"

# 2. 브라우저인 척 하기 위한 헤더 설정
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://www.saveticker.com/"
}

# 3. 데이터 가져오기
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # JSON 데이터를 파이썬 딕셔너리로 변환
    raw_data = response.json()
    
    # 'items' 또는 데이터가 들어있는 리스트 추출 (API 구조에 따라 'data' 혹은 'items'일 수 있습니다)
    # 일반적인 API 구조를 가정하여 작성했습니다.
    news_items = raw_data.get('items', raw_data) 
    
    # 4. Pandas DataFrame(표)으로 변환
    # news_items는 전체 응답 딕셔너리이므로, 실제 뉴스 리스트는 'news_list' 키 아래에 있습니다.
    df = pd.DataFrame(news_items['news_list'])
    
    # 5. 보기 좋게 주요 컬럼만 필터링 (컬럼명은 API 실제 결과에 따라 수정이 필요할 수 있습니다)
    # 예: ['title', 'source', 'created_at']
    print("최신 뉴스 리스트:")
    display(df[['id', 'title', 'source', 'created_at', 'view_count']]) # 코랩에서 표 형식으로 예쁘게 보여주는 함수
else:
    print(f"데이터를 가져오는데 실패했습니다. 상태 코드: {response.status_code}")
    if response.status_code == 403:
        print("Cloudflare 차단 가능성이 있습니다. 추가 우회 방법이 필요합니다.")
