import plotly.graph_objects as go
import pandas as pd
import plotly.offline as pyo

# 1. 準備數據
data = {
    '年份': ['110年12月', '111年12月', '112年12月', '113年12月', '114年10月'],
    '一卡通票證': [4556549, 5402511, 6070995, 6684320, 7109281], 
    '街口支付': [5202535, 5929697, 6396741, 6616273, 7069733], 
    '全支付': [0, 2786722, 4547069, 5244313, 6871386],           
    '悠遊卡': [1470132, 2052887, 2710401, 3345646, 3857300],    
    '玉山商業銀行': [1464773, 1725032, 2092023, 2694053, 3191803]   
}

df = pd.DataFrame(data)

brand_colors = {
    '一卡通票證': '#58B800',
    '街口支付': '#EE3B23',
    '全支付': '#f0e000',
    '悠遊卡': '#005BAB',
    '玉山商業銀行': '#009494'
}

pos_config = {
    '一卡通票證': ['bottom center', 'bottom center', 'bottom center', 'top center', 'top left'],
    '街口支付': ['top center', 'top center', 'top center', 'bottom center', 'top right'],
    '全支付': ['top center', 'top center', 'top center', 'top center', 'bottom center'],
    '悠遊卡': ['top center', 'top center', 'top center', 'top center', 'top center'],
    '玉山商業銀行': ['bottom center', 'bottom center', 'bottom center', 'bottom center', 'bottom center']
}

fig = go.Figure()

for column in df.columns[1:]:
    text_list = []
    for i, val in enumerate(df[column]):
        if val == 0:
            text_list.append('')
        else:
            label = f'<b>{val/10000:.0f}萬</b>'
            if i == 3 and column == '一卡通票證':
                label = label + '<br> ' 
            elif i == 3 and column == '街口支付':
                label = '<br>' + label 
            text_list.append(label)

    fig.add_trace(go.Scatter(
        x=df['年份'],
        y=df[column],
        mode='lines+markers+text',
        name=column,
        line=dict(color=brand_colors[column], width=4),
        marker=dict(size=10),
        text=text_list,
        textposition=pos_config[column],
        textfont=dict(size=14, color='black'), # 數據標籤微調大一點
        cliponaxis=False, 
        hovertemplate=f"<b>{column}</b><br>人數: %{{y:,.0f}}<extra></extra>"
    ))

# 修改重點：放大寬高、字體，並確保水平置中
fig.update_layout(
    title={'text': '2021-2025年電子支付使用人數前五名增長趨勢圖', 'x': 0.5, 'y': 0.95, 'font': {'size': 28}},
    plot_bgcolor='white',
    width=1300,  # 寬度放大
    height=900,  # 高度放大
    
    # 左右 margin 對稱確保置中
    margin=dict(t=150, r=100, l=100, b=120),
    
    xaxis_title={
        'text': '統計時間',
        'font': {'size': 20, 'color': 'black'},
        'standoff': 40
    },
    
    yaxis_title={
        'text': '使用者人數 (人)',
        'font': {'size': 18}
    },
    yaxis_tickformat=',',
    
    xaxis=dict(
        showgrid=True, 
        gridcolor='#F0F0F0',
        range=[-0.5, 4.5], 
        tickfont=dict(size=16) # 刻度文字放大
    ), 
    
    yaxis=dict(
        showgrid=True, 
        gridcolor='#F0F0F0', 
        dtick=1000000, 
        range=[-500000, 8500000],
        tickfont=dict(size=14)
    ), 
    
    legend=dict(
        orientation="h", 
        yanchor="bottom", 
        y=1.03, 
        xanchor="center", 
        x=0.5,
        font=dict(size=16) # 圖例字體放大
    )
)

pyo.plot(fig, filename='ebank_centered_xaxis.html', auto_open=True)