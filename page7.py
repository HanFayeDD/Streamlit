import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pydeck as pdk
import streamlit as st

GREEN_RGB = [0, 255, 0, 40]
RED_RGB = [240, 100, 0, 40]

def flitter_m(x):
    if x['s_j'] == -1 or x['s_w'] == -1 or x['e_j'] == -1 or x['e_w'] == -1:
        return False    
    else:   
        return True

def get_target_loc(temp, expect_station):
    data = temp.iloc[0]
    if data['StartStation'] == expect_station:
        return data['s_j'], data['s_w']
    else:
        return data['e_j'], data['e_w']
    

def draw(temp, expect_station):
    temp
    jingdu, weidu = get_target_loc(temp, expect_station)
    arc_layer = pdk.Layer(
        "ArcLayer",
        data=temp,
        get_width="count_std",
        get_source_position=["s_j", "s_w"],
        get_target_position=["e_j", "e_w"],
        get_tilt=15,
        get_source_color=[64, 255, 0, 100],#RED_RGB,
        get_target_color=[0, 128, 200, 100], #GREEN_RGB,
        pickable=True,
        auto_highlight=True,
    )
    view_state = pdk.ViewState(
        latitude=weidu,
        longitude=jingdu,
        bearing=0,
        pitch=20,
        zoom=5,
    )
    TOOLTIP_TEXT = {"html": "{StartStation} 到 {ArriveStation} <br /> 共有 {count} 趟车次",
                    "style": {"backgroundColor": "steelblue", "color": "white"}}
    r = pdk.Deck(arc_layer, initial_view_state=view_state, tooltip=TOOLTIP_TEXT)
    st.pydeck_chart(r)

od_info = pd.read_csv('OD_cnt.csv')
st.title('🚅🚅🚂🚂China RailWay')

station_set = []
station_set.extend(od_info['StartStation'].to_list())
station_set.extend(od_info['ArriveStation'].to_list())
station_set = list(set(station_set))
expect_station = st.text_input("输入车站😀😀", "广州南")

if expect_station in station_set:
    temp = od_info.loc[(od_info['StartStation'] == expect_station) | 
                       (od_info['ArriveStation'] == expect_station)]
    temp = temp.loc[temp.apply(flitter_m, axis=1)]
    if temp.shape[0] == 0:
           st.error('过滤后df为空,请重新选择', icon="🚨")
    else:
        draw(temp, expect_station)
else:
    st.error('not found', icon="🚨")
    


