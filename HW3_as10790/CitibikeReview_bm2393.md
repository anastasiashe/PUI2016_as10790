## Ben's Peer Review!

#### Null and Alternate Hypotheses: 

The null hypothesis is almost formulated correctly. It should have "less than or equal to" rather than just "less than". 
The alternate hypothesis is formulated correctly.

It may, however, be helpful to spell out the hypotheses as formulas:
#### _$H_0$_ : $ duration_\mathrm{customer} \leq duration_\mathrm{subscriber} $
#### _$H_1$_ : $ duration_\mathrm{customer} > duration_\mathrm{subscriber} $

Note: Apparently Github doesn't like showing math in markdown files. The above works in a Jupyter notebook though!

#### Does the data fit the project?

Yes. However, some thought should be given to the outliers in the data. There are some observations (trip duration > 36 days!) that should clearly be thrown away.

#### Appropriate statistical test to test the hypotheses:

This project calls for a t-Test. It looks at a comparison of two groups and the indepenent variable is only those two groups.