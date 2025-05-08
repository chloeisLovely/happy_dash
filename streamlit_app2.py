# 최종 배포용 streamlit_app.py 코드 (파일 쓰기 없이 실행만 하도록 구성)

final_code = '''
import streamlit as st
import pandas as pd
import plotly.express as px

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("world-happiness-2024.csv")
    df.columns = [col.replace('Explained by: ', '').replace(' ', '_').lower() for col in df.columns]
    df = df.rename(columns={'country_name': 'Country', 'ladder_score': 'Happiness_Score'})
    return df

df = load_data()

# 화면 너비 최대로 설정
st.set_page_config(layout="wide")
st.title("🌍 2024 World Happiness Dashboard")
st.markdown("📊 세계 행복지수 데이터를 한 화면에 시각적으로 확인해보세요.")

# 시각화용 데이터 준비
top10 = df.sort_values("Happiness_Score", ascending=False).head(10)

# 주요 수치형 컬럼
numeric_cols = ["Happiness_Score", "log_gdp_per_capita", "social_support",
                "healthy_life_expectancy", "freedom_to_make_life_choices",
                "generosity", "perceptions_of_corruption"]

# 각 그래프 생성
fig_map = px.choropleth(
    df,
    locations="Country",
    locationmode="country names",
    color="Happiness_Score",
    hover_name="Country",
    color_continuous_scale="YlGnBu",
    title="2024 세계 행복 점수"
)

fig_bar = px.bar(
    top10,
    x="Happiness_Score",
    y="Country",
    orientation="h",
    color="Happiness_Score",
    color_continuous_scale="Blues",
    title="Top 10 Happiest Countries"
)

fig_corr = px.scatter(
    df,
    x="log_gdp_per_capita",
    y="Happiness_Score",
    text="Country",
    trendline="ols",
    title="GDP vs Happiness Score"
)

# 세 개의 그래프를 한 줄에 표시
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🗺️ 세계 행복 지도")
    st.plotly_chart(fig_map, use_container_width=True)

with col2:
    st.subheader("🏆 상위 국가 그래프")
    st.plotly_chart(fig_bar, use_container_width=True)

with col3:
    st.subheader("📈 GDP vs 행복 점수")
    st.plotly_chart(fig_corr, use_container_width=True)
'''

# 저장
final_path = "/mnt/data/streamlit_app.py"
with open(final_path, "w", encoding="utf-8") as f:
    f.write(final_code)

final_path
