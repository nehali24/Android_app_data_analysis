# Android_app_data_analysis

This data set has been picked up from kaggle, in which i am trying to analyse the android app market using Python. Initially some data cleaning was required like dropping duplicates , dealing with diffrent datatypes and converting them . The total number of catagories in this dataset were 34 unique apps, maximum share of apps is acquired by Family type , second most popular is Games and third one is Tools.
As we know how app rating affects the brand image of any app, we also found that average rating of an app was 4.189 on scale of 1 to 5. Rating basically act as KPI for any app.
Even when we tried plotting the histogram of average app rating we found that plot was skewed to right which indicated that majority of apps are highly rated.

Price for any app depends on the catagory, interest , features, motive and platform. Different catagories of apps will show different price range.
When a plot was obtained for Categories vs App price trending,  when i tried analysing apps whose price was above 200, it was shown in plot that gaming and business genre apps are not that expensive but  medical and photography apps were very expensive and was downloaded only by a genre of users. 

Paid apps vs free apps analysis: When this analysis was done it showed that paid apps definately has less number of downloads the free apps.
I also has user review data though which i performed sentiment analysis, i could see that free apps receives lot of negavtive comments, whereas paid apps rarely receive negative comments. 

![output_18_1](https://user-images.githubusercontent.com/60546284/92946483-a456cd80-f44e-11ea-85c8-4f364933e711.png)
![output_21_1](https://user-images.githubusercontent.com/60546284/92947039-65754780-f44f-11ea-9b80-7da15d5c8d6f.png)
