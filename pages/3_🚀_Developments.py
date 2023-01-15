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
st.set_page_config(page_title='Development - Near Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('🚀Developments')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Near_Dev_New_contracts':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/75ffb6a4-9110-45b0-ac04-ada0a87c8069/data/latest')
    elif query == 'Near_DevTopnew_weekly_transactions':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/b79d62ba-f40c-4c76-a301-bdb28ad03fc4/data/latest')
    elif query == 'Near_TopNew_Fee':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/fe38d3cc-e103-4627-b2eb-d5a750133e2c/data/latest')
    elif query == 'NearTop10Contracts_Transactions':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/aa2249c8-85dd-4aac-a36a-2165c3b67b48/data/latest')
    elif query == 'NearTop_newcontracts_fee':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/3861369a-98db-4743-a531-2db1860d5cc8/data/latest')
    elif query == 'NearWeekly_TopContracts_users':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/4651d25e-65b6-4fbe-bac1-843c86f093ca/data/latest')
    elif query == 'New_USer':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/287004c6-4fb5-476b-b24c-0bc9d341da1b/data/latest')
    return None


Near_Dev_New_contracts = get_data('Near_Dev_New_contracts')
Near_DevTopnew_weekly_transactions = get_data(
    'Near_DevTopnew_weekly_transactions')
Near_TopNew_Fee = get_data('Near_TopNew_Fee')
NearTop10Contracts_Transactions = get_data('NearTop10Contracts_Transactions')
NearTop_newcontracts_fee = get_data('NearTop_newcontracts_fee')
NearWeekly_TopContracts_users = get_data('NearWeekly_TopContracts_users')
New_USer = get_data('New_USer')


st.text(" \n")
st.subheader('New Contract Metrics')


df = Near_Dev_New_contracts
df2 = Near_DevTopnew_weekly_transactions
df4 = Near_TopNew_Fee
df5 = NearTop10Contracts_Transactions
df6 = NearTop_newcontracts_fee
df7 = NearWeekly_TopContracts_users
df8 = New_USer


# New Contract Deployed Daily
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['DATE'], y=df["NEW_CONTRACTS"],
                     name="New Contract"), secondary_y=False)
fig.add_trace(go.Line(x=df['DATE'], y=df["CUM_NEW_CONTRACTS"],
                      name="Cum New Contract"), secondary_y=True)
fig.update_layout(
    title_text='New Contract Deployed Daily')
fig.update_yaxes(
    title_text="New Contract", secondary_y=False)
fig.update_yaxes(title_text="Cum New Contract", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Top new contracts Based on average transactions fee
fig = px.bar(df4, x="TX_RECEIVER", y="AVG_TX_FEE", color="TX_RECEIVER",
             title='Top new contracts Based on average transactions fee')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Average TX FEE".title())
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Top New Contracts Based on Total Transactions Fee
fig = px.bar(df4, x="TX_RECEIVER", y="TOTAL_TX_FEE", color="TX_RECEIVER",
             title='Top New Contracts Based on Total Transactions Fee')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="TOTAL TX FEE".title())
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.text(" \n")
st.text(" \n")
st.text(" \n")
st.subheader('Overall Contract Metrics')


# Daily Top New Contracts based on Transactions
fig = px.bar(df8.sort_values(["DATE", "TRANSACTIONS"], ascending=[
    True, False]), x="DATE", y="TRANSACTIONS", color="TX_RECEIVER", title='Daily Top "New" Contracts based on Transactions')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Transactions')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Weekly Top Contracts Based on users
fig = px.bar(df7.sort_values(["DATE", "USERS"], ascending=[
    True, False]), x="DATE", y="USERS", color="CONTRACT", title='Weekly Top Contracts Based on users')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Transactions')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Most popular Contract based on users
fig = px.pie(df7, values="USERS",
             names="CONTRACT", title='Most popular Contract based on users')
fig.update_layout(legend_title=None, legend_y=0.5)
fig.update_traces(textinfo='percent+value', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Near Dev- Top 10 Contracts Based on Transactions
fig = px.bar(df5, x="CONTRACT_ADDRESS", y="TRANSACTIONS", color="CONTRACT_ADDRESS",
             title='Top 10 Contracts Based on Transactions')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="TRANSACTIONS".title())
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
