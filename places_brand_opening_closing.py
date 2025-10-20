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
# Keep-alive comment: 2025-06-17 17:23:11.748848
# Keep-alive comment: 2025-06-18 04:23:17.677624
# Keep-alive comment: 2025-06-18 15:23:17.918565
# Keep-alive comment: 2025-06-19 02:23:15.262467
# Keep-alive comment: 2025-06-19 13:23:15.846411
# Keep-alive comment: 2025-06-20 00:23:11.669100
# Keep-alive comment: 2025-06-20 11:24:00.960568
# Keep-alive comment: 2025-06-20 22:23:20.056646
# Keep-alive comment: 2025-06-21 09:23:05.542267
# Keep-alive comment: 2025-06-21 20:23:17.810656
# Keep-alive comment: 2025-06-22 07:23:10.254983
# Keep-alive comment: 2025-06-22 18:23:01.304138
# Keep-alive comment: 2025-06-23 05:23:17.466498
# Keep-alive comment: 2025-06-23 16:23:11.615377
# Keep-alive comment: 2025-06-24 03:23:17.735986
# Keep-alive comment: 2025-06-24 14:22:58.015306
# Keep-alive comment: 2025-06-25 01:22:51.320795
# Keep-alive comment: 2025-06-25 12:23:13.877023
# Keep-alive comment: 2025-06-25 23:23:15.958163
# Keep-alive comment: 2025-06-26 10:23:23.437308
# Keep-alive comment: 2025-06-26 21:24:48.233020
# Keep-alive comment: 2025-06-27 08:23:16.515761
# Keep-alive comment: 2025-06-27 19:23:13.211349
# Keep-alive comment: 2025-06-28 06:23:19.635872
# Keep-alive comment: 2025-06-28 17:23:09.748275
# Keep-alive comment: 2025-06-29 04:22:59.417148
# Keep-alive comment: 2025-06-29 15:22:49.514444
# Keep-alive comment: 2025-06-30 02:23:10.824065
# Keep-alive comment: 2025-06-30 13:22:53.715682
# Keep-alive comment: 2025-07-01 00:24:57.353656
# Keep-alive comment: 2025-07-01 11:23:13.207226
# Keep-alive comment: 2025-07-01 22:23:16.832796
# Keep-alive comment: 2025-07-02 09:23:11.191036
# Keep-alive comment: 2025-07-02 20:25:00.294196
# Keep-alive comment: 2025-07-03 07:23:25.769213
# Keep-alive comment: 2025-07-03 18:22:52.095760
# Keep-alive comment: 2025-07-04 05:23:14.908028
# Keep-alive comment: 2025-07-04 16:23:10.121970
# Keep-alive comment: 2025-07-05 03:23:09.464297
# Keep-alive comment: 2025-07-05 14:23:13.826768
# Keep-alive comment: 2025-07-06 01:23:12.002511
# Keep-alive comment: 2025-07-06 12:23:08.215863
# Keep-alive comment: 2025-07-06 23:23:10.143163
# Keep-alive comment: 2025-07-07 10:23:11.253700
# Keep-alive comment: 2025-07-07 21:23:10.063558
# Keep-alive comment: 2025-07-08 08:23:14.325088
# Keep-alive comment: 2025-07-08 19:23:10.905067
# Keep-alive comment: 2025-07-09 06:23:20.916499
# Keep-alive comment: 2025-07-09 17:23:54.678750
# Keep-alive comment: 2025-07-10 04:23:09.542533
# Keep-alive comment: 2025-07-10 15:23:16.354543
# Keep-alive comment: 2025-07-11 02:23:08.574883
# Keep-alive comment: 2025-07-11 13:23:09.867406
# Keep-alive comment: 2025-07-12 00:22:55.750829
# Keep-alive comment: 2025-07-12 11:23:13.416675
# Keep-alive comment: 2025-07-12 22:23:09.437131
# Keep-alive comment: 2025-07-13 09:23:09.332223
# Keep-alive comment: 2025-07-13 20:22:54.027539
# Keep-alive comment: 2025-07-14 07:23:07.594462
# Keep-alive comment: 2025-07-14 18:23:30.701251
# Keep-alive comment: 2025-07-15 05:23:20.700309
# Keep-alive comment: 2025-07-15 16:23:15.272008
# Keep-alive comment: 2025-07-16 03:23:14.149737
# Keep-alive comment: 2025-07-16 14:23:15.972134
# Keep-alive comment: 2025-07-17 01:23:09.751879
# Keep-alive comment: 2025-07-17 12:23:16.900085
# Keep-alive comment: 2025-07-17 23:23:07.901436
# Keep-alive comment: 2025-07-18 10:23:30.158456
# Keep-alive comment: 2025-07-18 21:23:09.663773
# Keep-alive comment: 2025-07-19 08:23:49.558897
# Keep-alive comment: 2025-07-19 19:22:54.432930
# Keep-alive comment: 2025-07-20 06:23:18.808888
# Keep-alive comment: 2025-07-20 17:23:25.144477
# Keep-alive comment: 2025-07-21 04:23:19.961236
# Keep-alive comment: 2025-07-21 15:23:07.549625
# Keep-alive comment: 2025-07-22 02:23:29.133412
# Keep-alive comment: 2025-07-22 13:23:43.510399
# Keep-alive comment: 2025-07-23 00:23:16.252816
# Keep-alive comment: 2025-07-23 11:23:06.733546
# Keep-alive comment: 2025-07-23 22:23:08.944188
# Keep-alive comment: 2025-07-24 09:23:26.391431
# Keep-alive comment: 2025-07-24 20:23:11.392214
# Keep-alive comment: 2025-07-25 07:23:06.544590
# Keep-alive comment: 2025-07-25 18:23:11.778766
# Keep-alive comment: 2025-07-26 05:23:04.538505
# Keep-alive comment: 2025-07-26 16:23:09.543046
# Keep-alive comment: 2025-07-27 03:23:04.800436
# Keep-alive comment: 2025-07-27 14:22:54.802744
# Keep-alive comment: 2025-07-28 01:23:17.002196
# Keep-alive comment: 2025-07-28 12:23:12.763333
# Keep-alive comment: 2025-07-28 23:23:16.192016
# Keep-alive comment: 2025-07-29 10:22:45.638711
# Keep-alive comment: 2025-07-29 21:23:15.862550
# Keep-alive comment: 2025-07-30 08:23:12.299126
# Keep-alive comment: 2025-07-30 19:23:21.308839
# Keep-alive comment: 2025-07-31 06:23:25.275736
# Keep-alive comment: 2025-07-31 17:23:11.193686
# Keep-alive comment: 2025-08-01 04:23:08.889740
# Keep-alive comment: 2025-08-01 15:23:21.199513
# Keep-alive comment: 2025-08-02 02:23:04.192647
# Keep-alive comment: 2025-08-02 13:23:14.986699
# Keep-alive comment: 2025-08-03 00:23:10.202127
# Keep-alive comment: 2025-08-03 11:23:15.774243
# Keep-alive comment: 2025-08-03 22:23:10.526286
# Keep-alive comment: 2025-08-04 09:23:08.033501
# Keep-alive comment: 2025-08-04 20:23:12.989572
# Keep-alive comment: 2025-08-05 07:23:15.860774
# Keep-alive comment: 2025-08-05 18:23:17.343828
# Keep-alive comment: 2025-08-06 05:23:10.940762
# Keep-alive comment: 2025-08-06 16:25:01.638131
# Keep-alive comment: 2025-08-07 03:23:14.163587
# Keep-alive comment: 2025-08-07 14:23:17.137817
# Keep-alive comment: 2025-08-08 01:23:05.349759
# Keep-alive comment: 2025-08-08 12:23:16.919003
# Keep-alive comment: 2025-08-08 23:23:17.012852
# Keep-alive comment: 2025-08-09 10:23:09.728146
# Keep-alive comment: 2025-08-09 21:23:32.347928
# Keep-alive comment: 2025-08-10 08:23:16.248259
# Keep-alive comment: 2025-08-10 19:23:15.896977
# Keep-alive comment: 2025-08-11 06:23:10.721140
# Keep-alive comment: 2025-08-11 17:23:18.038185
# Keep-alive comment: 2025-08-12 04:23:17.033580
# Keep-alive comment: 2025-08-12 15:23:09.111411
# Keep-alive comment: 2025-08-13 02:23:16.391255
# Keep-alive comment: 2025-08-13 13:23:14.629159
# Keep-alive comment: 2025-08-14 00:23:10.070506
# Keep-alive comment: 2025-08-14 11:23:18.146149
# Keep-alive comment: 2025-08-14 22:23:11.140998
# Keep-alive comment: 2025-08-15 09:23:10.863623
# Keep-alive comment: 2025-08-15 20:23:00.302445
# Keep-alive comment: 2025-08-16 07:23:25.060406
# Keep-alive comment: 2025-08-16 18:23:11.599387
# Keep-alive comment: 2025-08-17 05:23:13.934765
# Keep-alive comment: 2025-08-17 16:23:09.522856
# Keep-alive comment: 2025-08-18 03:23:12.000884
# Keep-alive comment: 2025-08-18 14:23:13.604942
# Keep-alive comment: 2025-08-19 01:23:11.360492
# Keep-alive comment: 2025-08-19 12:23:17.763666
# Keep-alive comment: 2025-08-19 23:23:38.306910
# Keep-alive comment: 2025-08-20 10:23:14.236944
# Keep-alive comment: 2025-08-20 21:23:16.416021
# Keep-alive comment: 2025-08-21 08:23:13.053605
# Keep-alive comment: 2025-08-21 19:23:18.187110
# Keep-alive comment: 2025-08-22 06:23:16.523026
# Keep-alive comment: 2025-08-22 17:23:11.603840
# Keep-alive comment: 2025-08-23 04:23:20.271562
# Keep-alive comment: 2025-08-23 15:23:09.637166
# Keep-alive comment: 2025-08-24 02:23:09.159114
# Keep-alive comment: 2025-08-24 13:23:11.013613
# Keep-alive comment: 2025-08-25 00:23:16.811080
# Keep-alive comment: 2025-08-25 11:23:17.030204
# Keep-alive comment: 2025-08-25 22:23:11.406285
# Keep-alive comment: 2025-08-26 09:23:13.410044
# Keep-alive comment: 2025-08-26 20:23:17.064321
# Keep-alive comment: 2025-08-27 07:23:21.878912
# Keep-alive comment: 2025-08-27 18:22:51.516877
# Keep-alive comment: 2025-08-28 05:23:21.909595
# Keep-alive comment: 2025-08-28 16:23:11.984006
# Keep-alive comment: 2025-08-29 03:22:55.154966
# Keep-alive comment: 2025-08-29 14:23:02.941201
# Keep-alive comment: 2025-08-30 01:23:00.050595
# Keep-alive comment: 2025-08-30 12:22:56.000058
# Keep-alive comment: 2025-08-30 23:22:59.396796
# Keep-alive comment: 2025-08-31 10:22:55.402633
# Keep-alive comment: 2025-08-31 21:23:06.961296
# Keep-alive comment: 2025-09-01 08:23:11.443508
# Keep-alive comment: 2025-09-01 19:23:07.099859
# Keep-alive comment: 2025-09-02 06:22:56.487555
# Keep-alive comment: 2025-09-02 17:23:08.064947
# Keep-alive comment: 2025-09-03 04:22:59.479318
# Keep-alive comment: 2025-09-03 15:23:03.432316
# Keep-alive comment: 2025-09-04 02:23:04.374302
# Keep-alive comment: 2025-09-04 13:23:16.139265
# Keep-alive comment: 2025-09-05 00:22:55.831955
# Keep-alive comment: 2025-09-05 11:22:52.071828
# Keep-alive comment: 2025-09-05 22:23:01.215982
# Keep-alive comment: 2025-09-06 09:22:56.599571
# Keep-alive comment: 2025-09-06 20:22:55.739353
# Keep-alive comment: 2025-09-07 07:23:00.975330
# Keep-alive comment: 2025-09-07 18:23:00.929474
# Keep-alive comment: 2025-09-08 05:22:56.952927
# Keep-alive comment: 2025-09-08 16:23:04.094610
# Keep-alive comment: 2025-09-09 03:23:28.666595
# Keep-alive comment: 2025-09-09 14:23:04.131819
# Keep-alive comment: 2025-09-10 01:22:55.074643
# Keep-alive comment: 2025-09-10 12:23:08.315231
# Keep-alive comment: 2025-09-10 23:22:56.594741
# Keep-alive comment: 2025-09-11 10:22:59.396101
# Keep-alive comment: 2025-09-11 21:22:56.276077
# Keep-alive comment: 2025-09-12 08:23:12.073865
# Keep-alive comment: 2025-09-12 19:23:02.611454
# Keep-alive comment: 2025-09-13 06:22:49.364866
# Keep-alive comment: 2025-09-13 17:22:55.746267
# Keep-alive comment: 2025-09-14 04:22:45.661723
# Keep-alive comment: 2025-09-14 15:22:57.325013
# Keep-alive comment: 2025-09-15 02:22:55.024884
# Keep-alive comment: 2025-09-15 13:22:58.807142
# Keep-alive comment: 2025-09-16 00:22:56.221167
# Keep-alive comment: 2025-09-16 11:23:02.260526
# Keep-alive comment: 2025-09-16 22:22:55.618698
# Keep-alive comment: 2025-09-17 09:22:58.897305
# Keep-alive comment: 2025-09-17 20:23:08.224088
# Keep-alive comment: 2025-09-18 07:23:03.562535
# Keep-alive comment: 2025-09-18 18:23:03.339679
# Keep-alive comment: 2025-09-19 05:22:57.539060
# Keep-alive comment: 2025-09-19 16:23:32.878664
# Keep-alive comment: 2025-09-20 03:23:00.488270
# Keep-alive comment: 2025-09-20 14:23:02.335417
# Keep-alive comment: 2025-09-21 01:23:02.097885
# Keep-alive comment: 2025-09-21 12:23:02.123901
# Keep-alive comment: 2025-09-21 23:22:56.960376
# Keep-alive comment: 2025-09-22 10:23:00.828168
# Keep-alive comment: 2025-09-22 21:22:56.586239
# Keep-alive comment: 2025-09-23 08:22:59.608058
# Keep-alive comment: 2025-09-23 19:23:05.440841
# Keep-alive comment: 2025-09-24 06:22:57.548080
# Keep-alive comment: 2025-09-24 17:23:04.182157
# Keep-alive comment: 2025-09-25 04:27:24.686870
# Keep-alive comment: 2025-09-25 15:23:08.652332
# Keep-alive comment: 2025-09-26 02:23:02.824463
# Keep-alive comment: 2025-09-26 13:23:07.314778
# Keep-alive comment: 2025-09-26 19:31:34.711758
# Keep-alive comment: 2025-09-27 05:31:38.826358
# Keep-alive comment: 2025-09-27 15:31:34.046914
# Keep-alive comment: 2025-09-28 01:31:38.381578
# Keep-alive comment: 2025-09-28 11:31:39.283646
# Keep-alive comment: 2025-09-28 21:31:39.142604
# Keep-alive comment: 2025-09-29 07:31:45.892797
# Keep-alive comment: 2025-09-29 17:31:54.959619
# Keep-alive comment: 2025-09-30 03:31:33.261191
# Keep-alive comment: 2025-09-30 13:31:41.272501
# Keep-alive comment: 2025-09-30 23:31:58.148146
# Keep-alive comment: 2025-10-01 09:32:07.063901
# Keep-alive comment: 2025-10-01 19:31:39.621743
# Keep-alive comment: 2025-10-02 05:32:07.152578
# Keep-alive comment: 2025-10-02 15:32:05.883420
# Keep-alive comment: 2025-10-03 01:31:38.233961
# Keep-alive comment: 2025-10-03 11:31:59.437851
# Keep-alive comment: 2025-10-03 21:31:34.280577
# Keep-alive comment: 2025-10-04 07:31:32.957917
# Keep-alive comment: 2025-10-04 17:31:43.940450
# Keep-alive comment: 2025-10-05 03:31:37.571432
# Keep-alive comment: 2025-10-05 13:31:42.704549
# Keep-alive comment: 2025-10-05 23:32:03.394674
# Keep-alive comment: 2025-10-06 09:32:09.836790
# Keep-alive comment: 2025-10-06 19:31:44.222286
# Keep-alive comment: 2025-10-07 05:31:40.861649
# Keep-alive comment: 2025-10-07 15:32:03.331165
# Keep-alive comment: 2025-10-08 01:31:39.256446
# Keep-alive comment: 2025-10-08 11:31:41.028494
# Keep-alive comment: 2025-10-08 21:31:40.012637
# Keep-alive comment: 2025-10-09 07:31:43.247164
# Keep-alive comment: 2025-10-09 17:31:43.483362
# Keep-alive comment: 2025-10-10 03:31:29.225388
# Keep-alive comment: 2025-10-10 13:31:22.433358
# Keep-alive comment: 2025-10-10 23:31:33.641111
# Keep-alive comment: 2025-10-11 09:31:39.264334
# Keep-alive comment: 2025-10-11 19:31:33.172722
# Keep-alive comment: 2025-10-12 05:31:36.439173
# Keep-alive comment: 2025-10-12 15:31:42.328620
# Keep-alive comment: 2025-10-13 01:31:35.449500
# Keep-alive comment: 2025-10-13 11:32:07.630461
# Keep-alive comment: 2025-10-13 21:31:30.318691
# Keep-alive comment: 2025-10-14 07:31:34.273148
# Keep-alive comment: 2025-10-14 17:31:37.494356
# Keep-alive comment: 2025-10-15 03:31:34.137598
# Keep-alive comment: 2025-10-15 13:31:38.030743
# Keep-alive comment: 2025-10-15 23:31:40.456455
# Keep-alive comment: 2025-10-16 09:31:37.278734
# Keep-alive comment: 2025-10-16 19:31:43.760819
# Keep-alive comment: 2025-10-17 05:31:41.043393
# Keep-alive comment: 2025-10-17 15:31:58.404230
# Keep-alive comment: 2025-10-18 01:31:35.096209
# Keep-alive comment: 2025-10-18 11:31:59.833079
# Keep-alive comment: 2025-10-18 21:32:09.218073
# Keep-alive comment: 2025-10-19 07:31:28.965154
# Keep-alive comment: 2025-10-19 17:32:04.513954
# Keep-alive comment: 2025-10-20 03:32:02.945703
# Keep-alive comment: 2025-10-20 13:31:42.717104
# Keep-alive comment: 2025-10-20 23:31:35.651390