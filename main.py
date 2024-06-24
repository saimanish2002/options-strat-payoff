import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#URL for clicable hyperlink 'My Name'
linkedin_url = "https://www.linkedin.com/in/saimanish-prabhakar-3074351a0/"

st.sidebar.title("Options Strategies Payoff Calculator")

# App credits (hyperlink to Linkedin page)
st.sidebar.markdown("<div style='background-color: black; color: green; padding: 3px; border-radius: 3px; font-size: 12px; display: inline-block;'>Created by:</div>", unsafe_allow_html=True)
st.sidebar.markdown(" ")
st.sidebar.markdown(f"<div style='background-color: black; color: white; padding: 3px; border-radius: 3px; font-size: 12px; display: inline-block; margin-left: 0px;'><a href='{linkedin_url}' target='_blank' style='color: orange; text-decoration: none;'>Saimanish Prabhakar</a></div>", unsafe_allow_html=True)

st.sidebar.markdown("---")

# Valdates whether strategy is != '-' to begin animation for changing strategy selection
if "strategy_changed" not in st.session_state:
    st.session_state.strategy_changed = False
    st.session_state.last_strategy = "-"

# Selectbox for user to choose strategy
strategy = st.sidebar.selectbox("Select Strategy", ["-", "Long Call", "Short Call", "Long Put", "Short Put", "Bull Call Spread", "Bear Put Spread", "Long Straddle", "Long Strangle", "Strip", "Strap", "Long Butterfly"])
st.sidebar.markdown("<div style='background-color: black; color: red; padding: 5px; border-radius: 5px; font-size: 12px; display: inline-block;'>To RESET all strategy parameters, re-select strategy as ' - ' and continue using the app.</div>", unsafe_allow_html=True)
st.sidebar.markdown("---")

if strategy == "Long Call":
        
        # Defining the functions used to calculate the strategy
        # Each strategy follows the same structual format
        # 'LC' in this case stands for Long Call, other strategies have different acronyms
        # Focus on 'Call Values', 'Net-Payoff' and 'Break-Even Point (BEP)' functions for strategy's output accuracy
        
        def calculate_long_call_payoff(LC_strike_price, LC_premium, LC_expiration_prices):
            LC_payoffs = []
            for LC_expiration_price in LC_expiration_prices:
                LC_call_value = max(LC_expiration_price - LC_strike_price, 0)
                LC_net_payoff = LC_call_value - LC_premium
                LC_payoffs.append((LC_expiration_price, LC_premium, LC_call_value, LC_net_payoff))

            # Columns for the net-payoff table
            LC_payoff_table = pd.DataFrame(LC_payoffs, columns=['Expiration Price', 'Premium', 'Call Value', 'Net Payoff'])
            return LC_payoff_table

        # Allows user to input numbers for strategy payoff calculation
        st.sidebar.caption("Please adjust the strategy parameters as required")
        LC_strike_price =st.sidebar.number_input("Strike Price", value=100.0,step=1.0)
        LC_premium = st.sidebar.number_input("Premium", value=5.0, step=0.1)
        st.sidebar.markdown("---")
        st.sidebar.caption("Please adjust the payoff table and graph parameters as required")
        LC_start_price = st.sidebar.number_input("Start Expiration Price", value=60.0, step=1.0)
        LC_end_price = st.sidebar.number_input("End Expiration Price", value=140.0, step=1.0)
        LC_step_size = st.sidebar.number_input("Step Size", value=5.0, step=1.0)
        
        # Ensures that strike prices are within range of expiration prices for computational accuracy
        if LC_start_price >= LC_strike_price:
            st.error("Start Expiration Price should be lower than the Strike Price.")
        elif LC_end_price <= LC_strike_price:
            st.error("End Expiration Price should be higher than the Strike Price.")
        else:

            LC_expiration_prices = np.arange(LC_start_price, LC_end_price + LC_step_size, LC_step_size)
            LC_payoff_table = calculate_long_call_payoff(LC_strike_price, LC_premium, LC_expiration_prices)

            # Create net payoff table
            st.subheader("Long Call: Net-Payoff Table")
            st.table(LC_payoff_table)

            st.markdown("---")

            # Create net payoff graph
            st.subheader("Long Call: Net-Payoff Graph")
            fig, ax = plt.subplots()

            ax.plot(LC_payoff_table['Expiration Price'], LC_payoff_table['Net Payoff'])
            ax.set_xlabel('Expiration Price')
            ax.set_ylabel('Net Payoff')
            ax.axhline(y=0, color='r', linestyle='--')

            # Calculating the break-even point
            LC_bep = LC_strike_price + LC_premium

            # Find the closest 'Expiration Price' value to bep
            closest_index = abs(LC_payoff_table['Expiration Price'] - LC_bep).idxmin()
            LC_bep_payoff = LC_payoff_table.loc[closest_index, 'Net Payoff']

            # Plot the break-even point
            ax.plot(LC_bep, LC_bep_payoff, 'go', markersize=10, label='Break Even Point')
            ax.annotate(f'BEP: {LC_bep:.2f}', xy=(LC_bep, LC_bep_payoff), xytext=(LC_bep + 5, LC_bep_payoff + 2),
                        arrowprops=dict(facecolor='black', arrowstyle='->'))

            st.pyplot(fig)

elif strategy == "Short Call":

        # Defining the functions used to calculate the strategy
        # Each strategy follows the same structual format
        # 'SC' in this case stands for Short Call, other strategies have different acronyms
        # Focus on 'Call Values', 'Net-Payoff' and 'Break-Even Point (BEP)' functions for strategy's output accuracy

        def calculate_short_call_payoff(SC_strike_price, SC_premium, SC_expiration_prices):
            SC_payoffs = []
            for SC_expiration_price in SC_expiration_prices:
                SC_call_value = max(0,SC_expiration_price - SC_strike_price)
                SC_net_payoff = SC_premium - SC_call_value
                SC_payoffs.append((SC_expiration_price, SC_premium, SC_call_value, SC_net_payoff))

            # Columns for the net-payoff table
            SC_payoff_table = pd.DataFrame(SC_payoffs, columns=['Expiration Price', 'Premium', 'Call value', 'Net Payoff'])
            return SC_payoff_table

        # Allows user to input numbers for strategy payoff calculation
        st.sidebar.caption("Please adjust the strategy parameters as required")
        SC_strike_price = st.sidebar.number_input("Strike Price", value=100.0, step=1.0)
        SC_premium = st.sidebar.number_input("Premium", value=5.0, step=0.1)
        st.sidebar.markdown("---")
        st.sidebar.caption("Please adjust the payoff table and graph parameters as required")
        SC_start_price = st.sidebar.number_input("Start Expiration Price", value=60.0, step=1.0)
        SC_end_price = st.sidebar.number_input("End Expiration Price", value=140.0, step=1.0)
        SC_step_size = st.sidebar.number_input("Step Size", value=5.0, step=1.0)

        # Ensures that strike prices are within range of expiration prices for computational accuracy
        if SC_start_price >= SC_strike_price:
            st.error("Start Expiration Price should be lower than the Strike Price.")
        elif SC_end_price <= SC_strike_price:
            st.error("End Expiration Price should be higher than the Strike Price.")
        else:

            SC_expiration_prices = np.arange(SC_start_price, SC_end_price + SC_step_size, SC_step_size)
            SC_payoff_table = calculate_short_call_payoff(SC_strike_price,SC_premium, SC_expiration_prices)

            # Create net-Payoff Table
            st.subheader("Short Call: Net-Payoff Table")
            st.table(SC_payoff_table)

            st.markdown("---")

            # Create net-Payoff Graph
            st.subheader("Short Call: Net-Payoff Graph")
            fig, ax = plt.subplots()

            ax.plot(SC_payoff_table['Expiration Price'], SC_payoff_table['Net Payoff'])
            ax.set_xlabel('Expiration Price')
            ax.set_ylabel('Net Payoff')
            ax.axhline(y=0, color = 'r', linestyle='--')

            # Calculating the break-even point
            SC_bep = SC_strike_price + SC_premium

            # Find the closest 'Expiration Price' value to bep
            closest_index = abs(SC_payoff_table['Expiration Price'] - SC_bep).idxmin()
            SC_bep_payoff = SC_payoff_table.loc[closest_index, 'Net Payoff']

            # Plot the break-even point
            ax.plot(SC_bep, SC_bep_payoff, 'go', markersize=10, label='Break Even Point')
            ax.annotate(f'BEP: {SC_bep:.2f}', xy=(SC_bep, SC_bep_payoff), xytext=(SC_bep + 5, SC_bep_payoff + 2),
                        arrowprops=dict(facecolor='black', arrowstyle='->'))

            st.pyplot(fig)

elif strategy == "Long Put":

        # Defining the functions used to calculate the strategy
        # Each strategy follows the same structual format
        # 'LP' in this case stands for Long Put, other strategies have different acronyms
        # Focus on 'Put Values', 'Net-Payoff' and 'Break-Even Point (BEP)' functions for strategy's output accuracy

        def calculate_long_put_payoff(LP_strike_price, LP_premium, LP_expiration_prices):
            LP_payoffs = []
            for LP_expiration_price in LP_expiration_prices:
                LP_put_value = max(LP_strike_price - LP_expiration_price,0)
                LP_net_payoff = LP_put_value - LP_premium
                LP_payoffs.append((LP_expiration_price, LP_premium, LP_put_value, LP_net_payoff))
            
            # Columns for the net-payoff table
            LP_payoff_table = pd.DataFrame(LP_payoffs, columns=['Expiration Price', 'Premium', 'Put value', 'Net Payoff'])
            return LP_payoff_table
        
        # Allows user to input numbers for strategy payoff calculation
        st.sidebar.caption("Please adjust the strategy parameters as required")
        LP_strike_price =st.sidebar.number_input("Strike Price", value=100.0,step=1.0)
        LP_premium = st.sidebar.number_input("Premium", value=5.0, step=0.1)
        st.sidebar.markdown("---")
        st.sidebar.caption("Please adjust the payoff table and graph parameters as required")
        LP_start_price = st.sidebar.number_input("Start Expiration Price", value=60.0, step=1.0)
        LP_end_price = st.sidebar.number_input("End Expiration Price", value=140.0, step=1.0)
        LP_step_size = st.sidebar.number_input("Step Size", value=5.0, step=1.0)

        # Ensures that strike prices are within range of expiration prices for computational accuracy
        if LP_start_price >= LP_strike_price:
            st.error("Start Expiration Price should be lower than the Strike Price.")
        elif LP_end_price <= LP_strike_price:
            st.error("End Expiration Price should be higher than the Strike Price.")
        else:

            LP_expiration_prices = np.arange(LP_start_price, LP_end_price + LP_step_size, LP_step_size)
            LP_payoff_table = calculate_long_put_payoff(LP_strike_price, LP_premium, LP_expiration_prices)

            # Create net payoff table
            st.subheader("Long Put: Net-Payoff Table")
            st.table(LP_payoff_table)

            st.markdown("---")

            # Create net payoff graph
            st.subheader("Long Put: Net-Payoff Graph")
            fig, ax = plt.subplots()

            ax.plot(LP_payoff_table['Expiration Price'], LP_payoff_table['Net Payoff'])
            ax.set_xlabel('Expiration Price')
            ax.set_ylabel('Net Payoff')
            ax.axhline(y=0, color='r', linestyle='--')

            # Calculating the break-even point
            LP_bep = LP_strike_price - LP_premium

            # Find the closest 'Expiration Price' value to bep
            closest_index = abs(LP_payoff_table['Expiration Price'] - LP_bep).idxmin()
            LP_bep_payoff = LP_payoff_table.loc[closest_index, 'Net Payoff']

            # Plot the break-even point
            ax.plot(LP_bep, LP_bep_payoff, 'go', markersize=10, label='Break Even Point')
            ax.annotate(f'BEP: {LP_bep:.2f}', xy=(LP_bep, LP_bep_payoff), xytext=(LP_bep + 5, LP_bep_payoff + 2),
                        arrowprops=dict(facecolor='black', arrowstyle='->'))

            st.pyplot(fig)

elif strategy == "Short Put":

        # Defining the functions used to calculate the strategy
        # Each strategy follows the same structual format
        # 'SP' in this case stands for Short Put, other strategies have different acronyms
        # Focus on 'Put Values', 'Net-Payoff' and 'Break-Even Point (BEP)' functions for strategy's output accuracy

        def calculate_short_put_payoff(SP_strike_price, SP_premium, SP_expiration_prices):
            SP_payoffs = []
            for SP_expiration_price in SP_expiration_prices:
                SP_put_value = max(SP_strike_price - SP_expiration_price, 0)
                SP_net_payoff = SP_premium - SP_put_value
                SP_payoffs.append((SP_expiration_price, SP_premium, SP_put_value, SP_net_payoff))

            # Columns for the net-payoff table
            SP_payoff_table = pd.DataFrame(SP_payoffs, columns=['Expiration Price', 'Premium', 'Put value', 'Net Payoff'])
            return SP_payoff_table    

        # Allows user to input numbers for strategy payoff calculation
        st.sidebar.caption("Please adjust the strategy parameters as required")
        SP_strike_price = st.sidebar.number_input("Strike Price", value=100.0, step=1.0)
        SP_premium = st.sidebar.number_input("Premium", value=5.0, step=0.1)
        st.sidebar.markdown("---")
        st.sidebar.caption("Please adjust the payoff table and graph parameters as required")
        SP_start_price = st.sidebar.number_input("Start Expiration Price", value=60.0, step=1.0)
        SP_end_price = st.sidebar.number_input("End Expiration Price", value=140.0, step=1.0)
        SP_step_size = st.sidebar.number_input("Step Size", value=5.0, step=1.0)

        # Ensures that strike prices are within range of expiration prices for computational accuracy
        if SP_start_price >= SP_strike_price:
            st.error("Start Expiration Price should be lower than the Strike Price.")
        elif SP_end_price <= SP_strike_price:
            st.error("End Expiration Price should be higher than the Strike Price.")
        else:

            SP_expiration_prices = np.arange(SP_start_price, SP_end_price + SP_step_size, SP_step_size)
            SP_payoff_table = calculate_short_put_payoff(SP_strike_price,SP_premium, SP_expiration_prices)

            # Create net-payoff table
            st.subheader("Short Put: Net-Payoff Table")
            st.table(SP_payoff_table)

            st.markdown("---")

            # Create net-payoff graph
            st.subheader("Short Put: Net-Payoff Graph")
            fig, ax = plt.subplots()

            ax.plot(SP_payoff_table['Expiration Price'], SP_payoff_table['Net Payoff'])
            ax.set_xlabel('Expiration Price')
            ax.set_ylabel('Net Payoff')
            ax.axhline(y=0, color = 'r', linestyle='--')

            # Calculating the break-even point
            SP_bep = SP_strike_price - SP_premium

            # Find the closest 'Expiration Price' value to bep
            closest_index = abs(SP_payoff_table['Expiration Price'] - SP_bep).idxmin()
            SP_bep_payoff = SP_payoff_table.loc[closest_index, 'Net Payoff']

            # Plots the break-even point
            ax.plot(SP_bep, SP_bep_payoff, 'go', markersize=10, label='Break Even Point')
            ax.annotate(f'BEP: {SP_bep:.2f}', xy=(SP_bep, SP_bep_payoff), xytext=(SP_bep + 5, SP_bep_payoff + 2),
                        arrowprops=dict(facecolor='black', arrowstyle='->'))

            st.pyplot(fig)

elif strategy == "Bull Call Spread":

        # Defining the functions used to calculate the strategy
        # Each strategy follows the same structual format
        # 'BCS' in this case stands for Bull Call Spread, other strategies have different acronyms
        # Focus on 'Net-Premium','Call 1 and Call 2 Values', 'Net-Payoff' and 'Break-Even Point (BEP)' functions for strategy's output accuracy

        def calculate_bull_call_spread_payoff(BCS_lower_strike, BCS_higher_strike, BCS_premium_call1, BCS_premium_call2, BCS_expiration_prices):
            BCS_payoffs = []
            BCS_net_premium = BCS_premium_call1 - BCS_premium_call2
            for BCS_expiration_price in BCS_expiration_prices:
                BCS_call1_value = max(BCS_expiration_price - BCS_lower_strike, 0)
                BCS_call2_value = max(BCS_expiration_price - BCS_higher_strike, 0)
                BCS_net_payoff = BCS_call1_value - BCS_call2_value - BCS_net_premium
                BCS_payoffs.append((BCS_expiration_price, BCS_net_premium, BCS_call1_value, BCS_call2_value, BCS_net_payoff))
        
            # Columns for the net-payoff table
            BCS_payoff_table = pd.DataFrame(BCS_payoffs, columns=['Expiration Price', 'Net Premium', 'Call 1 Value', 'Call 2 Value', 'Net Payoff'])
            return BCS_payoff_table
        
        # Allows user to input numbers for strategy payoff calculation
        st.sidebar.caption("Please adjust the strategy parameters as required")
        BCS_lower_strike = st.sidebar.number_input("Call 1: Lower Strike Price (ITM)", value=90.0, step=1.0)
        BCS_higher_strike = st.sidebar.number_input("Call 2: Higher Strike Price (OTM)", value=110.0, step=1.0)
        BCS_premium_call1 = st.sidebar.number_input("Call 1: Higher Premium (ITM)", value=8.0, step=0.1)
        BCS_premium_call2 = st.sidebar.number_input("Call 2: Lower Premium (OTM)", value=5.0, step=0.1)
        st.sidebar.markdown("---")
        st.sidebar.caption("Please adjust the payoff table and graph parameters as required")
        BCS_start_price = st.sidebar.number_input("Start Expiration Price", value=80.0, step=1.0)
        BCS_end_price = st.sidebar.number_input("End Expiration Price", value=120.0, step=1.0)
        BCS_step_size = st.sidebar.number_input("Step Size", value=5.0, step=1.0)

        # Ensures that strike prices are within range of expiration prices for computational accuracy
        # Additionally guides user to input premium float values that align with strategy's principles
        if BCS_start_price >= BCS_lower_strike or BCS_start_price >= BCS_higher_strike:
            st.error("Start Expiration Price should be lower than both Strike Prices.")
        elif BCS_end_price <= BCS_lower_strike or BCS_end_price <= BCS_higher_strike:
            st.error("End Expiration Price should be higher than both Strike Prices.")
        elif BCS_premium_call1 <= BCS_premium_call2:
            st.error("Call 1 premium should be higher than Call 2")
        elif BCS_premium_call2 >= BCS_premium_call1:
            st.error("Call 2 premium should be lower than Call 1")
        else:

            BCS_expiration_prices = np.arange(BCS_start_price, BCS_end_price + BCS_step_size, BCS_step_size)
            BCS_payoff_table = calculate_bull_call_spread_payoff(BCS_lower_strike, BCS_higher_strike, BCS_premium_call1, BCS_premium_call2, BCS_expiration_prices)
            
            # Create net-payoff table
            st.subheader("Bull Call Spread: Net-Payoff Table")
            st.table(BCS_payoff_table)
            
            st.markdown("---")

            # Create net-payoff graph
            st.subheader("Bull Call Spread: Net-Payoff Graph")
            fig, ax = plt.subplots()

            ax.plot(BCS_payoff_table['Expiration Price'], BCS_payoff_table['Net Payoff'])
            ax.set_xlabel('Expiration Price')
            ax.set_ylabel('Net Payoff')
            ax.axhline(y=0, color='r', linestyle='--')

            # Calculating the break-even point
            BCS_bep = BCS_lower_strike + BCS_payoff_table['Net Premium'].iloc[0]
            
            # Find the closest 'Expiration Price' value to bep
            closest_index = abs(BCS_payoff_table['Expiration Price'] - BCS_bep).idxmin()
            BCS_bep_payoff = BCS_payoff_table.loc[closest_index, 'Net Payoff']
            
            # Plots the break-even point
            ax.plot(BCS_bep, BCS_bep_payoff, 'go', markersize=10, label='Break Even Point')
            ax.annotate(f'BEP: {BCS_bep:.2f}', xy=(BCS_bep, BCS_bep_payoff), xytext=(BCS_bep + 5, BCS_bep_payoff + 2),
                arrowprops=dict(facecolor='black', arrowstyle='->'))
            
            st.pyplot(fig)

elif strategy == "Bear Put Spread":
     
        # Defining the functions used to calculate the strategy
        # Each strategy follows the same structual format
        # 'BPS' in this case stands for Bear Put Spread, other strategies have different acronyms
        # Focus on 'Net-Premium','Put 1 and Put 2 Values', 'Net-Payoff' and 'Break-Even Point (BEP)' functions for strategy's output accuracy

        def calculate_bear_put_spread_payoff(BPS_higher_strike, BPS_lower_strike, BPS_premium_put1, BPS_premium_put2, BPS_expiration_prices):
            BPS_payoffs = []
            BPS_net_premium = BPS_premium_put2 - BPS_premium_put1
            for BPS_expiration_price in BPS_expiration_prices:
                BPS_put1_value = max(BPS_higher_strike - BPS_expiration_price, 0)
                BPS_put2_value = max(BPS_lower_strike - BPS_expiration_price, 0)
                BPS_net_payoff = BPS_put2_value - BPS_put1_value + BPS_net_premium
                BPS_payoffs.append((BPS_expiration_price, BPS_net_premium, BPS_put1_value, BPS_put2_value, BPS_net_payoff))
            
            # Columns for the net-payoff table
            BPS_payoff_table = pd.DataFrame(BPS_payoffs, columns=['Expiration Price', 'Net Premium', 'Put 1 Value', 'Put 2 Value', 'Net Payoff'])
            return BPS_payoff_table
    
        # Allows user to input numbers for strategy payoff calculation
        st.sidebar.caption("Please adjust the strategy parameters as required")
        BPS_higher_strike = st.sidebar.number_input("Put 1: Higher Strike Price (ITM)", value=110.0, step=1.0)
        BPS_lower_strike = st.sidebar.number_input("Put 2: Lower Strike Price (OTM)", value=90.0, step=1.0)
        BPS_premium_put1 = st.sidebar.number_input("Put 1: Higher Premium (ITM)", value=8.0, step=0.1)
        BPS_premium_put2 = st.sidebar.number_input("Put 2: Lower Premium (OTM)", value=5.0, step=0.1)
        st.sidebar.markdown("---")
        st.sidebar.caption("Please adjust the payoff table and graph parameters as required")
        BPS_start_price = st.sidebar.number_input("Start Expiration Price", value=80.0, step=1.0)
        BPS_end_price = st.sidebar.number_input("End Expiration Price", value=120.0, step=1.0)
        BPS_step_size = st.sidebar.number_input("Step Size", value=5.0, step=1.0)

        # Ensures that strike prices are within range of expiration prices for computational accuracy
        # Additionally guides user to input premium float values that align with strategy's principles
        if BPS_start_price >= BPS_lower_strike or BPS_start_price >= BPS_higher_strike:
            st.error("Start Expiration Price should be lower than both Strike Prices.")
        elif BPS_end_price <= BPS_lower_strike or BPS_end_price <= BPS_higher_strike:
            st.error("End Expiration Price should be higher than both Strike Prices.")
        elif BPS_premium_put1 <= BPS_premium_put2:
            st.error("Put 1 premium should be higher than Put 2")
        elif BPS_premium_put2 >= BPS_premium_put1:
            st.error("Put 2 premium should be lower than Put 1")
        else:

            BPS_expiration_prices = np.arange(BPS_start_price, BPS_end_price + BPS_step_size, BPS_step_size)
            BPS_payoff_table = calculate_bear_put_spread_payoff(BPS_lower_strike, BPS_higher_strike, BPS_premium_put1, BPS_premium_put2, BPS_expiration_prices)
            
            # Create net-payoff table
            st.subheader("Bear Put Spread: Net-Payoff Table")
            st.table(BPS_payoff_table)

            st.markdown("---")

            # Create net-payoff graph
            st.subheader("Bear Put Spread: Net-Payoff Graph")
            fig, ax = plt.subplots()

            ax.plot(BPS_payoff_table['Expiration Price'], BPS_payoff_table['Net Payoff'])
            ax.set_xlabel('Expiration Price')
            ax.set_ylabel('Net Payoff')
            ax.axhline(y=0, color='r', linestyle='--')

            # Calculating the break-even point
            BPS_bep = BPS_higher_strike + BPS_payoff_table['Net Premium'].iloc[0]
            
            # Find the closest 'Expiration Price' value to bep
            closest_index = abs(BPS_payoff_table['Expiration Price'] - BPS_bep).idxmin()
            BPS_bep_payoff = BPS_payoff_table.loc[closest_index, 'Net Payoff']
            
            # Plots the break-even point
            ax.plot(BPS_bep, BPS_bep_payoff, 'go', markersize=10, label='Break Even Point')
            ax.annotate(f'BEP: {BPS_bep:.2f}', xy=(BPS_bep, BPS_bep_payoff), xytext=(BPS_bep + 5, BPS_bep_payoff + 2), arrowprops=dict(facecolor='black', arrowstyle='->'))
            
            st.pyplot(fig)  

elif strategy == "Long Straddle":
        
        # Defining the functions used to calculate the strategy
        # Each strategy follows the same structual format
        # 'LSD' in this case stands for Long Straddle, other strategies have different acronyms
        # Focus on 'Net-Premium','Call and Put Values', 'Net-Payoff' and 'Break-Even Point(s) (BEP)' functions for strategy's output accuracy

        def calculate_long_straddle_payoff(LSD_strike_price, LSD_premium_call, LSD_premium_put, LSD_expiration_prices):
            LSD_payoffs = []
            LSD_net_premium = LSD_premium_call + LSD_premium_put
            for LSD_expiration_price in LSD_expiration_prices:
                LSD_call_value = max(LSD_expiration_price - LSD_strike_price, 0)
                LSD_put_value = max(LSD_strike_price - LSD_expiration_price, 0)
                LSD_net_payoff = max(LSD_call_value, LSD_put_value) - LSD_net_premium
                LSD_payoffs.append((LSD_expiration_price, LSD_net_premium, LSD_call_value, LSD_put_value, LSD_net_payoff))

            # Columns for the net-payoff table
            LSD_payoff_table = pd.DataFrame(LSD_payoffs, columns=['Expiration Price', 'Net Premium', 'Call Value', 'Put Value', 'Net Payoff'])
            return LSD_payoff_table
        
        # Allows user to input numbers for strategy payoff calculation
        st.sidebar.caption("Please adjust the strategy parameters as required")
        LSD_strike_price = st.sidebar.number_input("Call & Put Strike", value=100.0, step=1.0)
        LSD_premium_call = st.sidebar.number_input("Call Premium", value=6.0, step=0.1)
        LSD_premium_put = st.sidebar.number_input("Put Premium", value=4.0, step=0.1)
        st.sidebar.markdown("---")
        st.sidebar.caption("Please adjust the payoff table and graph parameters as required")
        LSD_start_price = st.sidebar.number_input("Start Expiration Price", value=80.0, step=1.0)
        LSD_end_price = st.sidebar.number_input("End Expiration Price", value=120.0, step=1.0)
        LSD_step_size = st.sidebar.number_input("Step Size", value=5.0, step=1.0)

        # Ensures that strike prices are within range of expiration prices for computational accuracy
        if LSD_start_price >= LSD_strike_price:
            st.error("Start Expiration Price should be lower than the Strike Price.")
        elif LSD_end_price <= LSD_strike_price:
            st.error("End Expiration Price should be higher than the Strike Price.")
        else:

            LSD_expiration_prices = np.arange(LSD_start_price, LSD_end_price + LSD_step_size, LSD_step_size)
            LSD_payoff_table = calculate_long_straddle_payoff(LSD_strike_price, LSD_premium_call, LSD_premium_put, LSD_expiration_prices)

            # Create net-payoff table
            st.subheader("Long Straddle: Net-Payoff Table")
            st.table(LSD_payoff_table)

            st.markdown("---")
            
            # Create net-payoff graph
            st.subheader("Long Straddle: Net-Payoff Graph")
            fig, ax = plt.subplots()

            ax.plot(LSD_payoff_table['Expiration Price'], LSD_payoff_table['Net Payoff'])
            ax.set_xlabel('Expiration Price')
            ax.set_ylabel('Net Payoff')
            ax.axhline(y=0, color='r', linestyle='--')
            
            # Calculating the break-even point
            LSD_net_premium = LSD_premium_call + LSD_premium_put
            LSD_bep_lower = LSD_strike_price - LSD_net_premium
            LSD_bep_upper = LSD_strike_price + LSD_net_premium

            # Plots the break-even point
            ax.plot(LSD_bep_lower, 0, 'go', markersize=10, label='Break-Even')
            ax.plot(LSD_bep_upper, 0, 'go', markersize=10)
            ax.annotate(f'BEP: {LSD_bep_lower:.2f}', xy=(LSD_bep_lower, 0), xytext=(LSD_bep_lower - 5, -2), arrowprops=dict(facecolor='black', arrowstyle='->'))
            ax.annotate(f'BEP: {LSD_bep_upper:.2f}', xy=(LSD_bep_upper, 0), xytext=(LSD_bep_upper + 5, -2), arrowprops=dict(facecolor='black', arrowstyle='->'))

            st.pyplot(fig)          

elif strategy == "Long Strangle":
        
        # Defining the functions used to calculate the strategy
        # Each strategy follows the same structual format
        # 'LSN' in this case stands for Long Strangle, other strategies have different acronyms
        # Focus on 'Net-Premium','Call and Put Values', 'Net-Payoff' and 'Break-Even Point(s) (BEP)' functions for strategy's output accuracy

        def calculate_long_strangle_payoff(LSN_call_strike_price, LSN_put_strike_price, LSN_premium_call, LSN_premium_put, LSN_expiration_prices):
            LSN_payoffs = []
            LSN_net_premium = LSN_premium_call + LSN_premium_put
            for LSN_expiration_price in LSN_expiration_prices:
                LSN_call_value = max(LSN_expiration_price - LSN_call_strike_price, 0)
                LSN_put_value = max(LSN_put_strike_price - LSN_expiration_price, 0)
                LSN_net_payoff = LSN_call_value + LSN_put_value - LSN_net_premium
                LSN_payoffs.append((LSN_expiration_price, LSN_net_premium, LSN_call_value, LSN_put_value, LSN_net_payoff))

            # Columns for the net-payoff table
            LSN_payoff_table = pd.DataFrame(LSN_payoffs, columns=['Expiration Price', 'Net Premium', 'Call Value', 'Put Value', 'Net Payoff'])
            return LSN_payoff_table
        
        # Allows user to input numbers for strategy payoff calculation
        st.sidebar.caption("Please adjust the strategy parameters as required")
        LSN_call_strike_price = st.sidebar.number_input("Higher Call Strike Price", value=100.0, step=1.0)
        LSN_put_strike_price = st.sidebar.number_input("Lower Put Strike Price", value= 80.0, step=1.0)
        LSN_premium_call = st.sidebar.number_input("Lower Call Premium", value=4.0, step=0.1)
        LSN_premium_put = st.sidebar.number_input("Higher Put Premium", value=6.0, step=0.1)
        st.sidebar.markdown("---")
        st.sidebar.caption("Please adjust the payoff table and graph parameters as required")
        LSN_start_price = st.sidebar.number_input("Start Expiration Price", value=60.0, step=1.0)
        LSN_end_price = st.sidebar.number_input("End Expiration Price", value=120.0, step=1.0)
        LSN_step_size = st.sidebar.number_input("Step Size", value=5.0, step=1.0)
        
        # Ensures that strike prices are within range of expiration prices for computational accuracy
        # Additionally guides user to input premium float values that align with strategy's principles
        if LSN_start_price >= LSN_call_strike_price or LSN_start_price >= LSN_put_strike_price:
            st.error("Start Expiration Price should be lower than both Strike Prices.")
        elif LSN_end_price <= LSN_call_strike_price or LSN_end_price <= LSN_put_strike_price:
            st.error("End Expiration Price should be higher than both Strike Prices.")
        elif LSN_premium_put <= LSN_premium_call:
            st.error("Put premium should be higher than Call premium")
        elif LSN_premium_call >= LSN_premium_put:
            st.error("Call premium should be lower than Put premium")
        else:

            LSN_expiration_prices = np.arange(LSN_start_price, LSN_end_price + LSN_step_size, LSN_step_size)
            LSN_payoff_table = calculate_long_strangle_payoff(LSN_call_strike_price, LSN_put_strike_price, LSN_premium_call, LSN_premium_put, LSN_expiration_prices)

            # Create net-payoff table
            st.subheader("Long Strangle: Net-Payoff Table")
            st.table(LSN_payoff_table)

            st.markdown("---")
            
            # Create net-payoff graph
            st.subheader("Long Strangle: Net-Payoff Graph")
            fig, ax = plt.subplots()
            ax.plot(LSN_payoff_table['Expiration Price'], LSN_payoff_table['Net Payoff'])
            ax.set_xlabel('Expiration Price')
            ax.set_ylabel('Net Payoff')
            ax.axhline(y=0, color='r', linestyle='--')

            # Calculating the break-even point
            LSN_net_premium = LSN_premium_call + LSN_premium_put
            LSN_bep_lower = LSN_put_strike_price - LSN_net_premium
            LSN_bep_upper = LSN_call_strike_price + LSN_net_premium

            # Plots the break-even point
            ax.plot(LSN_bep_lower, 0, 'go', markersize=10, label='Break-Even')
            ax.plot(LSN_bep_upper, 0, 'go', markersize=10)
            ax.annotate(f'BEP: {LSN_bep_lower:.2f}', xy=(LSN_bep_lower, 0), xytext=(LSN_bep_lower - 5, -2), arrowprops=dict(facecolor='black', arrowstyle='->'))
            ax.annotate(f'BEP: {LSN_bep_upper:.2f}', xy=(LSN_bep_upper, 0), xytext=(LSN_bep_upper + 5, -2), arrowprops=dict(facecolor='black', arrowstyle='->'))

            st.pyplot(fig)

elif strategy == "Strip":
        
        # Defining the functions used to calculate the strategy
        # Each strategy follows the same structual format
        # 'STI' in this case stands for Strip, other strategies have different acronyms
        # Focus on 'Net-Premium','Put and Call Values', 'Net-Payoff' and 'Break-Even Point (BEP)' functions for strategy's output accuracy

        def calculate_strip_payoff(STI_strike_price, STI_premium_put, STI_premium_call, STI_expiration_prices):
            STI_payoffs = []
            STI_net_premium = STI_premium_call + 2 * STI_premium_put

            for STI_expiration_price in STI_expiration_prices:
                STI_put_value = max(STI_strike_price - STI_expiration_price, 0)
                STI_call_value = max(STI_expiration_price - STI_strike_price, 0)
                STI_net_payoff = 2 * STI_put_value + STI_call_value - STI_net_premium 
                STI_payoffs.append((STI_expiration_price, STI_net_premium, STI_call_value, STI_put_value, STI_net_payoff))
            
            # Columns for the net-payoff table
            STI_payoff_table = pd.DataFrame(STI_payoffs, columns=['Expiration Price', 'Net Premium', 'Call Value', 'Put Value', 'Net Payoff'])
            return STI_payoff_table
        
        # Allows user to input numbers for strategy payoff calculation
        st.sidebar.caption("Please adjust the strategy parameters as required")
        STI_strike_price = st.sidebar.number_input("Strike Price", value=100.0, step=1.0)
        STI_premium_call = st.sidebar.number_input("Call Premium", value=4.0, step=0.1)
        STI_premium_put = st.sidebar.number_input("Put Premium", value=6.0, step=0.1)
        st.sidebar.markdown("---")
        st.sidebar.caption("Please adjust the payoff table and graph parameters as required")
        STI_start_price = st.sidebar.number_input("Start Expiration Price", value=80.0, step=1.0)
        STI_end_price = st.sidebar.number_input("End Expiration Price", value=120.0, step=1.0)
        STI_step_size = st.sidebar.number_input("Step Size", value=5.0, step=1.0)
        
        # Ensures that strike prices are within range of expiration prices for computational accuracy
        if STI_start_price >= STI_strike_price:
            st.error("Start Expiration Price should be lower than the Strike Price.")
        elif STI_end_price <= STI_strike_price:
            st.error("End Expiration Price should be higher than the Strike Price.")
        else:

            STI_expiration_prices = np.arange(STI_start_price, STI_end_price + STI_step_size, STI_step_size)
            STI_payoff_table = calculate_strip_payoff(STI_strike_price, STI_premium_put, STI_premium_call, STI_expiration_prices)
            
            # Create net-payoff table
            st.subheader("Strip Strategy: Net-Payoff Table")
            st.table(STI_payoff_table)

            st.markdown("---")
            
            # Create net-payoff graph
            st.subheader("Strip Strategy: Net-Payoff Graph")
            fig, ax = plt.subplots()
            ax.plot(STI_payoff_table['Expiration Price'], STI_payoff_table['Net Payoff'])
            ax.set_xlabel('Expiration Price')
            ax.set_ylabel('Net Payoff')
            ax.axhline(y=0, color='r', linestyle='--')
            
            # Calculating the break-even point
            STI_net_premium = STI_premium_call + 2 * STI_premium_put
            STI_bep_lower = STI_strike_price - STI_net_premium / 2
            STI_upper_limit = STI_strike_price + STI_net_premium

            # Plots the break-even point
            ax.plot(STI_bep_lower, 0, 'go', markersize=10, label='Lower Break-Even')
            ax.annotate(f'BEP: {STI_bep_lower:.2f}', xy=(STI_bep_lower, 0), xytext=(STI_bep_lower - 5, -2), arrowprops=dict(facecolor='black', arrowstyle='->'))
            ax.plot(STI_upper_limit, 0, 'go', markersize=10, label='Profit Limit')
            ax.annotate(f'Limit: {STI_upper_limit:.2f}', xy=(STI_upper_limit, 0), xytext=(STI_upper_limit + 5, -2), arrowprops=dict(facecolor='black', arrowstyle='->'))

            st.pyplot(fig)
            st.markdown(" ")

            # Explaning the meaning behind 'upper limit' in a strip strategy
            st.write("The upper limit for a strip strategy indicates the price point")
            st.write("where profit potential becomes severely limited, even though the")
            st.write("strategy might still technically remain profitable, due to the")
            st.write("counteracting effect of the call option.")

elif strategy == "Strap":
        
        # Defining the functions used to calculate the strategy
        # Each strategy follows the same structual format
        # 'STA' in this case stands for Strap, other strategies have different acronyms
        # Focus on 'Net-Premium','Put and Call Values', 'Net-Payoff' and 'Break-Even Point(s) (BEP)' functions for strategy's output accuracy

        def calculate_strap_payoff(STA_strike_price, STA_premium_put, STA_premium_call, STA_expiration_prices):
            STA_payoffs = []
            STA_net_premium = 2 * STA_premium_call + STA_premium_put

            for STA_expiration_price in STA_expiration_prices:
                STA_put_value = max(STA_strike_price - STA_expiration_price, 0)
                STA_call_value = max(STA_expiration_price - STA_strike_price, 0)
                STA_net_payoff = 2 * STA_call_value + STA_put_value - STA_net_premium 
                STA_payoffs.append((STA_expiration_price, STA_net_premium, STA_call_value, STA_put_value, STA_net_payoff))
            
            # Columns for the net-payoff table
            STA_payoff_table = pd.DataFrame(STA_payoffs, columns=['Expiration Price', 'Net Premium', 'Call Value', 'Put Value', 'Net Payoff'])
            return STA_payoff_table 
        
        # Allows user to input numbers for strategy payoff calculation
        st.sidebar.caption("Please adjust the strategy parameters as required")
        STA_strike_price = st.sidebar.number_input("Strike Price", value=100.0, step=1.0)
        STA_premium_call = st.sidebar.number_input("Call Premium", value=6.0, step=0.1)
        STA_premium_put = st.sidebar.number_input("Put Premium", value=4.0, step=0.1)
        st.sidebar.markdown("---")
        st.sidebar.caption("Please adjust the payoff table and graph parameters as required")
        STA_start_price = st.sidebar.number_input("Start Expiration Price", value=80.0, step=1.0)
        STA_end_price = st.sidebar.number_input("End Expiration Price", value=120.0, step=1.0)
        STA_step_size = st.sidebar.number_input("Step Size", value=5.0, step=1.0)
        
        # Ensures that strike prices are within range of expiration prices for computational accuracy
        if STA_start_price >= STA_strike_price:
            st.error("Start Expiration Price should be lower than the Strike Price.")
        elif STA_end_price <= STA_strike_price:
            st.error("End Expiration Price should be higher than the Strike Price.")
        else:
            
            STA_expiration_prices = np.arange(STA_start_price, STA_end_price + STA_step_size, STA_step_size)
            STA_payoff_table = calculate_strap_payoff(STA_strike_price, STA_premium_put, STA_premium_call, STA_expiration_prices)
            
            # Create net-payoff table
            st.subheader("Strap Strategy: Net-Payoff Table")
            st.table(STA_payoff_table)

            st.markdown("---")
            
            # Create net-payoff graph
            st.subheader("Strap Strategy: Net-Payoff Graph")
            fig, ax = plt.subplots()
            ax.plot(STA_payoff_table['Expiration Price'], STA_payoff_table['Net Payoff'])
            ax.set_xlabel('Expiration Price')
            ax.set_ylabel('Net Payoff')
            ax.axhline(y=0, color='r', linestyle='--')
           
            # Calculating the break-even point
            STA_net_premium = 2 * STA_premium_call + STA_premium_put
            STA_bep_lower = STA_strike_price - STA_net_premium
            STA_bep_upper = STA_strike_price + STA_net_premium / 2

            # Plots the break-even point
            ax.plot(STA_bep_lower, 0, 'go', markersize=10, label='Lower Break-Even')
            ax.annotate(f'BEP: {STA_bep_lower:.2f}', xy=(STA_bep_lower, 0), xytext=(STA_bep_lower - 5, -2), arrowprops=dict(facecolor='black', arrowstyle='->'))
            ax.plot(STA_bep_upper, 0, 'go', markersize=10, label='Upper Break Even')
            ax.annotate(f'BEP: {STA_bep_upper:.2f}', xy=(STA_bep_upper, 0), xytext=(STA_bep_upper + 5, -2), arrowprops=dict(facecolor='black', arrowstyle='->'))

            st.pyplot(fig)

elif strategy == "Long Butterfly":
       
        # Defining the functions used to calculate the strategy
        # Each strategy follows the same structual format
        # 'STA' in this case stands for Strap, other strategies have different acronyms
        # Focus on 'Net-Premium','Lower, Middle and  Upper Call Values', 'Net-Payoff' and 'Break-Even Point(s) (BEP)' functions for strategy's output accuracy

        def calculate_long_butterfly_payoff(LB_call_strike_lower, LB_call_strike_middle, LB_call_strike_upper, 
                                            LB_premium_lower, LB_premium_middle, LB_premium_upper, 
                                            LB_expiration_prices):
            
            LB_payoffs = []
            LB_net_premium = LB_premium_lower + LB_premium_upper - 2 * LB_premium_middle

            for LB_expiration_price in LB_expiration_prices:
                LB_lower_call_value = max(LB_expiration_price - LB_call_strike_lower, 0)
                LB_middle_call_value = -2 * max(LB_expiration_price - LB_call_strike_middle, 0)        
                LB_upper_call_value = max(LB_expiration_price - LB_call_strike_upper, 0)
                LB_net_payoff = LB_lower_call_value + LB_upper_call_value + LB_middle_call_value - LB_net_premium
                LB_payoffs.append((LB_expiration_price, LB_net_premium, LB_lower_call_value, LB_middle_call_value, LB_upper_call_value, LB_net_payoff))
            
            # Columns for the net-payoff table
            LB_payoff_table = pd.DataFrame(LB_payoffs, columns=['Expiration Price', 'Net Premium', 'Lower Call Value', 'Middle Call Value', 'Upper Call Value', 'Net Payoff'])
            return LB_payoff_table
        
        # Allows user to input numbers for strategy payoff calculation
        st.sidebar.caption("Please adjust the strategy parameters as required")
        LB_call_strike_lower = st.sidebar.number_input("Lower Call Strike Price", value=120.0, step=1.0)
        LB_call_strike_middle = st.sidebar.number_input("Middle Call Strike Price", value=125.0, step=1.0)
        LB_call_strike_upper = st.sidebar.number_input("Upper Call Strike Price", value=130.0, step=1.0)
        
        # Allows user to input numbers for strategy payoff calculation
        st.sidebar.markdown("---")
        st.sidebar.caption("Please adjust the strategy parameters as required")
        LB_premium_lower = st.sidebar.number_input("Lower Call Premium", value= 6.0, step= 0.1)
        LB_premium_middle = st.sidebar.number_input("Middle Call Premium", value= 4.0, step= 0.1)
        LB_premium_upper = st.sidebar.number_input("Upper Call Premium", value= 3.0, step= 0.1)
        
        # Allows user to input numbers for strategy payoff calculation
        st.sidebar.markdown("---")
        st.sidebar.caption("Please adjust the payoff table and graph parameters as required")
        LB_start_price = st.sidebar.number_input("Start Expiration Price", value=90.0, step=1.0)
        LB_end_price = st.sidebar.number_input("End Expiration Price", value=160.0, step=1.0)
        LB_step_size = st.sidebar.number_input("Step Size", value=5.0, step=1.0)
        
        # Ensures that strike prices are within range of expiration prices for computational accuracy
        # Additionally ensures that each of the three strike prices do not break strategy's principles
        if LB_start_price >= LB_call_strike_lower or LB_start_price >= LB_call_strike_middle or LB_start_price >= LB_call_strike_upper:
            st.error("Start Expiration Price should be lower than the Strike Prices.")
        elif LB_end_price <= LB_call_strike_lower or LB_end_price <= LB_call_strike_middle or LB_end_price <= LB_call_strike_upper:
            st.error("End Expiration Price should be higher than the Strike Prices.")
        elif LB_call_strike_middle != ((LB_call_strike_lower + LB_call_strike_upper) / 2):
            st.error("Middle Call Strike Price must be the average of the Lower and Upper Calls' Strike Prices.")
        elif LB_call_strike_lower >= LB_call_strike_middle or LB_call_strike_lower >= LB_call_strike_upper:
            st.error("Lower Call Strike price must be lower than Middle and Upper Calls' Strike Prices.")
        elif LB_call_strike_upper <= LB_call_strike_lower or LB_call_strike_upper <= LB_call_strike_middle:
            st.error("Upper Call Strike price must be hgiher than Lower and Middle Calls' Strike Prices.")

        else: 
             
            LB_expiration_prices = np.arange(LB_start_price, LB_end_price + LB_step_size, LB_step_size)
            LB_payoff_table = calculate_long_butterfly_payoff(LB_call_strike_lower, LB_call_strike_middle, LB_call_strike_upper, LB_premium_lower, LB_premium_middle, LB_premium_upper, LB_expiration_prices)
            
            # Create net-payoff table
            st.subheader("Long Butterfly: Net-Payoff Table")
            st.table(LB_payoff_table)

            st.markdown("---")
            
            # Create net-payoff graph
            st.subheader("Long Butterfly: Net-Payoff Graph")
            fig, ax = plt.subplots()
            ax.plot(LB_payoff_table['Expiration Price'], LB_payoff_table['Net Payoff'])
            ax.set_xlabel('Expiration Price')
            ax.set_ylabel('Net Payoff')
            ax.axhline(y=0, color='r', linestyle='--')

            # Calculating the break-even point
            LB_net_premium = LB_premium_lower + LB_premium_upper - 2 * LB_premium_middle
            LB_bep_lower = LB_call_strike_lower + LB_net_premium 
            LB_bep_upper = LB_call_strike_upper - LB_net_premium 

            # Plots the break-even point
            ax.plot(LB_bep_lower, 0, 'go', markersize=10, label='Break-Even')
            ax.plot(LB_bep_upper, 0, 'go', markersize=10)
            ax.annotate(f'BEP: {LB_bep_lower:.2f}', xy=(LB_bep_lower, 0), xytext=(LB_bep_lower - 5, -2), arrowprops=dict(facecolor='black', arrowstyle='->'))
            ax.annotate(f'BEP: {LB_bep_upper:.2f}', xy=(LB_bep_upper, 0), xytext=(LB_bep_upper + 5, -2), arrowprops=dict(facecolor='black', arrowstyle='->'))

            st.pyplot(fig)

elif strategy == "-":
    st.write("Welcome to the Web-app!")
    st.write("Please start by selecting a strategy from the box in the sidebar")
    st.write("Smartphone users: Click on the ' > ' arrow on the top left side of your screen to access the sidebar")
    st.write("If you found this web-app useful, please click on my name in the sidebar to connect with me on Linkedin!")
    st.write("Happy Learning!")
