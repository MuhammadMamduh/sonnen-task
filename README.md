# Documentation
### Framework Features
+ Using Pytest with a parametrized fixture to cover the 3 Battery Models (Basic, Standard, & Pro)
+ I've integrated allure reports in order to get a user-friendly test report
  + you can run it using `run-and-generate-report.sh`
+ This framework contains covers 3 main scenarios * 3 Battery Models (Basic, Standard & Pro) = 9 TCs:
  - `PV Production > House Consumption`
    - If the remaining power > battery need to fully charge, the remaining power will be sold to the grid/government
    - If the remaining power <= battery need to fully charge, the battery will take all the remaining power, and nothing will be sold (or bought) from the grid/government
  - `PV Production = House Consumption`
    - Since there's no remaining power in this case, the battery won't be charged/discharged, and no power will be bought/sold from/to the grid/government
  - `PV Production < House Consumption`
    - If the power deficit > Power stored in the battery, then the power in the battery will be used, and the remaining deficit will be bought from the grid/government
    - If the power deficit <= Power stored in the battery, then the power in the battery will be used, and as it is sufficient, then there's no need to buy from the grid/government 
### Future Enhancements
+ Add more scenarios
+ Add better calculations when it comes to the relationship between the physics units (like the relationship between the Power, Volt, and Ampere)
+ GitHub workflow
