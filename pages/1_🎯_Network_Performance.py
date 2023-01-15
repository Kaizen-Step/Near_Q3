# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Global Variables
theme_plotly = None  # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='Network Performance - Near Q3 Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('🎯Network Performance')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Overview_Tx_Performance':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a23a11a3-4fc4-4297-ab8b-9b2800f9a3e9/data/latest')
    elif query == 'hours24_Changes_Per_TX':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/8f1d8254-2387-4631-ab6d-6f487c5187e3/data/latest')
    elif query == 'TX_Num_Overtime':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/4e1c9246-a508-475f-9048-8abba7eb96d7/data/latest')
    elif query == 'Terra_Transactions_Intervals':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/22fab0e2-89d7-4f75-a2d1-d96c5dc017d1/data/latest')
    elif query == 'Succ_Vs_Fail':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/c3d7705d-92a2-47ec-910c-6b5de148a133/data/latest')
    elif query == 'Overview_Contract_Deployed':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/aecb2cbd-9f9c-4a69-97eb-5a0a13cf04c6/data/latest')
    elif query == 'Overview_Total_Staking_Reward':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/97a71654-c83b-4f34-be2c-6f9f826822fd/data/latest')
    elif query == 'Overview_bridge_out':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/89ff4f7f-817e-4337-bff0-b54e4b83b763/data/latest')
    elif query == 'Overview_new':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ffd5b837-e3bf-4f55-a415-331c67137ac1/data/latest')
    elif query == 'Terra_heatmap2':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/f0f8af7f-08b8-4efe-853c-f0572a8b2290/data/latest')
    elif query == 'Network_Per_Heatmap':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/11c49c5c-f1ee-49bc-84df-2f45722b70f6/data/latest')
    elif query == 'Net_Per_Intervals':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/fa29510f-8e90-4eda-84da-15e171fe8fa1/data/latest')
    return None


Overview_Tx_Performance = get_data('Overview_Tx_Performance')
hours24_Changes_Per_TX = get_data('hours24_Changes_Per_TX')
TX_Num_Overtime = get_data('TX_Num_Overtime')
Terra_Transactions_Intervals = get_data('Terra_Transactions_Intervals')
Succ_Vs_Fail = get_data('Succ_Vs_Fail')
Overview_Transactions = get_data('Overview_Transactions')
Overview_Contract_Deployed = get_data('Overview_Contract_Deployed')
Overview_Total_Staking_Reward = get_data('Overview_Total_Staking_Reward')
Overview_bridge_out = get_data('Overview_bridge_out')
Overview_new = get_data('Overview_new')
Terra_heatmap2 = get_data('Terra_heatmap2')
Network_Per_Heatmap = get_data('Network_Per_Heatmap')
Net_Per_Intervals = get_data('Net_Per_Intervals')
st.subheader('Glance')

df = Overview_Tx_Performance
df2 = hours24_Changes_Per_TX
df3 = TX_Num_Overtime
df4 = Terra_Transactions_Intervals
df5 = Succ_Vs_Fail
df6 = Net_Per_Intervals
df12 = Overview_Transactions
df13 = Overview_Contract_Deployed
df14 = Overview_Total_Staking_Reward
df15 = Overview_bridge_out
df16 = Overview_new
df17 = Terra_heatmap2
df18 = Network_Per_Heatmap

c1, c2, c3 = st.columns(3)
with c1:
    st.metric(label='**TX Success Rate**',
              value=df["Success Rate"].map('{:,.2f}'.format).values[0])
    st.metric(label='**Number of TX per Block(TPB)**',
              value=df["TPB"].map('{:,.0f}'.format).values[0])
    # st.metric(label='**Average Time Between Blocks**',
    # value=df16["TOTAL_FEES"].map('{:,.0f}'.format).values[0])
with c2:
    st.metric(label='**Average Block time**',
              value=str(df["Average Block Time"].map('{:,.04}'.format).values[0]))
    st.metric(label='**Average Fail Rate**',
              value=df["Failed Rate"].map('{:,.2f}'.format).values[0])
    # st.metric(label='**Max Time Between Blocks**',
    # value=df16["TOTAL_FEES"].map('{:,.0f}'.format).values[0])

with c3:
    st.metric(label='**Number of TX per Second(TPS)**',
              value=df["TPS"].map('{:,.2f}'.format).values[0])
    st.metric(label='**Number of Block Per Min**',
              value=df["Average Block per Min"].map('{:,.2f}'.format).values[0])
    # st.metric(label='**Min Time Between Blocks**',
    # value=df16["TOTAL_FEES"].map('{:,.0f}'.format).values[0])


st.subheader('Quarter Change')
Co1, Co2 = st.columns(2)
with Co1:
    st.metric(label='**Current Quarter Success Rate**',
              value=str(df2["Today Success Rate"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Current Quarter TPS**',
              value=df2["24 Hours TPS"].map('{:,.0f}'.format).values[0])

with Co2:
    st.metric(label='**Quarter change [percent]**',
              value=str(df2["change (%) Success Rate"].map('{:,.2f}'.format).values[0]))
    st.metric(label='**Quarter change [Percent]**',
              value=df2["change (%) TPS"].map('{:,.2f}'.format).values[0])


tab_Overtime, tab_Heatmaps, tab_Comparison = st.tabs(
    ['**Over Time**', '**HeatMaps**', '**Comparison**'])

with tab_Overtime:
    interval = st.radio('**Time Interval**',
                        ['Daily', 'Weekly', 'Monthly'], key='fees_interval', horizontal=True)

    if st.session_state.fees_interval == 'Daily':

        # Daily Block Time
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df6["DAY"], y=df6["AVG_BLOCK_TIME_DAILY"],
                             name='Daily Block Time'), secondary_y=False)
        fig.update_layout(
            title_text='Daily Block Time')
        fig.update_yaxes(
            title_text='Daily Block Time', secondary_y=False)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # Daily "TPS_DAILY"
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df6["DAY"], y=df6["TPS_DAILY"],
                             name="TPS_DAILY"), secondary_y=False)
        fig.update_layout(
            title_text='Daily Transaction Per Second')
        fig.update_yaxes(
            title_text="TPS_DAILY", secondary_y=False)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    elif st.session_state.fees_interval == 'Weekly':

        # Weekly Block Time
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df6["WEEK"], y=df6["AVG_BLOCK_TIME_WEEKLY"],
                             name='Weekly Block Time'), secondary_y=False)
        fig.update_layout(
            title_text='Weekly Block Time')
        fig.update_yaxes(
            title_text='Weekly Block Time', secondary_y=False)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # Weekly "TPS_DAILY"
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df6["WEEK"], y=df6["TPS_WEEKLY"],
                             name="TPS_WEEKLY"), secondary_y=False)
        fig.update_layout(
            title_text='Weekly Transaction Per Second')
        fig.update_yaxes(
            title_text="TPS_WEEKLY", secondary_y=False)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    elif st.session_state.fees_interval == 'Monthly':

       # Monthly Block Time
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df6["MONTH"], y=df6["AVG_BLOCK_TIME_MONTHLY"],
                             name='Monthly Block Time'), secondary_y=False)
        fig.update_layout(
            title_text='Monthly Block Time')
        fig.update_yaxes(
            title_text='Monthly Block Time', secondary_y=False)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # Monthly "TPS_DAILY"
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df6["MONTH"], y=df6["TPS_MONTHLY"],
                             name="TPS MONTHLY"), secondary_y=False)
        fig.update_layout(
            title_text='Monthly Transaction Per Second')
        fig.update_yaxes(
            title_text="TPS MONTHLY", secondary_y=False)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


with tab_Heatmaps:

    st.subheader('Heatmaps')

    # Failedtransactions per minute on hour of day (UTC)
    fig = px.density_heatmap(df18, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="Failed transactions per minute on hour of day (UTC)",
                             histfunc='avg', title="Failed transactions per minute on hour of day (UTC)".title(), nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
        'dtick': 1}, coloraxis_colorbar=dict(title="Failed transactions per minute on hour of day (UTC)"))
    fig.update_yaxes(categoryorder='array', categoryarray=week_days)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Success transactions per minute on hour of day (UTC)
    fig = px.density_heatmap(df18, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="Success transactions per minute on hour of day (UTC)",
                             histfunc='avg', title="Success transactions per minute on hour of day (UTC)".title(), nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
        'dtick': 1}, coloraxis_colorbar=dict(title="Success transactions per minute on hour of day (UTC)"))
    fig.update_yaxes(categoryorder='array', categoryarray=week_days)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


with tab_Comparison:
    # Daily Success VS Falied Rate
    fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
    fig.add_trace(go.Bar(x=df5["DATE"], y=df5["DAILY_SUCCESS_RATE"],
                         name="DAILY SUCCESS RATE".title()), secondary_y=False)
    fig.add_trace(go.Bar(x=df5["DATE"], y=df5["DAILY_FAILED_RATE"],
                         name="DAILY FAILED RATE".title()), secondary_y=False)
    fig.update_layout(
        title_text='Daily Success VS Falied Rate')
    fig.update_yaxes(
        title_text="Daily Success".title(), secondary_y=False)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
