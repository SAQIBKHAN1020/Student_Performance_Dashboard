import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


st.title("Student Performance Dashboard")

name=st.text_input("Enter The Name:")
english=st.number_input("English Marks",0,100)
math=st.number_input("Math Marks",0,100)
science=st.number_input("Science Marks",0,100)

if st.button("Analyze"):
    df=pd.DataFrame({
        "Name":[name],
        "English":[english],
        "Math":[math],
        "Science":[science]
    })

    df["Average"]=(df["English"] + df["Math"] + df["Science"]) / 3 

    df["Status"]=df["Average"].apply(lambda x: 1 if x >=50 else 0 )

    st.dataframe(df)

    fig,ax = plt.subplots()

    ax.bar(["English","Math","Science"],[english,math,science])
    st.pyplot(fig)


    data = pd.DataFrame({
        "Math": [80, 40, 70, 30, 90, 50],
        "English": [75, 35, 65, 40, 88, 55],
        "Science": [78, 30, 60, 45, 92, 50],
        "Status": [1, 0, 1, 0, 1, 1]
    })

    X=data[["Math","English","Science"]]
    y=data["Status"]

    model=LogisticRegression()
    model.fit(X,y)

    prediction = model.predict([[english,math,science]])


    if prediction[0]==1:
        st.success("ML Prediction:Pass")
    else:
        st.success("Ml Prediction : Fail")
    st.download_button("Download CSV",df.to_csv(index=False),"student_data.csv","text/csv")