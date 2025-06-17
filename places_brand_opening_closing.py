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
# Keep-alive comment: 2025-05-05 04:24:24.466476
# Keep-alive comment: 2025-05-05 15:23:43.862228
# Keep-alive comment: 2025-05-06 02:24:34.441986
# Keep-alive comment: 2025-05-06 13:23:36.494007
# Keep-alive comment: 2025-05-07 00:23:35.182359
# Keep-alive comment: 2025-05-07 11:23:47.855706
# Keep-alive comment: 2025-05-07 22:23:46.300377
# Keep-alive comment: 2025-05-08 09:23:55.169842
# Keep-alive comment: 2025-05-08 20:23:47.259236
# Keep-alive comment: 2025-05-09 07:23:57.895312
# Keep-alive comment: 2025-05-09 18:24:09.574893
# Keep-alive comment: 2025-05-10 05:23:52.489103
# Keep-alive comment: 2025-05-10 16:23:39.566844
# Keep-alive comment: 2025-05-11 03:23:38.383942
# Keep-alive comment: 2025-05-11 14:23:29.699318
# Keep-alive comment: 2025-05-12 01:23:35.770836
# Keep-alive comment: 2025-05-12 12:24:06.238250
# Keep-alive comment: 2025-05-12 23:23:38.817263
# Keep-alive comment: 2025-05-13 10:24:43.035543
# Keep-alive comment: 2025-05-13 21:23:39.906827
# Keep-alive comment: 2025-05-14 08:24:08.395203
# Keep-alive comment: 2025-05-14 19:24:09.631037
# Keep-alive comment: 2025-05-15 06:24:06.763999
# Keep-alive comment: 2025-05-15 17:24:37.804143
# Keep-alive comment: 2025-05-16 04:23:51.626602
# Keep-alive comment: 2025-05-16 15:22:55.510958
# Keep-alive comment: 2025-05-17 02:23:12.578506
# Keep-alive comment: 2025-05-17 13:23:56.353230
# Keep-alive comment: 2025-05-18 00:23:10.700512
# Keep-alive comment: 2025-05-18 11:23:42.216889
# Keep-alive comment: 2025-05-18 22:23:36.555430
# Keep-alive comment: 2025-05-19 09:24:13.633562
# Keep-alive comment: 2025-05-19 20:23:12.199739
# Keep-alive comment: 2025-05-20 07:23:28.352996
# Keep-alive comment: 2025-05-20 18:24:40.524433
# Keep-alive comment: 2025-05-21 05:23:11.717321
# Keep-alive comment: 2025-05-21 16:23:21.226640
# Keep-alive comment: 2025-05-22 03:23:15.394230
# Keep-alive comment: 2025-05-22 14:23:19.930645
# Keep-alive comment: 2025-05-23 01:23:18.110001
# Keep-alive comment: 2025-05-23 12:23:18.333466
# Keep-alive comment: 2025-05-23 23:23:21.613387
# Keep-alive comment: 2025-05-24 10:23:19.385995
# Keep-alive comment: 2025-05-24 21:23:16.038667
# Keep-alive comment: 2025-05-25 08:23:16.729726
# Keep-alive comment: 2025-05-25 19:23:21.785071
# Keep-alive comment: 2025-05-26 06:23:09.327823
# Keep-alive comment: 2025-05-26 17:23:11.367231
# Keep-alive comment: 2025-05-27 04:23:17.139477
# Keep-alive comment: 2025-05-27 15:23:21.983948
# Keep-alive comment: 2025-05-28 02:23:31.008795
# Keep-alive comment: 2025-05-28 13:23:22.484162
# Keep-alive comment: 2025-05-29 00:23:14.884341
# Keep-alive comment: 2025-05-29 11:23:10.698463
# Keep-alive comment: 2025-05-29 22:23:24.355684
# Keep-alive comment: 2025-05-30 09:23:09.931785
# Keep-alive comment: 2025-05-30 20:23:10.665326
# Keep-alive comment: 2025-05-31 07:23:22.615037
# Keep-alive comment: 2025-05-31 18:23:17.207058
# Keep-alive comment: 2025-06-01 05:23:16.730966
# Keep-alive comment: 2025-06-01 16:23:29.561698
# Keep-alive comment: 2025-06-02 03:23:30.696188
# Keep-alive comment: 2025-06-02 14:23:22.426900
# Keep-alive comment: 2025-06-03 01:23:12.114769
# Keep-alive comment: 2025-06-03 12:23:27.335754
# Keep-alive comment: 2025-06-03 23:23:23.435581
# Keep-alive comment: 2025-06-04 10:23:22.084679
# Keep-alive comment: 2025-06-04 21:23:01.104425
# Keep-alive comment: 2025-06-05 08:23:24.565507
# Keep-alive comment: 2025-06-05 19:23:15.284001
# Keep-alive comment: 2025-06-06 06:23:12.509757
# Keep-alive comment: 2025-06-06 17:22:55.163666
# Keep-alive comment: 2025-06-07 04:22:57.101064
# Keep-alive comment: 2025-06-07 15:23:06.000312
# Keep-alive comment: 2025-06-08 02:23:11.168581
# Keep-alive comment: 2025-06-08 13:23:12.591384
# Keep-alive comment: 2025-06-09 00:22:55.176802
# Keep-alive comment: 2025-06-09 11:23:10.205272
# Keep-alive comment: 2025-06-09 22:23:19.351022
# Keep-alive comment: 2025-06-10 09:23:22.381708
# Keep-alive comment: 2025-06-10 20:23:15.110058
# Keep-alive comment: 2025-06-11 07:23:16.483212
# Keep-alive comment: 2025-06-11 18:25:06.139569
# Keep-alive comment: 2025-06-12 05:23:13.481150
# Keep-alive comment: 2025-06-12 16:23:16.931150
# Keep-alive comment: 2025-06-13 03:23:17.630559
# Keep-alive comment: 2025-06-13 14:23:07.063543
# Keep-alive comment: 2025-06-14 01:23:27.570062
# Keep-alive comment: 2025-06-14 12:23:13.403596
# Keep-alive comment: 2025-06-14 23:23:04.788362
# Keep-alive comment: 2025-06-15 10:22:51.540803
# Keep-alive comment: 2025-06-15 21:23:25.636824
# Keep-alive comment: 2025-06-16 08:23:22.899120
# Keep-alive comment: 2025-06-16 19:23:06.882877
# Keep-alive comment: 2025-06-17 06:23:43.501188