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
st.set_page_config(page_title='Governance - TEMPLATE Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('🏛️Governance')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources


@st.cache()
def get_data(query):
    if query == 'Overview_Governance':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/b2558506-8bbc-46e7-8cbf-ada0bf938a7d/data/latest')
    elif query == 'Top10_Validator':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/51f20a77-f76b-474b-8959-8889209a2c16/data/latest')
    elif query == 'Top10_Deligator_TX':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/33918659-b306-477f-af12-6382a498461f/data/latest')
    elif query == 'Top10_Deligator_Vol':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/10798924-1171-4340-a0ed-87ae4ca808a3/data/latest')
    elif query == 'Overview_bridge_out':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/89ff4f7f-817e-4337-bff0-b54e4b83b763/data/latest')
    elif query == 'Overview_new':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ffd5b837-e3bf-4f55-a415-331c67137ac1/data/latest')
    elif query == 'Terra_heatmap2':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/f0f8af7f-08b8-4efe-853c-f0572a8b2290/data/latest')
    elif query == 'Terra_heatmap1':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/be525b82-1dd2-4969-af01-ddd330ac26f9/data/latest')
    return None


Overview_Governance = get_data('Overview_Governance')
Top10_Validator = get_data('Top10_Validator')
Top10_Deligator_TX = get_data('Top10_Deligator_TX')
Top10_Deligator_Vol = get_data('Top10_Deligator_Vol')
Overview_bridge_out = get_data('Overview_bridge_out')
Overview_new = get_data('Overview_new')
Terra_heatmap2 = get_data('Terra_heatmap2')
Terra_heatmap1 = get_data('Terra_heatmap1')

# Single Number Overview
st.subheader('Overview')
df1 = Overview_Governance
df2 = Top10_Validator
df3 = Top10_Deligator_TX
df4 = Top10_Deligator_Vol
df5 = Overview_bridge_out
df6 = Overview_new
df7 = Terra_heatmap2
df8 = Terra_heatmap1

c1, c2 = st.columns(2)
with c1:
    st.metric(label='**Avg Stake Volume per User**',
              value=str(df1["NEAR_PER_STAKER"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Number of Stake transaction**',
              value=df1["STAKES"].map('{:,.0f}'.format).values[0])

with c2:
    st.metric(label='**Number of Stakers**',
              value=str(df1["STAKERS"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Stake Volume**',
              value=df1["STAKED_NEAR"].map('{:,.0f}'.format).values[0])

st.subheader('Metrics')
# Top 10 Validator Based on Volume
fig = px.bar(df2, x="VALODATOR", y="AMOUNT", color="VALODATOR",
             title='Top 10 Validator Based on Volume')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="AMOUNT".title())
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Top 10 Delegator Based on Transactions
fig = px.bar(df3, x="STAKERS", y="STAKES", color="STAKERS",
             title='Top 10 Delegator Based on Transactions')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Stake".title())
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Top 10 Delegator Based on Volume
fig = px.bar(df4, x="STAKERS", y="AMOUNT", color="STAKERS",
             title='Top 10 Delegator Based on Volume')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Volume".title())
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
