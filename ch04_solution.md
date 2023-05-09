---
title: "Ch.4 Exercises: Classification"
output:
  html_document: default
  pdf_document: 
    latex_engine: lualatex
  word_document: default
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```

#### __Conceptual__

__1.__ 

  $$ \begin{aligned}
    P(x)(1+^{\beta_0 + \beta_1x}) &= e^{\beta_0 + \beta_1x}\\
    \frac{P(x)}{\frac{1}{1 + e^{\beta_0 + \beta_1x}}} &= e^{\beta_0 + \beta_1x}\\
    \frac{P(x)}{1 - \frac{e^{\beta_0 + \beta_1x}}{1+ e^{\beta_0 + \beta_1x}}} &= e^{\beta_0 + \beta_1x}\\
    \frac{P(x)}{1 - P(x)} &= e^{\beta_0 + \beta_1x}\\
  \end{aligned} $$ 
    

__2.__

  The terms from (4.12) that do not vary with $k$:
  
  $$ C = \frac{\frac{1}{\sqrt{2\pi}\sigma}\exp(-1/2\sigma^2x^2)}{\sum_l\pi_l\frac{1}{\sqrt{2\pi}\sigma}\exp(-1/2\sigma^2(x-\mu_l)^2)}$$
  Replacing C in (4.12):
  
  $$ P_k(x) = \pi_kC\exp(\frac{1}{2\sigma^2}(2\mu_kx - \mu_k^2))$$
  
  Taking logs of both sides:
  
  $$ \log(P_k(x)) = \log(\pi_k) + \log(C) + \frac{1}{2\sigma^2}(2\mu_kx - \mu_k^2) $$
  Rearranging and disregarding $C$:
  
  $$ \delta_k(x) = x\frac{\mu_k}{\sigma^2}-\frac{\mu_k^2}{2\sigma^2}+\log(\pi_k) $$

__3.__

  Removing the assumption of shared variance terms across all K classes, the terms from (4.12) that do not vary with $k$:
  
  $$ C' = \frac{\frac{1}{\sqrt{2\pi}}}{\sum_l\pi_l\frac{1}{\sqrt{2\pi}\sigma_l}\exp(-1/2\sigma_l^2(x-\mu_l)^2)} $$
  
  Replacing $C'$ in (4.12) and taking logs:
  
  $$\begin{aligned}
  P_k(x) &= C'\frac{\pi_k}{\sigma_k}\exp(-\frac{1}{2\sigma^2}(x^2-2\mu_kx + \mu_k^2))\\
  \log(P_k(x)) &= -\frac{1}{2\sigma_k^2}x^2 + \frac{\mu_kx}{\sigma_k^2} - \frac{\mu_k^2}{2\sigma_k^2} + \log(\frac{\pi_k}{\sigma_k}) + \log(C')      
  \end{aligned}$$
  
  As can be seen from the presence of $x^2$ in the final term, the discriminant is not linear.
  

__4.__ 

__(a)__
  
  In a uniform distribution, all intervals of the same length are equally probable. Assuming $x\in[0.05, 0.95]$, then intervals: $[x-0.05, x+0.05]$, so $length=0.1$.
  On average 10% of the observations would be available to make a prediction for the test observation.
  

__(b)__

  Assuming $x\in[0.05, 0.95]$, $x1_{length} \times x2_{length} = 0.01$. Therefore, 1% of the available observations would be used to make a prediction.   

__(c)__

  When p=100; $0.1^p \times 100 = 0.1^{100} \times 100$ of the observations are available.
  
__(d)__

  As the number of predictors increase, the fraction of observations available to make a prediction is reduced exponentially.
  
__(e)__

  $If p=1 ; d(length) = 0.1^{1/1} = 0.1$
  $If p=2 ; d(length) = 0.1^{1/2} = 0.32$
  $If p=100 ; d(length) = 0.1^{1/100} = 0.977$
  
  As p increases the side length converges to 1, and this shows that the hypercube centered around the test observation with 10% of the test observation needs to be nearly the same size as the hypercube with all the observations. It also shows that observations are 'further' from a test observation as p increases; that is they are concentrated near the boundary of the hypercube.
  

__5.__ 

__(a)__

  - LDA better on the test set.
  - QDA better on the training set (more flexibility to better fit the data), but worse on the test set due to increased variance.
  
__(b)__

  - QDA better on training and test sets.

__(c)__

  - In general, QDA tends to be better than LDA when the sample size is large, and where there isn't a common covariance between the classes. As such I would expect QDA to provide a better fit and so provide better predictions.
  
__(d)__

  - False : LDA will likely provide a better fit for a linear decision boundary than QDA, and so provide a better test error rate. QDA could provide an over-fitting model (due to higher flexibility) that performs well on the training set but worse on the test set(due to higher variance).
  

__6.__ 

__(a)__

$$
\begin{aligned}
P(X) &= \frac{\exp(\hat\beta_0 + \hat\beta_1X_1 + \hat\beta_2X_2)}{1 + \exp(\hat\beta_0 + \hat\beta_1X_1 + \hat\beta_2X_2)}\\
P(X) &= \frac{\exp(-0.5)}{1+\exp(-0.5)} = 0.38 
\end{aligned}
$$
  
__(b)__ 

$$
\begin{aligned}
\log(\frac{P(X)}{1 - P(X)}) &= \hat\beta_0 + \hat\beta_1X_1 + \hat\beta_2X_2\\
\log(\frac{0.5}{1 - 0.5}) &= -6 + 0.05X1 + 3.5\\
X_1 &= 50 hours. 
\end{aligned}
$$

__7.__

$$\begin{aligned}
P(Y=yes|X=4) &= \frac{\pi_{yes}f_{yes}(x)}{\sum_{l=1}^K \pi_lf_l(x)} = \frac{\pi_{yes}\exp(-1/2\sigma^2(x-\mu_{yes})^2)}{\sum_{l=1}^K\pi_l\exp(-1/2\sigma^2(x-\mu_l)^2)}\\
P(Y=yes|X=4) &= \frac{0.8\times\exp(-0.5)}{0.8\times\exp(-0.5) + 0.2\times\exp(-16/72)}\\
P(Y=yes|X=4) &= 0.75
\end{aligned}$$
  

__8.__

  The KNN with K=1 model would fit the training set exactly and so the training error would be zero. This means the test error has to be 36% in order for the average of the errors to be 18%. As model selection is based on performance on the test set, we will choose logistic regression to classify new observations.


__9.__

__(a)__

$$
\begin{aligned}
Odds &= \frac{P(X)}{1-P(X)}\\
P(X) &= \frac{0.37}{1.37} = 0.27 
\end{aligned}$$

  - 27% of people with odds of 0.37 will default.
  

__(b)__

$$Odds = \frac{0.16}{1-0.16}=0.19$$
  
  

#### __Applied__
  
__10.__ 

__(a)__

```{r}
library(ISLR)
summary(Weekly)
```

  
  
```{r}
# Scatterplot matrix.
pairs(Weekly[,1:8])
```
  
```{r}
# Correlation matrix.
cor(Weekly[,1:8])
```
  
  - As can be seen on the scatterplot and correlation matrices, there appears to be a positive correlation between 'Year' and 'Volume' only. From the summary statistics, we can observe that the Lag variables are very similar to each other and 'Today'. There doesn't appear to to be any patterns except for an increase in volume from 1989 to 2001.
  
__(b)__ __(c)__

```{r}
logistic_fit = glm(Direction ~ Lag1+Lag2+Lag3+Lag4+Lag5+Volume, data=Weekly, family=binomial)
summary(logistic_fit)
```
  
  - Lag2 is statistically significant.
  
```{r}
logistic_probs = predict(logistic_fit, type="response")
logistic_preds = rep("Down", 1089) # Vector of 1089 "Down" elements.
logistic_preds[logistic_probs>0.5] = "Up" # Change "Down" to up when probability > 0.5.

# Confusion matrix
attach(Weekly)
table(logistic_preds,Direction)
```
  
  - The fraction of days where the predictions are correct is 611/1089 = 56%. Therefore, the training error rate is 48%. Of the 987 "Up" predictions the model makes, it is correct 557/987 = 56.4% of the time. Given that there were 605/1089 = 55.6% "Up" days, the model's accuracy when predicting "Up" is only slightly better than random guessing.

  

__(d)__

```{r}
# Training observations from 1990 to 2008.
train = (Year<2009)

# Test observations from 2009 to 2010.
Test = Weekly[!train ,]
Test_Direction= Direction[!train]

# Logistic regression on training set.
logistic_fit2 = glm(Direction ~ Lag2, data=Weekly, family=binomial, subset=train)

# Predictions on the test set.
logistic_probs2 = predict(logistic_fit2,Test, type="response")
logistic_preds2 = rep("Down", 104) 
logistic_preds2[logistic_probs2>0.5] = "Up" 

# Confusion matrix.
table(logistic_preds2,Test_Direction)

```
  
  - The model makes correct predictions on 65/104= 62.5% of the days.

__(e)__

```{r}
# Using LDA.
library(MASS)
lda_fit = lda(Direction ~ Lag2, data=Weekly, subset=train)
#lda_fit

# Predictions on the test set.
lda_pred = predict(lda_fit,Test)
lda_class = lda_pred$class

# Confusion matrix.
table(lda_class,Test_Direction)
```

  - The lda model makes correct predictions 65/104 = 62.5% of the days.

__(f)__

```{r}
# Using QDA.
qda_fit = qda(Direction ~ Lag2, data=Weekly, subset=train)
qda_pred = predict(qda_fit,Test)
qda_class = qda_pred$class
table(qda_class,Test_Direction)
```
  - QDA model's TPR=1 and precision(correct predictions)=0.58, which is no better than guessing each day is "Up". 
 

__(g)__

```{r}
# Using KNN
library(class)
set.seed(1)
train_X = Weekly[train,3]
test_X = Weekly[!train,3]
train_direction = Direction[train]

# Changing from vector to matrix by adding dimensions
dim(train_X) = c(985,1)
dim(test_X) = c(104,1)

# Predictions for K=1
knn_pred = knn(train_X, test_X, train_direction, k=1)
table(knn_pred, Test_Direction)
```
  
  - KNN with K=1 in correct in its predictions for 50% of the days.
  
  
__(h)__

  - Logistic regression, LDA give the exact same confusion matrix. The TPR = 0.92, Precision = 0.62, TNR = 0.21 and NPV(Negative Predictive Value) = 0.64. 
  - For KNN with K=1, the TPR = 0.51, Precision = 0.58, TNR = 0.48 and FPV = 0.41.
  - The logistic and LDA models provide the best results, particularly for predicting "Up" days. 

__(i)__
```{r}
# Using KNN and K=3
knn_pred2 = knn(train_X, test_X, train_direction, k=3)
table(knn_pred2, Test_Direction)
```

```{r}
# Using KNN and K=9
knn_pred3 = knn(train_X, test_X, train_direction, k=6)
table(knn_pred3, Test_Direction)
```

  - Higher K values shown an improvement in the overall correct predictions (59/104) made by a KNN model when using Lag2 as the only predictor.

```{r}
# Using LDA with all Lag values
lda_fit2 = lda(Direction ~ Lag1+Lag2+Lag3+Lag4+Lag5, data=Weekly, subset=train)

# Predictions on the test set
lda_pred2 = predict(lda_fit2,Test)
lda_class2 = lda_pred2$class

# Confusion matrix
table(lda_class2,Test_Direction)
```
  - No real improvement using LDA when using all Lag variables.
  
```{r}
# Using logistic with lag2 and lag2^2
logistic_fit3 = glm(Direction ~ Lag2 + I(Lag2^2), data=Weekly, family=binomial, subset=train)

# Predictions on the test set.
logistic_probs3 = predict(logistic_fit3,Test, type="response")
logistic_preds3 = rep("Down", 104) 
logistic_preds3[logistic_probs3>0.5] = "Up" 

# Confusion matrix.
table(logistic_preds3,Test_Direction)

```

 - Results are similar to Lag2 only.
 
   
```{r}
# Using logistic with lag2 and lag1^2
logistic_fit4 = glm(Direction ~ Lag2 + I(Lag1^2), data=Weekly, family=binomial, subset=train)

# Predictions on the test set.
logistic_probs4 = predict(logistic_fit4,Test, type="response")
logistic_preds4 = rep("Down", 104) 
logistic_preds4[logistic_probs4>0.5] = "Up" 

# Confusion matrix.
table(logistic_preds4,Test_Direction)
```
 
 - This model is correct on 64% of the days.

__11.__
__(a)__
  
```{r}
# Dataframe with "Auto" data and empty "mpg01" column
df = Auto
df$mpg01 = NA
median_mpg = median(df$mpg)

# Loop
for(i in 1:dim(df)[1]){
  if (df$mpg[i] > median_mpg){
    df$mpg01[i] = 1
  }else{
    df$mpg01[i] = 0
  }
}
```

```{r}
# function to move a column to end of dataframe.
movetolast = function(data, move) {
  data[c(setdiff(names(data), move), move)]
}
```

__(b)__  

```{r}
df = movetolast(df, c("name"))
pairs(df[,1:9])
```


```{r}
cor(df[,1:9])
```
  
  - There is a strong positive correlation between `mpg` and `mpg01`, and a strong negative correlation between `cylinders`, `displacement`, `weight`, `horsepower` and `mpg01`.
  - I will use these variables except `mpg`.`mpg` was used to separate observations into `mpg01` values and so using it can lead to perfectly separating test observations.
  
__(c)__

```{r}
# Training and Test data
require(caTools)
set.seed(123)
sample_data = sample.split(df$mpg, SplitRatio = 0.70)
train2 = subset(df, sample_data==TRUE) 
test2 = subset(df, sample_data==FALSE)
```
__(d)__

```{r}
# LDA model 
lda_fit3 = lda(mpg01 ~ cylinders+displacement+horsepower+weight, data=train2)

# Predictions and confusion matrix
lda_pred3 = predict(lda_fit3,test2)
predictions = lda_pred3$class
actual = test2$mpg01
table(predictions,actual)
```
  
  - The test error of this model is 11.5%.

__(e)__

```{r}
# QDA model
qda_fit2 = qda(mpg01 ~ cylinders+displacement+horsepower+weight, data=train2)
qda_pred2 = predict(qda_fit2,test2)
predictions = qda_pred2$class
table(predictions,actual)
```
  - The QDA model has a test error of 9.6%.

__(f)__

```{r}
# Logistic regression model
logistic_fit5 = glm(mpg01 ~ cylinders+displacement+horsepower+weight, data=train2, family=binomial)

logistic_probs5 = predict(logistic_fit5,test2, type="response")
logistic_preds5 = rep(0, length(test2$mpg01)) 
logistic_preds5[logistic_probs5>0.5] = 1 

table(logistic_preds5,actual)
```
  - The logistic model has a 9.6% test error rate.

__(g)__

```{r}
# Train, Test and response matrices.
train2_matrix = data.matrix(train2[,c("cylinders","displacement","weight","horsepower")])
test2_matrix = data.matrix(test2[,c("cylinders","displacement","weight","horsepower")])
train2_y = data.matrix(train2$mpg01)
test2_y = data.matrix(test2$mpg01)

# K=1 and predictions
knn_pred4 = knn(train2_matrix, test2_matrix, train2_y, k=1)
table(knn_pred4, test2_y)

```
  
  - KNN with K=1 has a test error of 20%.
  
```{r}
# K=3 and predictions
knn_pred5 = knn(train2_matrix, test2_matrix, train2_y, k=3)
table(knn_pred5, test2_y)
```
  
  - KNN with K=3 is has a test error of 15%.
  
```{r}
# K=9 and predictions
knn_pred6 = knn(train2_matrix, test2_matrix, train2_y, k=10)
table(knn_pred6, test2_y)
```

  
  - K=10 leads to a slight improvement in test error(14.4%), with diminishing returns as K gets even higher.
  
  
  
__12.__
__(a)__ __(b)__ __(c)__

```{r}
Power2 = function(x,a){
  print(x^a)
} 
Power2(3,8)
Power2(10,3)
Power2(8,17)
Power2(131,3)
```
__(d)__ __(e)__
```{r}
Power3 = function(x,a){
  result = x^a
  return(result)
}

# Plot f(x) = x^2
x = 1:100
y = Power3(x,2)
plot(x,y,log="x", main="Plot of x against x^2")
```

__(f)__
  
```{r}
PlotPower = function(x,a){
  x_values = x
  y_values = x^a
  plot(x_values, y_values)
}
PlotPower(1:10,3)
```

__13.__

```{r}
#library(ISLR)
#library(MASS)
#library(class)
boston_df = Boston

#Add 1 to column if CRIM > median and 0 otherwise
median_crim = median(Boston$crim)
boston_df$crim01 = with(ifelse(crim>median_crim, 1, 0), data=Boston)
```

```{r}
#Correlation between crim01 and other variables.
cor(boston_df$crim01,boston_df)
```


```{r}
#Training and Test sets
require(caTools)
set.seed(123)
boston_sample = sample.split(boston_df$crim01, SplitRatio = 0.80)
boston_train = subset(boston_df, boston_sample==TRUE) 
boston_test = subset(boston_df, boston_sample==FALSE)
```

```{r}
# Logistic regression using all variables except CHAS and crim(using crim can lead to perfect separation).
boston_lr = glm(crim01 ~.-chas-crim , data=boston_train, family=binomial)
summary(boston_lr)
boston_probs = predict(boston_lr,boston_test, type="response")
boston_preds = rep(0, length(boston_test$crim01))
boston_preds[boston_probs>0.5] = 1
actual = boston_test$crim01

table(boston_preds, actual)

```
  - Test error rate of 9.8%. Same accuracy when predicting 0(crime below median) or 1(crime above median).
  
  
```{r}
# Logistic regression using zn, nox, dis, rad and ptratio. These variables were statistically significant in the previous model.
boston_lr2 = glm(crim01 ~ zn+nox+dis+rad+ptratio, data=boston_train, family=binomial)
boston_probs2 = predict(boston_lr2,boston_test, type="response")
boston_preds2 = rep(0, length(boston_test$crim01))
boston_preds2[boston_probs2>0.5] = 1
actual = boston_test$crim01

table(boston_preds2, actual)
```

  - Test error rises to 14.7% when using this subset.

```{r}
# LDA
boston_lda = lda(crim01 ~.-chas-crim , data=boston_train)
boston_preds2 = predict(boston_lda, boston_test)
table(boston_preds2$class, actual)
```

   - Test error rate of 13.7%.

```{r}
# QDA
boston_qda = qda(crim01 ~.-chas-crim , data=boston_train)
boston_preds3 = predict(boston_qda, boston_test)
table(boston_preds3$class, actual)
```

  - Test error rate of 9.8%. More accurate when predicting 0.
```{r}
#KNN
#Training and Test sets without crim and chas
boston_train2 = data.matrix(subset(boston_train,select=-c(crim,chas)))
boston_test2 = data.matrix(subset(boston_test,select=-c(crim,chas)))

train2_y = data.matrix(boston_train[,15])
test2_y = data.matrix(boston_test[,15])

```

```{r}
# KNN-1 and predictions
boston_knn1 = knn(boston_train2, boston_test2, train2_y, k=1)
table(boston_knn1, test2_y)
```

  - Test error rate of 4.9%.
  
```{r}
# KNN-3 and predictions
boston_knn2 = knn(boston_train2, boston_test2, train2_y, k=3)
table(boston_knn2, test2_y)
```
  
  - Higher test error rate of 6.9%.

```{r}
# KNN-10 and predictions
boston_knn3 = knn(boston_train2, boston_test2, train2_y, k=10)
table(boston_knn3, test2_y)
```
  - Much higher test error rate of 11.7%.
  
  - Higher K values result in the test error rate increasing. KNN-1 gives the best performance, therefore the Bayes decision boundary for the data set is likely non-linear.
  - QDA and Logistic regression perform better than LDA but worse than KNN.
 
```{r}
#KNN-1 using indus, nox, age, dis, rad, tax (strongly correlated variables with crim01)
boston_train3 = data.matrix(subset(boston_train,select=c(indus,nox,age,dis,rad,tax)))
boston_test3 = data.matrix(subset(boston_test,select=c(indus,nox,age,dis,rad,tax)))

boston_knn4 = knn(boston_train3, boston_test3, train2_y, k=1)
table(boston_knn4, test2_y)
```
  - The test error is worse when using these variables.

```{r}
#KNN-2 using nox and rad - most statistically significant in the first logistic model.
boston_train4 = data.matrix(subset(boston_train,select=c(nox,rad)))
boston_test4 = data.matrix(subset(boston_test,select=c(nox,rad)))

boston_knn5 = knn(boston_train4, boston_test4, train2_y, k=2)
table(boston_knn5, test2_y)
```

 - Test error of 4%, which is the lowest among the tested models and subsets of variables. KNN with values of K=1,2 or 3 give the best results.




