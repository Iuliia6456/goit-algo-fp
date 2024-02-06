The results show that the number of dice rolls calculated by the Monte Carlo method is quite close to the analytical calculation.
But we should point out the larger number of dice rolls is used the more accurate result we get.

With the number of dice rolls in 1000 we observe the following result (not all amounts were taken into account, only those
which reflect the biggest gap and therefore provide the best visibility):

Amount | Analytical | Monte Carlo
4        8.33%        7.40% 
6        13.89%       14.80%
7        16.67%       17.60% 
9        11.11%       12.30% 
11       5.56%        4.40% 

To enlarge the accuracy of the result let's increase the number of dice rolls to 100 000. 
And we observe the accuracy has increased significantly, the results are almost the same:

Amount | Analytical | Monte Carlo
4        8.33%        8.32%  
6        13.89%       13.72%
7        16.67%       16.65% 
9        11.11%       11.09%  
11       5.56%        5.64%  

Thus, a larger number of dice rolls leads to more accurate results, but on the same time requires additional computation.
