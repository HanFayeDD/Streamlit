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
import time
CurrentConfig.ONLINE_HOST = "https://cdn.kesci.com/lib/pyecharts_assets/"

##字体设置
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"Deng.ttf")
plt.rcParams['axes.unicode_minus'] = False






def page2():    
    st.title('1.data_table')
    df = pd.DataFrame({'col1': [1,2,3]})
    df  # 👈 Draw the dataframe

    x = 10
    'x', x  # 👈 Draw the string 'x' and then the value of x

    # Also works with most supported chart types
    import matplotlib.pyplot as plt
    import numpy as np

    '''
    # 2.matplotlib绘图

    '''
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter([random.randint(1,100) for i in range(100)], [random.randint(1,100) for i in range(100)], c=[random.randint(1,100) for i in range(100)])
    plt.title('matplotlib在streamlit绘制', fontsize=20, fontproperties=font)
    st.pyplot(fig)


    '''
    # 3.streamlit绘图

    '''
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

    st.line_chart(chart_data)

    '''
    # 4.嵌入本地html
    没懂
    - 1
    - 2
    - 3
    '''
    content = ""

    st.title('5.latex_text')
    st.latex(r" 尝试latex    \frac{a}{b}")
    

def page3():
    st.title('1.输出流')
    _LOREM_IPSUM = """
    Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
    nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    """


    def stream_data():
        for word in _LOREM_IPSUM.split(" "):
            yield word + " "
            time.sleep(0.02)

        yield pd.DataFrame(
            np.random.randn(5, 10),
            columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
        )

        for word in _LOREM_IPSUM.split(" "):
            yield word + " "
            time.sleep(0.02)


    if st.button("Stream data"):
        st.write_stream(stream_data)
        
    st.title('2.容器')
    with st.container():
        st.write("This is inside the container")

        # You can call any Streamlit command, including custom components:
        st.bar_chart(np.random.randn(50, 3))

        st.write("This is outside the container")



pg = st.navigation([
    st.Page("page1.py", title="First page", icon="🔥"),
    st.Page(page2, title="Second page", icon="🤯"),
    st.Page(page3, title="Three page", icon="🤔"),
    st.Page("page4.py", title="Four page", icon="🍳")
])
pg.run()


