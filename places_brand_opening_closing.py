import streamlit as st
from read_data import read_from_gsheets
import altair as alt
from datetime import datetime, timedelta
import pandas as pd
import streamlit.components.v1 as components



st.set_page_config(
    page_title="Places Summary Statistics - Brands Freshness",
    layout="wide"
)

#### Brand Open Close #### 


brands_open_close_df = read_from_gsheets("Global Places")
brands_open_close_df = brands_open_close_df[["Country", "Release month", "Brands with at least 1 new opened POI", "Brands with at least 1 new closed POI"]]

brands_open_close_df["Brands with at least 1 new opened POI"] = brands_open_close_df["Brands with at least 1 new opened POI"].str.replace(',', '').astype(int)
brands_open_close_df["Brands with at least 1 new closed POI"] = brands_open_close_df["Brands with at least 1 new closed POI"].str.replace(',', '').astype(int)


for i, value in enumerate(brands_open_close_df['Release month']):
    try:
        brands_open_close_df.loc[i, 'Release month'] = pd.to_datetime(value, format='%b %Y').strftime('%Y-%m')
    except ValueError:
        brands_open_close_df.loc[i, 'Release month'] = pd.to_datetime(value, format='%B %Y').strftime('%Y-%m')

brands_open_close_df = brands_open_close_df[
    (pd.to_datetime(brands_open_close_df["Release month"]) >= pd.to_datetime("2021-01")) &
    (brands_open_close_df["Country"] == "Grand Total")
]

brands_open_close_df["Release month"] = pd.to_datetime(brands_open_close_df["Release month"])+ pd.DateOffset(1)
brands_open_close_df["Release month"] = brands_open_close_df["Release month"].dt.strftime('%Y-%m-%dT%H:%M:%SZ')

# st.dataframe(brands_open_close_df)

chart = alt.Chart(brands_open_close_df).mark_circle(size=50, fill='white', stroke='blue').encode(
    x=alt.X('Release month', title='Release month',  timeUnit='yearmonth'),
    y=alt.Y('Brands with at least 1 new opened POI', title='Brands with at least 1 opening or closing of a POI'),
    color=alt.value('blue'),
    tooltip=[alt.Tooltip('Release month', timeUnit='yearmonth',title='Release month'),
             alt.Tooltip('Brands with at least 1 new opened POI', title='>1 Opened POI', format=',')
    ]
) + alt.Chart(brands_open_close_df).mark_circle(size=50, fill='white', stroke='red').encode(
    x=alt.X('Release month', title='Release month',  timeUnit='yearmonth'),
    y=alt.Y('Brands with at least 1 new closed POI'),
    color=alt.value('red'),
    tooltip=[alt.Tooltip('Release month',  timeUnit='yearmonth',title='Release month'),
             alt.Tooltip('Brands with at least 1 new closed POI', title='>1 Closed POI', format=',')]
)

chart = chart.properties(
    width=900,
    height=500,
    title=alt.TitleParams(
        text='Brands with at Least 1 Opening or Closing of a POI',
        fontSize=18
    )
)

st.altair_chart(chart, use_container_width=True)

hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

css = '''
<style>
section.main > div:has(~ footer ) {
     padding-top: 0px;
    padding-bottom: 0px;
}

[data-testid="ScrollToBottomContainer"] {
    overflow: hidden;
}
</style>
'''

st.markdown(css, unsafe_allow_html=True)


# Keep-alive comment: 2025-04-25 16:08:47.976772
# Keep-alive comment: 2025-04-25 16:18:45.669015
# Keep-alive comment: 2025-04-26 00:24:20.541947
# Keep-alive comment: 2025-04-26 11:24:14.935486
# Keep-alive comment: 2025-04-26 22:23:14.419639
# Keep-alive comment: 2025-04-27 09:23:45.602179
# Keep-alive comment: 2025-04-27 20:23:40.226213
# Keep-alive comment: 2025-04-28 07:24:14.542668
# Keep-alive comment: 2025-04-28 18:24:30.792074
# Keep-alive comment: 2025-04-29 05:23:59.992266
# Keep-alive comment: 2025-04-29 16:24:45.252926
# Keep-alive comment: 2025-04-30 03:23:34.946584
# Keep-alive comment: 2025-04-30 14:24:03.997310
# Keep-alive comment: 2025-05-01 01:24:14.600458
# Keep-alive comment: 2025-05-01 12:23:45.965567
# Keep-alive comment: 2025-05-01 23:23:19.063651
# Keep-alive comment: 2025-05-02 10:24:05.315068
# Keep-alive comment: 2025-05-02 21:23:16.552967
# Keep-alive comment: 2025-05-03 08:23:40.663774
# Keep-alive comment: 2025-05-03 19:23:58.887253
# Keep-alive comment: 2025-05-04 06:24:04.442869
# Keep-alive comment: 2025-05-04 17:23:13.570319