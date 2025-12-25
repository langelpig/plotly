import plotly.graph_objects as go
import pandas as pd
import plotly.offline as pyo

# 1. 準備數據 (根據 PDF 內容提取前五名)
# 數據來源：112年12月 [cite: 15, 17] 與 114年10月 [cite: 2, 4]
data = {
    '機構名稱': ['一卡通票證', '街口支付', '全支付', '悠遊卡', '玉山銀行'],
    '112年12月': [6070995, 6396741, 4547069, 2710401, 2092023], 
    '114年10月': [7109281, 7069733, 6871386, 3857300, 3191803]  
}

df = pd.DataFrame(data)

# 2. 建立 Plotly 圖表
fig = go.Figure()

# 添加 112年12月 數據 (淺灰色長條圖)
fig.add_trace(go.Bar(
    x=df['機構名稱'],
    y=df['112年12月'],
    name='112年12月',
    marker_color='#D3D3D3', # 淺灰色
    text=df['112年12月'].apply(lambda x: f'{x:,}'),
    textposition='outside'
))

# 添加 114年10月 數據 (彩色對比)
fig.add_trace(go.Bar(
    x=df['機構名稱'],
    y=df['114年10月'],
    name='114年10月',
    marker_color=['#58B800', "#EE3B23", "#f0e000", "#005BAB", "#009494"], 
    text=df['114年10月'].apply(lambda x: f'{x:,}'),
    textposition='outside'
))

# 3. 設定圖表佈局、標題與背景網格
fig.update_layout(
    title={
        'text': '電子支付使用者人數增長對比 (112年12月 vs 114年10月)',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    barmode='group', 
    margin=dict(t=120, b=100, l=80, r=80),
     width=1100,
     height=700,
    xaxis_title='電子支付機構名稱',
    yaxis_title='使用者人數 (人)',
    yaxis_tickformat=',',
    hovermode='x unified',
    font=dict(
        family="Arial, sans-serif",
        size=16
    ),
    # ✨ 設定像第一張圖一樣的背景網格 ✨
    plot_bgcolor='white', # 純白背景
    xaxis=dict(
        showgrid=True,
        gridcolor='#F0F0F0', # 淺灰色橫線
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='#F0F0F0', # 淺灰色直線
        dtick=1000000,       # 每 1,000,000 人畫一條主網格線
        zeroline=True,
        zerolinecolor='#D3D3D3'
    )
)

# 4. 產出 HTML 並在瀏覽器開啟
pyo.plot(fig, filename='ebank_grid_chart.html', auto_open=True)

print("圖表已生成並儲存為 'ebank_grid_chart.html'。")