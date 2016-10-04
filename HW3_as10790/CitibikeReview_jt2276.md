## Review of Anastasiya Shegay's Citibike Analysis Project by Jonathan Toy

### a. Null/Alternative hypothesis formulation:
#### Anastasiya's null hypothesis should include equality between groups, i.e. it should be that the mean trip duration for user type 'customer' is less than or equal to the mean trip duration for user type 'subscriber', so that the null & alternative hypothesis cover all possible values, but it is otherwise correct and the question itself looks well posed. The alternative hypothesis appears to be correct.

### b. Data extraction:
#### As the data contains the information on the trip duration and user type for each rider, Anastasiya's question is feasible to answer using the chosen data set. Removing all columns except for 'tripduration' and 'usertype' was also the correct choice, as these are the only entries necessary to answer the posed question. Changing the units of the trip duration column from seconds into minutes to increase readability was also helpful.

### c. Test choice
#### As we are testing to see if there is a difference in means for a single dependent variable, our independent variable is dichotomous and we have no assumption that our dependent variable is normally distributed, I would recommend a t-test be performed to test this hypothesis, though as the sample sizes for both populations are quite large a z-test could also be used and the results would be similar to the t-test.
