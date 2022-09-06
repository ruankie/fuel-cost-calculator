import streamlit as st
from calculator import FuelCostCalculator

st.set_page_config(
    page_title="Fuel Cost Calculator", 
    page_icon=":car:",
    layout="centered",
)

with st.container():
    # title
    st.write("# :car: Fuel Cost Calculator")

    # description
    st.write("Calculate fuel cost for every km you drive.")

    # input fields
    st.write("---")
    base_currency = st.selectbox("💵 Base currency", ("R", "$", "€", "£"))
    tank_size = float(st.text_input(label="💧 Fuel tank size [L]", value="40.0"))
    distance_on_tank = float(st.text_input(label="🌍 Distance you can drive on a full tank [km]", value="450.0"))
    fuel_cost = float(st.text_input(label=f"⛽ Fuel cost [{base_currency}/L]", value="24.38"))

    # calculate button
    st.write("---")
    if st.button("Calculate"):
        calc = FuelCostCalculator(
            tank_size=tank_size,
            distance_on_tank=distance_on_tank,
            fuel_cost=fuel_cost,
            base_currency=base_currency
        )
        cost = calc.calculate_cost_per_km()
        st.write(f"### Cost per km: {calc.base_currency} {round(cost, 2)}")
    else:
        st.write("*Click Calculate when ready.*")
    st.write("---")
