import plotly.graph_objects as go
import pandas as pd

# 1. 整理五個年度的總計數據 [cite: 102, 69, 86, 125, 112]
data = {
    "年度月份": ["110年12月", "111年12月", "112年12月", "113年12月", "114年10月"],
    "使用者人數": [15813032, 21881494, 27131575, 30645744, 34813764],
}

df = pd.DataFrame(data)

# 2. 建立圖表
fig = go.Figure()

# 為每個年度添加一條長條
fig.add_trace(go.Bar(
    x=df["年度月份"],
    y=df["使用者人數"],
    text=df["使用者人數"],
    texttemplate='%{text:,}', # 設定數字格式為千分位逗號 [新增]
    textposition='outside',
    marker_color=['#4472C4', '#4472C4', '#4472C4', '#4472C4', '#4472C4'] 
))

# 3. 設定佈局
fig.update_layout(
    title={
        'text': '2021-2025年電子支付使用者總人數趨勢',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis_title='統計年度月份',
    yaxis_title='人數',
    template='plotly_white',
    width=1300,  # 寬度放大
    height=900,  # 高度放大
    bargap=0.5,
    # 修改字體大小為 20 且維持指定字型
    font=dict(
        family="Arial, sans-serif",
        size=20
    )
)

# 4. 顯示圖表
fig.show()