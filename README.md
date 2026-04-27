\# KQC7016 Lab 3 - ANOVA



This project demonstrates the application of one-way ANOVA using the WorldEnergy.csv dataset.



\## Selected Data

\- Countries: China, United States, India, Germany, Japan

\- Years: 2000 to 2022

\- Variable: primary\_energy\_consumption



\## Objective

The objective is to test whether there is a statistically significant difference in mean primary energy consumption among the selected countries.



\## Hypotheses

H0: The mean primary energy consumption is the same among China, United States, India, Germany, and Japan.



HA: At least one country has a different mean primary energy consumption.



\## Method

A one-way ANOVA test was performed using scipy.stats.f\_oneway.



\## Result

F-statistic = 161.2889  

p-value = 4.6316e-45



Since the p-value is less than 0.05, the null hypothesis is rejected.



\## Conclusion

There is a statistically significant difference in mean primary energy consumption among China, United States, India, Germany, and Japan from 2000 to 2022.



\## Files

\- Lab3.py

\- WorldEnergy.csv

\- Lab3\_ANOVA\_Boxplot.png

\- Lab3\_ANOVA\_Mean\_BarChart.png

\- Lab3\_ANOVA\_Result.csv

\- Lab3\_Descriptive\_Statistics.csv

