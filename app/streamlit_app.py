import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os

st.set_page_config(page_title='Telco Churn Intelligence — TCi', layout='wide', initial_sidebar_state='expanded')

# Custom dark theme via markdown + CSS (simple)
st.markdown(
    """<style>
    .reportview-container {
        background-color: #0b0f1a;
        color: #e6eef8;
    }
    .sidebar .sidebar-content {
        background-color: #071025;
    }
    .stButton>button {
        background-color: #0ea5a4;
    }
    </style>""", unsafe_allow_html=True)

# Load data
DATA_PATH = os.path.join('..','data','raw','telco_secret.csv') if os.path.exists('..') else os.path.join('data','raw','telco_secret.csv')
@st.cache_data
def load_data(path=DATA_PATH):
    return pd.read_csv(path)

df = load_data()

st.sidebar.title('TCi — Navigation')
page = st.sidebar.radio('Go to', ['Home','Exploration','Model Demo','Insights'])

if page == 'Home':
    st.title('Telco Churn Intelligence — TCi 📶')
    st.subheader('A data-driven investigation into why customers leave')
    c1, c2 = st.columns([1,2])
    with c1:
        st.image('/workspaces/telco-churn-tci/assets/logo.png', width=120)
        st.markdown('**Project:** Interview-ready DS portfolio project')
        st.markdown('**Dataset:** Synthetic Telco (Secret) — 3k rows')
    with c2:
        st.markdown('### Quick stats')
        st.metric('Total customers', int(df.shape[0]))
        churn_rate = (df['churn']=='Yes').mean()
        st.metric('Churn rate', f"{churn_rate:.2%}")
        st.markdown('---')
        st.markdown('**Usage highlights**')
        st.write(df[['app_usage_min_per_week','engagement_score','complaint_count_6m']].describe().T)

if page == 'Exploration':
    st.header('Exploration')
    st.markdown('Key distributions & relationships')
    c1, c2 = st.columns(2)
    with c1:
        st.subheader('Churn distribution')
        fig, ax = plt.subplots()
        sns.countplot(data=df, x='churn', palette=['#9ad1d4','#ffd6a5'], ax=ax)
        st.pyplot(fig)
    with c2:
        st.subheader('Tenure vs Monthly charges')
        fig2, ax2 = plt.subplots()
        sns.scatterplot(data=df, x='tenure', y='monthly_charges', hue='churn', ax=ax2)
        st.pyplot(fig2)

if page == 'Model Demo':
    st.header('Model Demo')
    st.markdown('Load baseline model (if available) or run a quick example')
    from sklearn.ensemble import RandomForestClassifier
    X = df[['tenure','monthly_charges','app_usage_min_per_week','complaint_count_6m','engagement_score']]
    y = (df['churn']=='Yes').astype(int)
    if st.button('Train demo model (quick)'):
        from sklearn.model_selection import train_test_split
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
        clf = RandomForestClassifier(n_estimators=100, random_state=42)
        clf.fit(X_train,y_train)
        st.success('Model trained (demo).')
        st.write('Test score:', clf.score(X_test,y_test))
        st.session_state['demo_model'] = clf

    st.markdown('Or input a sample customer:')
    col1, col2, col3 = st.columns(3)
    with col1:
        tenure = st.number_input('Tenure (months)', 0, 240, 12)
        monthly_charges = st.number_input('Monthly charges', 0.0, 1000.0, 70.0)
    with col2:
        app_usage = st.number_input('App usage min/week', 0, 10000, 120)
        complaints = st.number_input('Complaints (6m)', 0, 20, 0)
    with col3:
        eng_score = st.slider('Engagement score', 0.0, 1.0, 0.5)
    if st.button('Predict churn (demo)'):
        if 'demo_model' in st.session_state:
            model = st.session_state['demo_model']
        else:
            model = RandomForestClassifier(n_estimators=100, random_state=42)
            model.fit(X,y)
        x = [[tenure, monthly_charges, app_usage, complaints, eng_score]]
        proba = model.predict_proba(x)[0][1]
        st.metric('Churn probability', f"{proba:.2%}")
        st.write('Recommendation: ' + ('High risk — consider retention offer' if proba>0.5 else 'Low risk'))

if page == 'Insights':
    st.header('Actionable Insights')
    st.markdown('---')
    st.markdown('1) Customers on month-to-month contracts with low engagement have the highest churn risk.\n\n2) Frequent recent complaints correlate strongly with churn probability.\n\n3) Focus retention on new customers (tenure < 6 months).')
    st.markdown('---')