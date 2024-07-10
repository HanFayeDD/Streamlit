import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 
from pyecharts import options as opts
from pyecharts.charts import *
from pyecharts.datasets import register_url
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType
from streamlit_echarts import st_pyecharts
st.title("车站情况🌤")
df = pd.read_csv('cnstation.csv')


cnt_by_pro = df.value_counts('省').reset_index()
cnt_by_pro


bar = Bar()
bar.add_xaxis(cnt_by_pro['省'].tolist())
bar.add_yaxis("站点数量", cnt_by_pro['count'].tolist())
bar.set_global_opts(title_opts=opts.TitleOpts(title="全国站点数量"),
                    visualmap_opts=opts.VisualMapOpts(min_=min(cnt_by_pro['count']), max_=max(cnt_by_pro['count'])),
                    datazoom_opts=opts.DataZoomOpts(is_show=True),
                    toolbox_opts=opts.ToolboxOpts(is_show=True))
st_pyecharts(bar, width= '700px', height='500px')

