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

CurrentConfig.ONLINE_HOST = "https://cdn.kesci.com/lib/pyecharts_assets/"
st.title("1.try pyecharts")

b = (
    Bar()
    .add_xaxis(["Microsoft", "Amazon", "IBM", "Oracle", "Google", "Alibaba"])
    .add_yaxis(
        "2017-2018 Revenue in (billion $)", [21.2, 20.4, 10.3, 6.08, 4, 2.2]
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Top cloud providers 2018", subtitle="2017-2018 Revenue"
        ),
        toolbox_opts=opts.ToolboxOpts(),
    )
)
st_pyecharts(b)

data = [[i, j, random.randint(0, 100)] for i in range(24) for j in range(7)]
hour_list = [str(i) for i in range(24)]
week_list = ['周日', '周一', '周二', '周三', '周四', '周五', '周六']


bar3D = (
    Bar3D()
    .add(
        "",
        data,
        xaxis3d_opts=opts.Axis3DOpts(hour_list, type_="category"),
        yaxis3d_opts=opts.Axis3DOpts(week_list, type_="category"),
        zaxis3d_opts=opts.Axis3DOpts(type_="value"),
    )
)

st_pyecharts(bar3D)

data = []
for t in range(0, 1000):
    x = math.cos(t/10)
    y = math.sin(t/10)
    z = t/10
    data.append([x, y, z])

line3D = (Line3D()
          .add("", data,
               xaxis3d_opts=opts.Axis3DOpts(type_="value"),
               yaxis3d_opts=opts.Axis3DOpts(type_="value"))
          )

st_pyecharts(line3D)

# 虚假数据
x_data = list(range(1990,2020))
y_data_1 = [random.randint(0, 100) for _ in x_data]
y_data_2 = [random.randint(0, 100) for _ in x_data]


bar = (
    Bar()
    .add_xaxis(x_data)
    .add_yaxis('图例1', y_data_1)
    .add_yaxis('图例2', y_data_2)
    .set_global_opts(datazoom_opts=opts.DataZoomOpts(range_start=50, range_end=80))
)

st_pyecharts(bar)
