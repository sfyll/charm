# charm
dashboard to find most profitable call arb on charm

steps to follow:

1. Run DeribitExploiter.py to retreive data from deribit (thanks shepal)
2. update CharmData.xlsx with call data for both eth and wbtc using the following page : https://charm.fi/console/markets
3. in the file charmStatDashboard.py, run the function dashBoard whick takes three arguments:
      
      a. file location of the xlsx file described in step 2
      
      b. file location of the btc option data downloaded from Deribit in step 1.
      
      c. file location of the eth option data downloaded from Deribit in step 1.
            
            output will be a panda dataframe with the max arb opportunity for each strike.
