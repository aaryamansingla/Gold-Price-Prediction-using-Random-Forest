import streamlit as st
import pandas as pd
import pickle

df = pd.read_csv('C:\\Users\\welcome\\Desktop\\Machine learning\\Gold Price Prediction using Machine learning\\Gold_Price_Data\\gld_price_data.csv')
st.write("# Gold Price Prediction Using Random Forest Regressor")
ml_model = pickle.load(open("C:\\Users\\welcome\\Desktop\\Machine learning\\Gold Price Prediction using Machine learning\\Gold_Price_Data\\Pickle_RL_model.pkl", "rb")) #load the model

##create function for User input
def get_user_input():
    SPX = st.sidebar.slider("Enter the value of Standard & Poor's 500 Index",
                          df["SPX"].min(),
                          df["SPX"].max(),
                          df["SPX"].mean())
    USO = st.sidebar.slider("Enter the value of United States Oil",
                          df["USO"].min(),
                          df["USO"].max(),
                          df["USO"].mean())
    SLV = st.sidebar.slider("Enter the value of iShares Silver Trust",
                           df["SLV"].min(),
                           df["SLV"].max(),
                           df["SLV"].mean())
    EUR_USD = st.sidebar.slider("Enter the value of European Unioun Euro against United States Dollar",
                           df["EUR/USD"].min(),
                           df["EUR/USD"].max(),
                           df["EUR/USD"].mean())
    features = pd.DataFrame({"Standard & Poor's 500 Index":SPX,
                             "United States Oil":USO,
                             "iShares Silver Trust":SLV,
                             "European Unioun Euro against United States Dollar":EUR_USD}, index = [0])
    return features

input_df = get_user_input() #get user input from sidebar
prediction = ml_model.predict(input_df) #get predicitions

#display predictions
st.subheader("Prediction of gold price")
st.write("**The estimated price of gold is: $**",str(round(prediction[0],2)))
st.write("Disclaimer: THE VALUE MAY FLUCTUATE WITH A VERY SMALL DIFFERENCE BECAUSE THE PRICE OF GOLD IS SUBJECT TO THE MARKET CHANGES")
