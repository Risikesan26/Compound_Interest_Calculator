import streamlit as st
import pandas as pd
import numpy as np

st.title("💰 Compound Interest Calculator")
st.write("### 🧾 Input Data")


col1, col2 = st.columns(2)
initial_deposit = col1.number_input("Initial Deposit (RM)", min_value=0.0)
monthly_deposit = col1.number_input("Monthly Deposit (RM)", min_value=0.0)
years = int(col2.number_input("How many years", min_value=0))
annual_rate = col2.number_input("Interest Rate (% per annum)", min_value=0.0)


total_amount = initial_deposit
annual_rate_decimal = annual_rate / 100
results = []

for year in range(1, years + 1):
    for month in range(12):
        total_amount += monthly_deposit
        total_amount *= (1 + annual_rate_decimal / 12)
    results.append({"Year": year, "Total Amount": round(total_amount, 2)})


df = pd.DataFrame(results)


st.write("### 💸 Total")
if years > 0:
    st.write(f"Total amount after {years} years is: **RM {total_amount:,.2f}**")

if years > 0:
    st.write("### 📈 Growth Over Time")
    st.line_chart(df.set_index("Year"))

st.download_button("Download CSV", df.to_csv(index=False), file_name="compound_interest.csv")

with st.sidebar:
    st.header("📘 Learn More")

    st.subheader("📌 How Compound Interest Works")
    st.markdown("""
    Compound interest means you earn interest on both the money you invest and the interest you’ve already earned. 
    The formula used is:

    \n**A = P(1 + r/n)^(nt)**  
    Where:  
    - *P* = initial principal  
    - *r* = annual interest rate  
    - *n* = number of compounding periods per year  
    - *t* = number of years
    """)

    st.subheader("⏳ Why Starting Early Matters")
    st.markdown("""
    The earlier you start, the more time your money has to grow exponentially. 
    Even small monthly deposits grow significantly over decades thanks to compounding.
    """)

    st.info("💡 Example: RM100/month for 30 years at 6% ≈ RM100,000+.")

st.write("### 🎥 Learn About Compound Interest")

st.video("https://www.youtube.com/watch?v=wf91rEGw88Q")
st.video("https://www.youtube.com/watch?v=jTW777ENc3c&pp=ygUXY29tcG91bmQgaW50ZXJlc3QgYmFzaWM%3D")
