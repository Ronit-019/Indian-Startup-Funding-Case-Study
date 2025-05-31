import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',page_title='Startup Analysis')

df = pd.read_csv("startup_cleaned.csv")

df['date'] = df['date'].replace('05/072018','05/07/2018')
df['date'] = df['date'].replace('01/07/015','01/07/2015')
df['date'] = df['date'].replace('12/05.2015','12/05/2015')
df['date'] = df['date'].replace('13/04.2015','13/04/2015')

df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
year_list = sorted(df['year'].unique().tolist())
year_list.insert(0,"Overall")


st.sidebar.title("Navigation")
option = st.sidebar.selectbox('Select One', ['Home', 'Overall Analysis', 'Investor Analysis', 'Startup Analysis'])

if option == 'Home':
    st.title("🚀 Indian Startup Funding Analysis")
    st.markdown("""
    Welcome to the Indian Startup Funding Dashboard! 💡

    This application provides insights into:
    - 💰 Overall funding trends
    - 🧠 Sector and round-wise analysis
    - 🏙️ City-wise startup distributions
    - 📈 YOY investment patterns
    - 🤝 Investor and Startup level details

    Use the sidebar to explore:
    - **Overall trends**
    - **Investor-specific analysis**
    - **Startup-specific analysis**

    ---
    **Dataset Source**: [Startup Funding Data](#)
    """)

elif option == 'Overall Analysis':
    load_overall_analysis()

elif option == 'Investor Analysis':
    selected_investor = st.sidebar.selectbox("Select Investor", sorted(df['investor'].dropna().unique()))
    load_investor_details(selected_investor)

elif option == 'Startup Analysis':
    selected_startup = st.sidebar.selectbox("Select Startup", sorted(df['startup'].dropna().unique()))
    load_startup_analysis(selected_startup)

def load_overall_analysis():

    total = round(df['amount'].sum())
    max_funding = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
    avg_funding = round(df.groupby('startup')['amount'].sum().mean())
    num_startups = df['startup'].nunique()

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.metric("Total Funding", str(total) + 'Cr')
    with col2:
        st.metric("Maximum Funding", str(max_funding) + 'Cr')
    with col3:
        st.metric("Average Funding", str(avg_funding) + 'Cr')
    with col4:
        st.metric("Funded Startups", str(num_startups))

    col1, col2 = st.columns(2)

    with col1:
        st.header("MOM Graph According to Investment")

        selected_option1 = st.selectbox('Select Type',['Total','Count'],key='mom_select')

        if selected_option1 == 'Total':
            temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
        else:
            temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()

        temp_df['xaxis'] = temp_df['month'].astype(str) + '-' + temp_df['year'].astype(str)

        fig1 = plt.figure()
        plt.plot(temp_df['xaxis'],temp_df['amount'])
        plt.xticks(temp_df['xaxis'][::2])
        plt.xticks(rotation=90)
        st.pyplot(fig1)

    with col2:
        st.header("Sector Analysis of Funding")

        selected_option2 = st.selectbox('Select Type',['Total','Count'],key='sector_select')

        if selected_option2 == 'Total':
            temp_df = df.groupby('vertical')['amount'].sum().reset_index().sort_values(by='amount',ascending=False).head()
        else:
            temp_df = df.groupby('vertical')['amount'].count().reset_index().sort_values(by='amount',ascending=False).head()

        fig2 = plt.figure()
        plt.pie(temp_df['amount'],labels=temp_df['vertical'],autopct="%1.1f%%")
        st.pyplot(fig2)

    col1, col2 = st.columns(2)

    with col1:
        st.header("Round Wise Funding")

        selected_option1 = st.selectbox('Select Type', ['Total', 'Count'], key='round_select')

        if selected_option1 == 'Total':
            temp_df = df.groupby('round')['amount'].sum().sort_values(ascending=False).head(10)
        else:
            temp_df = df.groupby('round')['amount'].count().sort_values(ascending=False).head(10)

        fig1 = plt.figure()
        plt.bar(temp_df.index,temp_df.values)
        plt.xticks(rotation=90)
        st.pyplot(fig1)

    with col2:
        st.header("City Wise Funding")

        selected_option2 = st.selectbox('Select Type', ['Total', 'Count'], key='city_select')

        if selected_option2 == 'Total':
            temp_df = df.groupby('city')['amount'].sum().reset_index().sort_values(by='amount',ascending=False).head()
        else:
            temp_df = df.groupby('city')['amount'].count().reset_index().sort_values(by='amount',ascending=False).head()

        fig2 = plt.figure()
        plt.pie(temp_df['amount'], labels=temp_df['city'], autopct="%1.1f%%")
        st.pyplot(fig2)

    with col1:
        st.header("Top Startups According to Funding")

        selected_option1 = st.selectbox('Select Year', year_list, key='year1_select')

        if selected_option1 == 'Overall':
            my_df = df.groupby('startup')['amount'].sum().sort_values(ascending=False).head(10)
        else:
            my_df = df[df['year'] == selected_option1]
            my_df = my_df.groupby('startup')['amount'].sum().sort_values(ascending=False).head(10)

        fig1 = plt.figure()
        plt.bar(my_df.index, my_df.values)
        plt.xticks(rotation=90)
        st.pyplot(fig1)

    with col2:
        st.header("Top Startups According to Rounds")

        selected_option1 = st.selectbox('Select Year', year_list, key='year2_select')

        if selected_option1 == 'Overall':
            my_df = df.groupby('startup')['round'].count().sort_values(ascending=False).head(10)
        else:
            my_df = df[df['year'] == selected_option1]
            my_df = my_df.groupby('startup')['round'].count().sort_values(ascending=False).head(10)

        fig1 = plt.figure()
        plt.bar(my_df.index, my_df.values)
        plt.xticks(rotation=90)
        st.pyplot(fig1)

    col1, col2 = st.columns(2)

    with col1:
        st.header("No of Startups According to City")

        selected_option1 = st.selectbox('Select Year', year_list, key='year3_select')

        if selected_option1 == 'Overall':
            my_df = df.groupby(['city'])['startup'].count().sort_values(ascending=False).head(10)
        else:
            my_df = df[df['year'] == selected_option1]
            my_df = my_df.groupby(['city'])['startup'].count().sort_values(ascending=False).head(10)

        fig1 = plt.figure()
        # plt.bar(my_df.index, my_df.values)
        # plt.xticks(rotation=90)
        plt.pie(my_df.values,labels=my_df.index,autopct="%1.1f%%")
        st.pyplot(fig1)

    with col2:
        st.header("Top Startups According to Vertical")

        selected_option1 = st.selectbox('Select Year', year_list, key='year4_select')

        if selected_option1 == 'Overall':
            my_df = df.groupby(['vertical'])['amount'].count().sort_values(ascending=False).head(10)
        else:
            my_df = df[df['year'] == selected_option1]
            my_df = my_df.groupby(['vertical'])['amount'].count().sort_values(ascending=False).head(10)

        fig1 = plt.figure()
        plt.bar(my_df.index, my_df.values)
        plt.xticks(rotation=90)
        st.pyplot(fig1)

def load_investor_details(investor):
    st.title(investor)

    # load investor recent 5 investments
    last5_df = df[df['investor'].str.contains(investor)].head()[['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)

    col1,col2 = st.columns(2)
    with col1:
        #biggest investments
        big_series = df[df['investor'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head(10)
        st.subheader("Biggest Investments")
        fig = plt.figure()
        plt.bar(big_series.index,big_series.values)
        plt.xticks(rotation=90)
        st.pyplot(fig)

    with col2:
        vertical_series = df[df['investor'].str.contains(investor)].groupby('vertical')['amount'].sum().sort_values(ascending=False).head(10)
        st.subheader("Sectors Invested in")
        fig1 = plt.figure()
        plt.pie(vertical_series,labels=vertical_series.index,autopct="%1.1f%%",pctdistance=0.7,labeldistance=1.2,startangle=140)
        st.pyplot(fig1)

    col1,col2 = st.columns(2)
    with col1:
        round_series = df[df['investor'].str.contains(investor)].groupby('round')['amount'].sum().sort_values(ascending=False).head(10)
        st.subheader("Rounds Invested in")
        fig1 = plt.figure()
        plt.bar(round_series.index, round_series.values)
        plt.xticks(rotation=90)
        st.pyplot(fig1)

    with col2:
        city_series = df[df['investor'].str.contains(investor)].groupby('city')['amount'].sum().sort_values(ascending=False).head(10)
        st.subheader("Cities Invested in")
        fig1 = plt.figure()
        plt.pie(city_series,labels=city_series.index,autopct="%1.1f%%")
        st.pyplot(fig1)

    col1, col2 = st.columns(2)
    with col1:
        year_series = df[df['investor'].str.contains(investor)].groupby('year')['amount'].sum()
        st.subheader("YOY Investment")
        fig1 = plt.figure()
        plt.plot(year_series.index,year_series.values)
        st.pyplot(fig1)

def load_startup_analysis(startup):

    st.title(startup)
    industry = df[df['startup'] == startup]['vertical'].values[0]
    sub_industry = df[df['startup'] == startup]['subvertical'].values[0]
    city = df[df['startup'] == startup]['city'].values[0]

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("Industry")
        st.markdown(f"**{industry}**")
    with col2:
        st.markdown("Sub-Industry")
        st.markdown(f"**{sub_industry}**")
    with col3:
        st.markdown("City")
        st.markdown(f"**{city}**")

    last5_df = df[df['startup'].str.contains(startup)].head()[
        ['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('Most Recent Fundings')
    st.dataframe(last5_df)

    col1, col2 = st.columns(2)
    with col1:
        # biggest investments
        big_series = df[df['startup'].str.contains(startup)].groupby('investor')['amount'].sum().sort_values(ascending=False).head(10)
        st.subheader("Biggest Fundings")
        fig = plt.figure()
        plt.bar(big_series.index, big_series.values)
        plt.xticks(rotation=90)
        st.pyplot(fig)

    with col2:
        vertical_series = df[df['startup'].str.contains(startup)].groupby('vertical')['amount'].sum().head(10)
        st.subheader("Sectors Invested in the Startup")
        fig1 = plt.figure()
        plt.pie(vertical_series, labels=vertical_series.index, autopct="%1.1f%%")
        st.pyplot(fig1)

    col1, col2 = st.columns(2)
    with col1:
        round_series = df[df['startup'].str.contains(startup)].groupby('round')['amount'].sum().head(10)
        st.subheader("Rounds Investments")
        fig1 = plt.figure()
        plt.pie(round_series, labels=round_series.index, autopct="%1.1f%%")
        st.pyplot(fig1)

    with col2:
        city_series = df[df['startup'].str.contains(startup)].groupby('city')['amount'].sum().head(10)
        st.subheader("Cities Investments")
        fig1 = plt.figure()
        plt.pie(city_series, labels=city_series.index, autopct="%1.1f%%")
        st.pyplot(fig1)

    col1, col2 = st.columns(2)
    with col1:
        year_series = df[df['startup'].str.contains(startup)].groupby('year')['amount'].sum()
        st.subheader("YOY Investment")
        fig1 = plt.figure()
        plt.plot(year_series.index, year_series.values)
        st.pyplot(fig1)
