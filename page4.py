import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
data = pd.DataFrame(np.random.randn(20,3), columns=['line1', 'line2', 'line3'])
import streamlit.components.v1 as components
from pyecharts.charts import *
from pyecharts.components import Table
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
import random
import datetime
from pyecharts.globals import CurrentConfig
from streamlit_echarts import st_pyecharts
import datetime
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"Deng.ttf")
plt.rcParams['axes.unicode_minus'] = False
import time
CurrentConfig.ONLINE_HOST = "https://cdn.kesci.com/lib/pyecharts_assets/"
import akshare as ak


# import matplotlib as mpl
# import matplotlib.pyplot as plt
# from matplotlib.font_manager import FontProperties
# font = FontProperties(fname=r"Deng.ttf")
# plt.rcParams['axes.unicode_minus'] = False
# plt.plot([-1,-3,3], [2,6,7])
# plt.title('吃饭', fontproperties=font, fontsize=20)
# plt.show()

def get_df(id:str, begin_time:str, end_time:str):
    begin_time = begin_time.replace('-', '')
    stock_demo_df = ak.stock_zh_a_hist(
        symbol=id,
        period='daily',
        start_date=begin_time.replace('-', ''),
        end_date=end_time.replace('-', '')
    )
    return stock_demo_df
    

def draw(get_str:str, begin_time:datetime.date, end_time:datetime.date):
    try:
        begin_time = begin_time.strftime('%Y%m%d')
        end_time = end_time.strftime('%Y%m%d')
        with st.spinner('Wait for drawing...'):
            msg = st.toast('Gathering data......')
            df = get_df(get_str, begin_time, end_time)
            st.dataframe(df)
            st.subheader('pyecharts', divider='violet')
            line = Line()
            line.add_xaxis(df['日期'].astype(str).tolist())
            line.add_yaxis("成交量", df['成交量'].astype(float).round(2).tolist())
            line.set_global_opts(datazoom_opts=opts.DataZoomOpts(is_show=True),
                                toolbox_opts=opts.ToolboxOpts(is_show=True))
            st_pyecharts(line, height=400)
            st.subheader('pyplot', divider='rainbow')
            fig = plt.figure(figsize=(5, 8))
            ax = fig.add_subplot(211)
            df.plot(x='日期', y='最高', ax=ax, label='higest')
            df.plot(x='日期', y='最低', ax=ax, label='lowest')
            ax.set_xlabel('datetime')
            ax = fig.add_subplot(212)
            df.plot(x='日期', y='成交额', ax=ax, label='deal_money')
            df.plot(x='日期', y='成交量', ax=ax, label='deal_amount')
            ax.set_xlabel('datetime')
            plt.legend()
            fig.suptitle(f'{begin_time} - {end_time}', fontproperties=font, fontsize=30)
            st.pyplot(fig)
            msg.toast('Success!!!', icon='😍')
        st.success('Done!', icon='😊')
        st.balloons()
    except KeyError as e:
        st.error('{}不是合法股票代码或者时间错误'.format(get_str), icon="🚨")
        st.snow()

st.title('1.test interactive')    
get_str = st.text_input("请输入股票代码🤯🤯", "")
today = datetime.datetime.now()
before5year = today.year - 5
beginrange = datetime.date(before5year, 1, 1)
endrange = datetime.date(today.year, today.month, today.day)
d = st.date_input("输入时间区间😊😊",
                  (datetime.date(today.year, 1, 1), datetime.date(today.year, today.month, today.day-1)),
                  beginrange,
                  endrange,
                  format="MM.DD.YYYY")
if get_str.strip() != '' and d!=None and len(d)==2:
    draw(get_str=get_str.strip(), begin_time=d[0], end_time=d[1])







