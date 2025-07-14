import streamlit as st

def calculate_investment_value(years, initial_investment, monthly_investment,
                                annual_increase_percent, expected_annual_return, annual_fee):
    effective_annual_return = expected_annual_return - annual_fee
    monthly_return = (1 + effective_annual_return / 100) ** (1 / 12) - 1
    total_months = years * 12

    future_value = initial_investment * (1 + monthly_return) ** total_months
    current_monthly_investment = monthly_investment

    for month in range(1, total_months + 1):
        months_remaining = total_months - month
        future_value += current_monthly_investment * ((1 + monthly_return) ** months_remaining)

        if month % 12 == 0:
            current_monthly_investment *= 1 + (annual_increase_percent / 100)

    return round(future_value, 2)


# --- Streamlit UI ---
st.title("📈 Simple Investment Calculator")

years = st.slider("Investment Timeframe (Years)", 1, 50, 0)
initial = st.number_input("Day 1 Investment ($)", value=0)
monthly = st.number_input("Monthly Investment ($)", value=200)
increase = st.slider("Annual Increase in Monthly Investment (%)", 0, 20, 0)
return_rate = st.slider("Expected Annual Return (%)", 0.0, 20.0, 0)
fee = st.slider("Annual Bank Fee (%)", 0.0, 5.0, 0)

if st.button("Calculate"):
    result = calculate_investment_value(
        years, initial, monthly, increase, return_rate, fee
    )
    st.success(f"📊 Your investment will be worth: **${result:,.2f}**")
