# Overview

The data set that we are analyzing is data on the price of land in the USA from 1997 to 2017. This data includes the price of both states and regions.

https://www.kaggle.com/datasets/jmullan/agricultural-land-values-19972017


My purpose for writing this software was to answer questions i had about land prices and how they changed over time. I wnated to know the best places to buy land for cheap. 


[Software Demo Video](https://youtu.be/i2dV1DdB-3I)

# Data Analysis Results

What is the state with the cheapest land? what year was the cheapest?

             State LandCategory           Region Region or State  Year  Acre Value
2392  North Dakota      Pasture  Northern Plains           State  1997       141.0
2445  North Dakota      Pasture  Northern Plains           State  1998       144.0
2498  North Dakota      Pasture  Northern Plains           State  1999       146.0
2420       Wyoming      Pasture         Mountain           State  1997       150.0
2418    New Mexico      Pasture         Mountain           State  1997       150.0

What is the state with the most expensive land? what year was the most expensive?

             State      LandCategory     Region Region or State  Year  Acre Value
2905    New Jersey           Pasture  Northeast           State  2007     16800.0
659   Rhode Island  Farm Real Estate  Northeast           State  2008     16800.0
2958    New Jersey           Pasture  Northeast           State  2008     16500.0
600   Rhode Island  Farm Real Estate  Northeast           State  2007     16400.0
1782    New Jersey          Cropland  Northeast           State  2007     16000.0

What is the cheapest region and year?

                State LandCategory           Region Region or State  Year  Acre Value
2389  Northern Plains      Pasture  Northern Plains          Region  1997       206.0
2442  Northern Plains      Pasture  Northern Plains          Region  1998       216.0
2412         Mountain      Pasture         Mountain          Region  1997       219.0
2495  Northern Plains      Pasture  Northern Plains          Region  1999       222.0
2548  Northern Plains      Pasture  Northern Plains          Region  2000       230.0

What is the most expensive region and year

          State LandCategory     Region Region or State  Year  Acre Value
2168  Corn Belt     Cropland  Corn Belt          Region  2014      7000.0
2222  Corn Belt     Cropland  Corn Belt          Region  2015      6840.0
2276  Corn Belt     Cropland  Corn Belt          Region  2016      6710.0
2330  Corn Belt     Cropland  Corn Belt          Region  2017      6670.0
2368    Pacific     Cropland    Pacific          Region  2017      6570.0

What is the trend for land price per year

Year
1997    1459.957831
1998    1508.927711
1999    1570.102410
2000    1660.728916
2001    1755.873494
2002    1870.753012
2003    1984.337349
2004    2163.602410
2005    2606.686747
2006    2950.801205
2007    3214.709091
2008    3351.236364
2009    3170.418182
2010    3113.969325
2011    3204.283951
2012    3318.129630
2013    3482.691358
2014    3634.951220
2015    3695.676829
2016    3702.926380
2017    3741.564417
Name: Acre Value, dtype: float64

What land type is the most expensive and which is cheapest

LandCategory
Cropland            3109.421099
Farm Real Estate    3084.500404
Pasture             1891.594867
Name: Acre Value, dtype: float64

What is South dakotas land price trend over time?

Year
1997     312.000000
1998     333.666667
1999     343.666667
2000     371.666667
2001     396.666667
2002     422.000000
2003     453.666667
2004     495.666667
2005     588.666667
2006     693.333333
2007     783.333333
2008     930.000000
2009     906.666667
2010     964.666667
2011    1111.000000
2012    1363.666667
2013    1732.333333
2014    2120.000000
2015    2343.333333
2016    2263.333333
2017    2190.000000
Name: Acre Value, dtype: float64

What is Idahos land price trend over time?

Year
1997     973.333333
1998    1030.000000
1999    1096.666667
2000    1106.666667
2001    1143.333333
2002    1180.000000
2003    1220.000000
2004    1265.000000
2005    1453.333333
2006    2033.333333
2007    2290.000000
2008    2303.333333
2009    2030.000000
2010    1950.000000
2011    1920.000000
2012    1980.000000
2013    2096.666667
2014    2206.666667
2015    2306.666667
2016    2366.666667
2017    2450.000000
Name: Acre Value, dtype: float64

What is Wyomings land price trend over time?

Year
1997    369.666667
1998    386.333333
1999    383.666667
2000    425.000000
2001    447.333333
2002    470.000000
2003    492.333333
2004    507.333333
2005    470.666667
2006    563.333333
2007    683.333333
2008    740.000000
2009    702.333333
2010    730.000000
2011    776.666667
2012    810.000000
2013    810.000000
2014    830.000000
2015    846.666667
2016    846.666667
2017    840.000000
Name: Acre Value, dtype: float64

What is North Dakotas land price trend over time?

Year
1997     319.333333
1998     328.333333
1999     329.000000
2000     333.333333
2001     338.333333
2002     343.333333
2003     351.666667
2004     376.666667
2005     426.666667
2006     483.333333
2007     540.000000
2008     643.333333
2009     643.333333
2010     672.666667
2011     768.666667
2012     959.333333
2013    1292.666667
2014    1540.000000
2015    1636.666667
2016    1553.333333
2017    1563.333333
Name: Acre Value, dtype: float64

# Development Environment

-Python
-Pandas python library

# Useful Websites

* [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html#min) 
* [Getting started with Data Analysis with Python Pandas](https://towardsdatascience.com/getting-started-to-data-analysis-with-python-pandas-with-titanic-dataset-a195ab043c77)

# Future Work

* Create graphs that show the trends 
* add more questions
* find more data over time
* compare against inflation