# Data Preprocessing Project Backlog
## Exploratory Data Analysis
**Objectives.** Find outliers and missing values, treat outliers and missing values. Gain initial insights on variables' distributions.

### Part 1. Preliminary EDA
1. Imported the file
2. MultiPlot:
- Age: Noticed outliers for users with age above >111. Also there might be some inconsistencies as we have ages over 122 (which is the oldest verified age) and missing values.
    - Source: https://www.nytimes.com/1997/08/05/world/jeanne-calment-world-s-elder-dies-at-122.html
- Approximate Annual Income: Extreme outliers (above 600k) and missing values
    - We will need to filter and re-analyze the data for outliers
- City of Residence: no particular observations, seems to be more or less uniformly distributed
- Consultation Duration: no outliers but there are outliers (from 140)
- Consultation Price: there are extreme outliers but no missing values
    - Approach will be same as ANI
- Department: Uniformy distributed except for "General Practice" and "Psychiatry"
    - This might cause a light skew on small ages in the Age variable. Need to confirm by rechecking its histogram after outlier omission.
- Education Level: Significative prevalence on "Master" and "Undergraduate" and 29 missing variables
- Family History: slight prevalence of heart disease
- Gender: nothing of note
- Insurance coverage: missing values and a significative prevalence of people without insurance coverage. Excluding them, the variable has a slight right-skew
- Insurance provider: there are some missing variables, the distribution seems to be more or less uniform
- Marital status: nothing to notice
- Profession: prevalence in retired people and students.
- Satisfaction level: nothing to notice, except that 6 is less given respect to others
3. Variable Clustering:
- The correlation matrix does not suggest any significative correlations (to be rechecked in the final version)
4. Python (Pandas)
- Visit Date: No missing values, visits range from 2024-01-01 to 2024-06-30.

### Part 2. Post-Outliers EDA and Missing Values Imputation
1. Filtered according to the criterions prescribed above
- We have removed about the 1.41% of the data
2. Multiplot:
- Age: No outliers and data does not seem to have a particular distribution type
    - Most frequent customer age is 12
- ANI: There seems to be a neat separation from people with no income to people with income >32k.
    - We might need to separate the data into two parts for statistical distribution as this might make data unreliable
- Consultation Duration: Nothing of noteworthy, variable seems to be uniformly distributed
- Consulation Price: There is a peak at 192, and then the frequency drops (this suggests a possible right-side skew)
- Insurance Coverage: Analogous situation to ANI
    - There are a lot of people without insurance coverage, the rest of variable seems to be right-skewed
3. StatExplore
    - As suspected before, there is a significative skew in consultation price. There also seems to be negative skew in age.
4. Variable Clustering
- There is a significative (but not high enough) correlation between:
    - Age x ANI = 0.607
    - Consultation Price x Insurance Coverage = 0.63
- Even though these numbers are still inside the range [-0.7, 0.7], we still need to tread carefully with them.
5. Clustering (for Multidimensional outliers)
- For k=4, there seems to be no multidimensional outliers
6. Data Transformation
- Not required to standardize variables as specified in the project description

### Part 3. Inconsistencies
Possible inconsistencies
- Age and marital status: if age < 19 (legal age) but marital status is married, divorced or widoves
- Age and education level: multiple queries (by education level)
    - Example: elementary students should not be over 12 (UK school system)
    - For other specific cases we should take UK's system as reference
- Age and profession: people under 19 should be students only or similar
- Age and income: people under 16 should not have an income
- Profession and education level: multiple queries 
    - ex: engineers or lawyers should at least be undergraduates
- Patient ID: check if there are differences between demographic data (like the ages should be the same...)
    - Age
    - Gender
    - Family History
    - We do not check for city of residence, marital status, education level, profession as they can change in 5 months
- consultation price and insurance coverage: insurange coverage should always be smaller than consultation price
- insurange provider and insurance coverage: people without insurance should not have insurance coverage at all
