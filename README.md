# Invictus_Assessment
Nick Bailey Invictus Alpha Graduate Program Quantitative Assessment
# Question 1 - Theory
1.1.1)	The cost for a transaction on the Ethereum network (Gas cost) is determined by the GWei price per unit of gas. Gas is the unit of work expended per computation in the Ethereum Virtual Machine, covering the computing costs time and resources (electricity & hardware) incurred by the miners. Thus, the total cost of an Ethereum transaction is the amount of required gas multiplied by the price in the GWei per price unit whereby 1 GWei is one billionth of an ether. The key factor behind the costs is network congestion (variable), the value of USD/Eth pair (variable), electricity prices (for the miners, variable) and the complexity of transaction (constant – up to trader) and how fast you want it done (constant – up to trader). Having a simpler trade (A -> B cost less gas compared to A->B->C) reduces complexity and therefore cost.  The fees also depend on how fast the trader wants the transaction to be executed as a higher price for gas is paid if the trader wants to be placed higher in the queue. 

1.1.2)	A trader takes these fees into account when they want to maximize their trade. This is achieved by performing transactions when demand is low (GWei < 25 or at least in the range of 20 < Gwei < 50) which is often found on the weekends, predominantly in the evenings. In addition, trading the full amount at one time, instead of trading smaller amounts multiple times optimizes the smart contract by reducing complexity by removing all unneeded functions, simplifying the code and runtime.

1.1.3)	Automatic Market Makers (AMM) are a core component of the decentralized finance ecosystem which allow digital assets to be traded automatically/permissionless via liquidity pools on decentralized exchanges. The liquidity is provided by the collection of funds or digital assets locked in the smart contract provided by liquidity providers who are incentivized to supply these pools with assets/tokens. This differs from traditional exchanges where buyers and sellers offer up different prices for an asset and when the price of the asset is accepted by the users, they execute the trade, and that price becomes the assets market price. In AMM, you do not need another counterpart or another trader to execute a trade or trade pair, instead you interact with the smart contract that provides the market for you.

1.1.4)	Flash loans are a type of uncollateralized lending that has become popular on DeFi. They are almost the antithesis of traditional loans whereby the lender demands some sort of collateral assets to ensure that they will get their money back so that the contract can be approved and paid back, with interest, over a certain period. Flash loans are instant – the funds are both borrowed and returned within seconds in one transaction through smart contracts. If the borrower does not repay the funds or the trade does not provide a profit the conditions laid out in the smart contract are not met and the transaction is reversed, and the funds are returned to the lender just like it had never happened. 

1.1.5)	Stablecoins are cryptocurrencies that peg their market value to some external and ‘stable’ reserve like fiat money (eg. USD), exchange - traded commodities (eg. metals) or more recently, consumer price indices. Stablecoins thus replicate the advantages of traditional stable currencies via digital money with its value derived from the underlying assets. This solves volatility issues, store of value, international transfer times and fees. Stablecoins also offer a ‘safer’ option for individual or institutional investment compared to volatile or untrusted cryptocurrencies that lack reliability. Stablecoins are constructed in three different categories ; Fiat - collateralized being the simplest whereby price remains stable as the issuing party or controlling authority hold regulations by managing supply and demand of a currency (examples: Tether, USDC); Crypto – centralized stable coins use other cryptocurrencies (like ETH) as collateral whereby large numbers of cryptocurrency tokens are maintained as reserve; Non – collateralized stablecoins do not use a reserve or backed by any collateral but rather include a mechanism like a central authority/bank to maintain the price by minting new coins thus controlling stability via supply of tokens, just like printing new banknotes. 

1.1.6)	A perpetual future contract is a type of futures contract whereby the buyer and seller are not bound by the committed date in the contract which offers the buyer or seller to hold the position for as long as they want to and trade at any time. Perpetual futures contracts have no rules or regulations and rely on the decision of the two participating parties which depend on the market conditions. An integral part of perpetual futures contracts is the funding rate and is used ensure futures prices and index prices converge on a regular basis. Thus, when the perpetual futures contract is trading on a premium (higher than spot markets), long positions must pay short positions due to a positive funding rate and visa versa. The opportunity lies where we can hold a short position in the perpetual futures market and buy the same amount in the spot market which hedges our total investment, thus receiving funding rates with our short position in the perpetual futures contract. For example lets say the BTC perpetual price is $ 51k and the spot price is $ 50k – we open a short position on the perpetual market and buy the exact amount BTC on the spot market. If the perpetual price and spot price BTC goes to $ 52k we have a - $1k perpetual result whilst the spot result is + $ 2k, leaving us with a final profit of $1k. 

# Run/Build program
Libraries required to run:
pandas,
requests,
matplotlib,
plotly,
cbpro,
json
# Question 2.1

Open file named "Question2", download & run question2.1.py
Instructions specified in beginning of code. The code attempts to take the current allocation fraction & subract the new allocation fraction and determine if allocation is required for that entry. The program then attempts to allocate the difference in fractions to the entries that require more fraction allocation (those entries < 1). Then it attempts match the leftover allocatable for each entry and allocate that to the entires that require allocation. The program does not have full functionality and end points/conditions are still required as well as checking valid inputs.


# Question 3 - analysis

Open file named "Question3", download & run question3.py

The program pulls one years worth of historical data for BTC/USD, BTC-PERP, ETH/USD, ETH_PERP using FTX the API. The data in json format is then inputted into pandas data frame and the results in csv format are printed to the terminal. A candlestick graph is drawn to verify data and timeframe are correct as well as 20w SMA (see png images in Question 3). The program then defines functions which generate the sharpe, sortino and information ratios as well as the downside risk and tracking error. These functions are called and outputs printed in the terminal. Tracking error and information ratio functions returned Nan and could not be interpreted as expected.

# Question 3.1

Sharpe Ratio for BTC/USD using historical closing prices is calculated to be 0.09525 and sharpe ratio for ETH/USD using historical closing prices is calculated to be 0.07432. The Sharpe ratio being the risk – adjusted return (average return divided by standard deviation of return annualized) shows the average return with a ‘risk free’ rate. Both Spot markets for BTC/USD and ETH/USD indicate highly volatile markets with considerably (almost worryingly) low sharpe ratios whereby a sharpe ratio > 2 is considered very good ( S & P 500 market sharpe ratio = 2.46). The results indicate that BTC/USD is a more volatile market compared to ETH/USD with a sharpe ratio around 0.02 greater than ETH/USD. This indicates more investor interest in the ETH/USD asset. 
The sortino ratio is a subset of the sharpe ratio (both measure the risk – adjusted return) but it penalizes only those returns falling below the user – specified target, isolating the downside volatility. Both sortino ratios for BTC/USD and ETH/USD return Nan (0). As any trader could observe in candlestick charts, cryptocurrencies often have heavy downside risks and it is not uncommon for cryptocurrencies to have such low sortino ratios. An ideal sortino ratio would be around 2, indicating that our investment in BTC or ETH has high downside risks associated with it and therefore less appealing to the average investor.

# Question 4

Open file named "Question 4", download & run question4.py

The program uses the cbpro library in conjunction with the constants.py file using a simple strategy to place a BTC limit order.The program first an authentication is created in main() which uses an API url (with sandbox coinbase pro). An initializer is created for tradingSystems and the program continues to define main functions that will be required. Main functions include: Execute trade action (buy or sell), view coinbase account, view order id and obtain current price of bitcoin for reference. Buy and sell orders were recorded and stored in text file labelled order.txt.


