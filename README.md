# Options Trading Strategies Profitability Calculator

Hey there, welcome to the app! Below you will find the walkthrough of the app's functions below along with some tips for users. 

## 🌟 WALKTHROUGH 

### 🔶 Step 1: Select an options strategy from the dropdown list

<img width="318" alt="Screenshot 2024-05-05 at 19 25 31" src="https://github.com/saimanish2002/options-strat-payoff/assets/161119631/2e0561ef-141d-43de-9884-4ba6545164ec">

### 🔶 Step 2: Enter the parameter values for chosen strategy

<img width="304" alt="Screenshot 2024-05-05 at 19 28 04" src="https://github.com/saimanish2002/options-strat-payoff/assets/161119631/c1518b5f-933a-4a15-8733-b21139749996">

## 🔷 Parameters glossary:
🔹 Strike Price: 
- The predetermined price at which the holder of an option can buy (call) or sell (put) the underlying asset.
- This is the central point around which potential profit or loss is calculated.
🔹 Premium:
- The cost of the option contract itself, paid by the buyer to the seller.
- This is an upfront expense, factored into the net profit or loss calculations.
🔹 Start Expiration Price:
- The lowest underlying asset price that the calculator will consider when generating potential profit/loss scenarios.
🔹 End Expiration Price:
- The highest underlying asset price included in the calculator's analysis.
🔹 Step Size:
- The incremental amount by which the underlying asset's price changes in the calculator's simulations.
- For example, a step size of $5 means the calculator will show profitability at underlying asset prices of $50, $55, $60, and so on.

## 💣 Note that a strategy may have multiple strikes and premiums. For illustration purposes, we have chosen to use the 'long Call' options strategy as part of the walkthrough. 

### 🎉 Voila! The app will have computed the net-payoff table, graph and break even poin(s) according to your inputs! 

<img width="756" alt="Screenshot 2024-05-05 at 19 38 59" src="https://github.com/saimanish2002/options-strat-payoff/assets/161119631/9f806aea-813f-4ac0-b1e2-19ea36360f38">

<img width="749" alt="Screenshot 2024-05-05 at 19 39 07" src="https://github.com/saimanish2002/options-strat-payoff/assets/161119631/0a085207-66a0-4065-8e65-a4f0c474961a">

### 🌟 USER TIPS

## 🔻 TIP 1: Make sure strike price(s) are between start and end expiration prices. 

All strike prices must be in between the range of expiration prices denoted by the start expiration price, end expiration price and step size which creates the range between the two prices according to the step specified. 

<img width="876" alt="Screenshot 2024-05-05 at 19 55 49" src="https://github.com/saimanish2002/options-strat-payoff/assets/161119631/d7f9985a-1d45-47e4-abbf-37f75d6d03aa">

## 🔻 TIP 2: Read parameter labels carefully to input higher / lower values for the appropriate strikes / premiums

Strategies such as a bull call spread (see illustration below) require multiple inputs for various parameters. It is imperative that you enter the right values for the appropriate parameter to avoid receiving an error such as the one below. 

<img width="302" alt="Screenshot 2024-05-05 at 20 04 51" src="https://github.com/saimanish2002/options-strat-payoff/assets/161119631/6af671ef-8183-4014-8f0b-d0567d069b88">

<img width="558" alt="Screenshot 2024-05-05 at 20 05 18" src="https://github.com/saimanish2002/options-strat-payoff/assets/161119631/686dbe46-df99-4b26-a4f4-0dee2ab141e2">

## 🔻 TIP 3: How to reset parameter values

Sometimes, you might enter a combination of values by mistake that completely mess up the net-payoff table and graph (see figures below). To solve this, simply re-select the 'strategy' as ' - ' and then comtinue by selecting the strategy again where all values will be reset. 

<img width="314" alt="Screenshot 2024-05-05 at 20 12 16" src="https://github.com/saimanish2002/options-strat-payoff/assets/161119631/b79582f7-9e3f-4aad-b955-a64fa130c7e7">

### 🌟 IF YOU FOUND THIS USEFUL, PLEASE CONNECT WITH ME ON LINKEDIN !

Linkedin URL: https://www.linkedin.com/in/saimanish-prabhakar-3074351a0/






