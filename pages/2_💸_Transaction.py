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
st.set_page_config(page_title='Transactions - TEMPLATE Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('💸Transactions')

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
    elif query == 'TX_Overtime_Intervals':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/fa29510f-8e90-4eda-84da-15e171fe8fa1/data/latest')
    elif query == 'Average_Transaction_Fee':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/c3d7705d-92a2-47ec-910c-6b5de148a133/data/latest')
    elif query == 'Transactions_Averages':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/3238ec2f-3619-421d-b813-5f619483070c/data/latest')
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
    elif query == 'Terra_heatmap1':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/be525b82-1dd2-4969-af01-ddd330ac26f9/data/latest')
    return None


Overview_Tx_Performance = get_data('Overview_Tx_Performance')
hours24_Changes_Per_TX = get_data('hours24_Changes_Per_TX')
TX_Overtime_Intervals = get_data('TX_Overtime_Intervals')
Average_Transaction_Fee = get_data('Average_Transaction_Fee')
Transactions_Averages = get_data('Transactions_Averages')
Overview_Transactions = get_data('Overview_Transactions')
Overview_Contract_Deployed = get_data('Overview_Contract_Deployed')
Overview_Total_Staking_Reward = get_data('Overview_Total_Staking_Reward')
Overview_bridge_out = get_data('Overview_bridge_out')
Overview_new = get_data('Overview_new')
Terra_heatmap2 = get_data('Terra_heatmap2')
Terra_heatmap1 = get_data('Terra_heatmap1')

st.subheader('Glance')

df = Overview_Tx_Performance
df2 = hours24_Changes_Per_TX
df3 = TX_Overtime_Intervals
df4 = Average_Transaction_Fee
df5 = Transactions_Averages
df12 = Overview_Transactions
df13 = Overview_Contract_Deployed
df14 = Overview_Total_Staking_Reward
df15 = Overview_bridge_out
df16 = Overview_new
df17 = Terra_heatmap2
df18 = Terra_heatmap1

c1, c2, c3 = st.columns(3)
with c1:
    st.metric(label='**Avg Fee**',
              value=df["Average Fee"].map('{:,.4f}'.format).values[0])
    st.metric(label='**Avg Fee per Block**',
              value=df["Average Fee per Block"].map('{:,.04}'.format).values[0])
    st.metric(label='**Max FEE**',
              value=df["Max Fee"].map('{:,.04}'.format).values[0])
with c2:
    st.metric(label='**Total Transactions**',
              value=str(df["Total Transactions"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Average Daily Transactions**',
              value=df["Average Daily Transctions"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Total Fees [USD]**',
              value=df["Total Fees"].map('{:,.0f}'.format).values[0])

with c3:
    st.metric(label='**Total Blocks**',
              value=df["Total Block"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Total Fees [Token]**',
              value=df16["TOTAL_FEES"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Last Transaction Overview**',
              value=df16["TOTAL_FEES"].map('{:,.0f}'.format).values[0])


st.subheader('24 Hour Change')
Co1, Co2 = st.columns(2)
with Co1:
    st.metric(label='**Current Day Total Transaction**',
              value=str(df2["Today Transactions"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Current day Transaction Fee**',
              value=df2["Today TX Fee"].map('{:,.0f}'.format).values[0])

with Co2:
    st.metric(label='**24 hour change [Percent]**',
              value=str(df2["change (%) Transactions"].map('{:,.2f}'.format).values[0]))
    st.metric(label='**24 hour change [Percent]**',
              value=df2["change (%) TX Fee"].map('{:,.0f}'.format).values[0])


tab_Overtime, tab_Averages, tab_Heatmap = st.tabs(
    ['**Over Time**', '**Averages**', '**Heatmaps**'])

with tab_Overtime:
    interval = st.radio('**Time Interval**',
                        ['Daily', 'Weekly', 'Monthly'], key='fees_interval', horizontal=True)

    if st.session_state.fees_interval == 'Daily':

        # Transaction over Time with Cumulative Value
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df3["DAY"], y=df3["TOTAL_TRANSACTIONS_OVER_TIME"],
                             name='Total Transaction'), secondary_y=False)
        fig.add_trace(go.Line(x=df3["DAY"], y=df3["CUMULATIVE_TRANSACTIONS_DAILY"],
                              name='CUMULATIVE Transactions'), secondary_y=True)
        fig.update_layout(
            title_text='Daily Transactions with Cumulative Value')
        fig.update_yaxes(
            title_text='Total Transaction', secondary_y=False)
        fig.update_yaxes(title_text='CUMULATIVE Transaction', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # Fees over Time with Cumulative Value
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df3["DAY"], y=df3["TOTAL_FEES_OVER_TIME"],
                             name='Total Fee'), secondary_y=False)
        fig.add_trace(go.Line(x=df3["DAY"], y=df3["CUMULATIVE_FEE_DAILY"],
                              name='CUMULATIVE Fee'), secondary_y=True)
        fig.update_layout(
            title_text='Daily Transaction Fee with Cumulative Value')
        fig.update_yaxes(
            title_text='Total Fee', secondary_y=False)
        fig.update_yaxes(title_text='CUMULATIVE Fee', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # Daily Block over Time With Cumulative Value
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df3["DAY"], y=df3["TOTAL_BLOCK_OVER_TIME"],
                             name='Daily Block'), secondary_y=False)
        fig.add_trace(go.Line(x=df3["DAY"], y=df3["CUMULATIVE_BLOCK_DAILY"],
                              name='CUMULATIVE Block'), secondary_y=True)
        fig.update_layout(
            title_text='Daily Block With Cumulative Value')
        fig.update_yaxes(
            title_text='Daily Block', secondary_y=False)
        fig.update_yaxes(title_text='CUMULATIVE Block', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    elif st.session_state.fees_interval == 'Weekly':

        # Total Transaction over Time with Cumulative Value
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df3["WEEK"], y=df3["TOTAL_TRANSACTIONS_OVER_TIME"],
                             name='Total Transaction'), secondary_y=False)
        fig.add_trace(go.Line(x=df3["WEEK"], y=df3["CUMULATIVE_BLOCK_WEEKLY"],
                              name='CUMULATIVE Transactions'), secondary_y=True)
        fig.update_layout(
            title_text='Weekly Transactions with Cumulative Value')
        fig.update_yaxes(
            title_text='Total Transaction', secondary_y=False)
        fig.update_yaxes(title_text='CUMULATIVE Transaction', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # Total Fees over Time with Cumulative Value
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df3["WEEK"], y=df3["TOTAL_FEES_OVER_TIME"],
                             name='Total Fee'), secondary_y=False)
        fig.add_trace(go.Line(x=df3["WEEK"], y=df3["CUMULATIVE_FEE_WEEKLY"],
                              name='CUMULATIVE Fee'), secondary_y=True)
        fig.update_layout(
            title_text='Weekly Transaction Fee with Cumulative Value')
        fig.update_yaxes(
            title_text='Total Fee', secondary_y=False)
        fig.update_yaxes(title_text='CUMULATIVE Fee', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # Weekly Block Time over Time
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df3["WEEK"], y=df3["TOTAL_BLOCK_OVER_TIME"],
                             name='Weekly Block'), secondary_y=False)
        fig.add_trace(go.Line(x=df3["WEEK"], y=df3["CUMULATIVE_TRANSACTIONS_WEEKLY"],
                              name='CUMULATIVE Block'), secondary_y=True)
        fig.update_layout(
            title_text='Weekly Block With Cumulative Value')
        fig.update_yaxes(
            title_text='Weekly Block', secondary_y=False)
        fig.update_yaxes(title_text='CUMULATIVE Block', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    elif st.session_state.fees_interval == 'Monthly':

        # Total Transaction over Time with Cumulative Value
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df3["MONTH"], y=df3["TOTAL_TRANSACTIONS_OVER_TIME"],
                             name='Total Transaction'), secondary_y=False)
        fig.add_trace(go.Line(x=df3["MONTH"], y=df3["CUMULATIVE_TRANSACTIONS_MONTHLY"],
                              name='CUMULATIVE Transactions'), secondary_y=True)
        fig.update_layout(
            title_text='Monthly Transactions with Cumulative Value')
        fig.update_yaxes(
            title_text='Total Transaction', secondary_y=False)
        fig.update_yaxes(title_text='CUMULATIVE Transaction', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # Total Fees over Time with Cumulative Value
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df3["MONTH"], y=df3["TOTAL_FEES_OVER_TIME"],
                             name='Total Fee'), secondary_y=False)
        fig.add_trace(go.Line(x=df3["MONTH"], y=df3["CUMULATIVE_BLOCK_MONTHLY"],
                              name='CUMULATIVE Fee'), secondary_y=True)
        fig.update_layout(
            title_text='Monthly Transaction Fee with Cumulative Value')
        fig.update_yaxes(
            title_text='Total Fee', secondary_y=False)
        fig.update_yaxes(title_text='CUMULATIVE Fee', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # Monthly Block Time over Time
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df3["MONTH"], y=df3["TOTAL_BLOCK_OVER_TIME"],
                             name='Monthly Block'), secondary_y=False)
        fig.add_trace(go.Line(x=df3["MONTH"], y=df3["CUMULATIVE_BLOCK_MONTHLY"],
                              name='CUMULATIVE Block'), secondary_y=True)
        fig.update_layout(
            title_text='Monthly Block With Cumulative Value')
        fig.update_yaxes(
            title_text='Monthly Block', secondary_y=False)
        fig.update_yaxes(title_text='CUMULATIVE Block', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


with tab_Averages:

    # Number of Transactions with Standards Moving Average
    fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
    fig.add_trace(go.Bar(x=df5['DATE'], y=df5['NUMBER_OF_TRANSACTIONS'],
                         name='Daily NUMBER OF TRANSACTIONS'), secondary_y=False)
    fig.add_trace(go.Line(x=df5['DATE'], y=df5['MA7_TX'],
                          name='Daily Moving average (MA7))'), secondary_y=True)
    fig.add_trace(go.Line(x=df5['DATE'], y=df5['MA26_TX'],
                          name='Daily Moving average (MA26)'), secondary_y=True)
    fig.add_trace(go.Line(x=df5['DATE'], y=df5['MA52_TX'],
                          name='Daily Moving average (MA52))'), secondary_y=True)
    fig.add_trace(go.Line(x=df5['DATE'], y=df5['MA100_TX'],
                          name='Daily Moving average (MA100)'), secondary_y=True)
    fig.update_layout(
        title_text='Number of Transactions with Standards Moving Average')
    fig.update_yaxes(
        title_text='Daily NUMBER OF TRANSACTIONS', secondary_y=False)
    fig.update_yaxes(title_text='Moving averages TX Number', secondary_y=True)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Transaction Fees with Moving averages
    fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
    fig.add_trace(go.Bar(x=df5['DATE'], y=df5["TOTAL_FEES"],
                         name='Daily Volume'), secondary_y=False)
    fig.add_trace(go.Line(x=df5['DATE'], y=df5['MA7_FEE'],
                          name='Daily Moving average (MA7))'), secondary_y=True)
    fig.add_trace(go.Line(x=df5['DATE'], y=df5['MA26_FEE'],
                          name='Daily Moving average (MA26)'), secondary_y=True)
    fig.add_trace(go.Line(x=df5['DATE'], y=df5['MA52_FEE'],
                          name='Daily Moving average (MA52))'), secondary_y=True)
    fig.add_trace(go.Line(x=df5['DATE'], y=df5['MA100_FEE'],
                          name='Daily Moving average (MA100)'), secondary_y=True)
    fig.update_layout(
        title_text='Transaction Fees with Standard Moving averages')
    fig.update_yaxes(
        title_text="TOTAL_FEES", secondary_y=False)
    fig.update_yaxes(title_text='Moving averages Volume', secondary_y=True)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Daily AVG Transaction Fee
    fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
    fig.add_trace(go.Bar(x=df4["DATE"], y=df4["AVG_TRANSACTION_FEE_DAILY"],
                         name='AVG TX Fee'), secondary_y=False)
    fig.update_layout(title_text='Daily AVG Transaction Fee')
    fig.update_yaxes(title_text='AVG TX Fee', secondary_y=False)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with tab_Heatmap:
    # Block per minute on hour of day (UTC)
    fig = px.density_heatmap(df17, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="block per minute on hour of day (UTC)",
                             histfunc='avg', title='Block per minute on hour of day (UTC) Heatmap', nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
        'dtick': 1}, coloraxis_colorbar=dict(title="block per minute on hour of day (UTC)"))
    fig.update_yaxes(categoryorder='array', categoryarray=week_days)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # User per minute on hour of day (UTC)
    fig = px.density_heatmap(df17, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="User per minute on hour of day (UTC)",
                             histfunc='avg', title="User per minute on hour of day (UTC)".title(), nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
        'dtick': 1}, coloraxis_colorbar=dict(title="User per minute on hour of day (UTC)"))
    fig.update_yaxes(categoryorder='array', categoryarray=week_days)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # transactions per minute on hour of day (UTC)
    fig = px.density_heatmap(df17, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="transactions per minute on hour of day (UTC)",
                             histfunc='avg', title="Transactions per minute on hour of day (UTC)".title(), nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
        'dtick': 1}, coloraxis_colorbar=dict(title="transactions per minute on hour of day (UTC)"))
    fig.update_yaxes(categoryorder='array', categoryarray=week_days)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
