---
title: "Ch.3 Exercises: Linear Regression"
output:
  pdf_document: 
    latex_engine: lualatex
  html_document: default
  word_document: default
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```

#### __Conceptual__ 

1. The Null hypothesis for Table 3.4 is : \[ (TV) H_0 : \beta_0 = 0  \] \[ (Radio) H_0: \beta_1 = 0  \] \[ (Newspaper) H_0: \beta_2 = 0  \] 
   The p-values for TV and Radio are significant, so their null hypothesis can be rejected. It shows a strong likelihood that TV and Radio advert spending impacts sales positively.
   The p-value for Newspaper is not significant and so the null hypothesis is accepted. This shows that newspaper spending does not increase sales in the presence of TV and Radio spending.
   
   
2. KNN refers to a non-parametric method that can be used for classification or regression. 

   In the case of classification, a KNN classifier identifies the nearest ***K*** points to the         observation $x_{0}$ to be classified. It then estimates the probability of $x_{0}$       belonging to a specific class based on the fraction of that class amongst all the selected ***K***        points. Finally, the point is classified as belonging to the class with the        highest probability. The KNN classifier provided a qualitative response.
   
   KNN regression is similar to classification in that to also uses the nearest ***K*** points to $x_{0}$.However, unlike a classifier it provides a quantitative prediction by averaging the ***K*** points to estimate the $f(x_0)$.


3.  The regression formula for the response and predictors is : `Y = 50 + 20*GPA + 0.07*IQ + 35*Gender + 0.01*GPA:IQ - 10*GPA:Gender`.
    We can then calculate income for both genders using various predictors.          

      (a) iii is True; As males earn more on average than females after their GPA exceeds 3.5.
    
      (b) 137.1K.
    
      (c) False; In the case of the female with an IQ of 100 and a GPA of 4.0, the interaction term adds 17.6k to her final salary, and this represents around 15% of her final salary, therefore the impact of the interaction term is substantial but we have calculate the p-value of the coefficient to determine if it is statistically significant.

    
4.
   (a) The extra polynomial terms allow for a closer fit (more degrees of freedom) of the training data, so I would expect the training RSS for cubic regression to be lower than for simple linear regression.
   
   (b) The true relationship is linear and so simple linear regression would generalize better to unseen data, as such I would expect it to have lower test RSS. The cubic model likely over fit the training data, and so I would expect it to have a higher test RSS.
   
   (c) Cubic regression will have a better fit to non-linear data and so its training RSS will be lower.
   
   (d) The test RSS depends on how far from linear the true relationship$f(x)$ is. If $f(x)$ is more linear than cubic, then cubic regression can over fit, so cubic RSS will be higher and liner RSS will be lower.If $f(x)$ is more cubic than linear, then linear regression can under fit, so linear RSS will be higher and cubic RSS will be lower.
   
5. 
   
   $$ \hat{y}_{i} = x_{i} \times \frac{\sum_{i'=1}^{n}\left ( x_{i'} y_{i'} \right )}{\sum_{j=1}^{n} x_{j}^{2}} $$
   
   $$ \hat{y}_{i} = \sum_{i'=1}^{n} \frac{\left ( x_{i'} y_{i'} \right ) \times x_{i}}{\sum_{j=1}^{n} x_{j}^{2}} $$
   
   $$ \hat{y}_{i} = \sum_{i'=1}^{n} \left ( \frac{ x_{i} x_{i'} } { \sum_{j=1}^{n} x_{j}^{2} } \times y_{i'} \right ) $$
   $$ a_{i'} = \frac{ x_{i} x_{i'} } { \sum_{j=1}^{n} x_{j}^{2} } $$
6. If $x_{i}=\bar{x}$, then $\hat{\beta_{1}}=0$ (Eqn 3.4, pg.62). Therefore, $\hat{\beta_{0}}=\bar{y}$ and $\hat{y_{i}}$ = $\bar{y}$.
   A line will always pass through $(\bar{x},\bar{y})$ when $x_{i}=\bar{x}$.


7. When $(\bar{x}=\bar{y}=0)$ then:
   
   $$ \begin{aligned} RSS &= \sum_{i=1}^{n} \ (y_i-\hat{y}_{i})^2 \\  TSS &= \sum_{i=1}^{n} \ y_i^2\end{aligned}$$
   
   
   Our aim is to show that $R^2 = Cor(X,Y)^2$

   $$ \begin{aligned} R^2 &= 1 - RSS/TSS \\
   R^2 &= 1 - \frac{\sum(y_i -\hat{y}_{i})^2}{\sum(y_i)^2} \\
   \hat{y}_{i} &= \hat{\beta_1}x_i
   \end{aligned}$$
   
   
   
   
   After replacing $\hat{y_i}$ and simplifying:
   $$R^2 = 1 - \frac{\sum(\ y_i - (\sum\ x_iy_i/ \sum\ x_i^2)x_i)^2}{\sum(y_i)^2} = \frac{2(\sum\ x_iy_i)^2/\sum\ x_i^2 - \sum(\ x_iy_i)^2/ \sum\ x_i^2}{\sum\ y_i^2} $$
   Finally:
 
 $$R^2 = \frac{\sum_{i=1}^{n}\ (x_iy_i)^2}{\sum_{i=1}^{n}\ (x_i)^2\sum_{i=1}^{n}\ (y_i)^2} = Cor(X,Y)^2 $$

### Applied

__8.__ __(a)__

```{r}
library(ISLR)
#fix(Auto)
data(Auto)
mpg_pwr = lm(mpg~horsepower,data=Auto)
summary(mpg_pwr)
```
(i) There is strong evidence of a relationship between mpg and horsepower as the p-value for horsepower's coefficient is close to zero.


(ii) The $R^2$ statistic is 0.61, and this means 60% of variance in mpg can be explained by horsepower in this model. To calculate the residual error relative to the response we use the mean of mpg and the RSE. The mean of mpg is ``r mean(Auto$mpg, na.rm=T)``.The RSE was 4.906 which indicates a percentage error of``r 4.906/mean(Auto$mpg, na.rm=T) * 100.0``%. The relationship between mpg and horsepower is reasonably strong.


(iii) MPG has a negative linear relationship with horsepower. For every unit increase in horsepower, the mpg falls by -0.158mpg.

(iv)   
```{r}
predict(mpg_pwr, data.frame(horsepower=c(98)), interval='prediction')
predict(mpg_pwr, data.frame(horsepower=c(98)), interval='confidence')
```

   - `y = 39.935 - (0.158 x 98) = 24.45mpg`.

__(b)__
```{r}
plot(mpg~horsepower,main= "Scatter plot of mpg vs. horsepower", data=Auto)
abline(mpg_pwr, lwd =3, col ="red")
```

__(c)__
```{r}
par(mfrow=c(2,2))
plot(mpg_pwr)
```
   
   - The residuals v fitted chart shows a slight u-shaped pattern, and this indicates non-linearity in the data.
   - The residuals v leverage chart shows that some observations have high leverage.
   - The scale-location chart shows some possible outliers. We can confirm by using studentized residuals to find observations with values greater than 3:

```{r}
rstudent(mpg_pwr)[which(rstudent(mpg_pwr)>3)]
```

__9.__ __(a)__

```{r}
#head(Auto)
pairs(Auto[,1:8])

```


__(b)__   
```{r}
cor(Auto[,1:8])
```

__(c)__
```{r}
mpg_all = lm(mpg~.-name,data=Auto)
summary(mpg_all)
```
   i. p-value: < 3.3e-16 for a F-statistic of 252.4. This shows significant evidence of a relationship between the predictors and the mpg.
   
   ii. Displacement, weight, year and origin are statistically significant as their p-values are below 0.05 or near zero.
   
   iii. The coefficient for the 'year' predictor is 0.75, and suggests that increasing it by one year will mean a vehicles predicted mpg will be 0.75mpg
   higher, assuming all other predictors are kept constant.

__(d)__

```{r}
par(mfrow=c(2,2))
plot(mpg_all)
```
   
   - The Residuals v Fitted values chart indicates some non-linearity in the data, and so polynomial regression could provide a better fit than simple
   linear regression.
   - The standardized residuals vs leverage chart shows that observation 14 has high leverage.
   - Some observations are potential outliers: 
   
```{r}
   rstudent(mpg_all)[which(rstudent(mpg_all)>3)]
```
   - Additionally, we can check for collinearity between the predictors by finding `VIF` values. The results show some variables with VIF higher than
   5 or 10, which according to the text is problematic. Collinearity increases inaccuracy in the estimate for predictors coefficients, and hence increases their standard errors.
   
```{r}
   library(car)
   vif(mpg_all)
```




__(e)__
```{r}
mpg_interaction = lm(mpg~.-name + year:cylinders + acceleration:horsepower,data=Auto)
summary(mpg_interaction)

```

   - `cylinders:year` and `horsepower:acceleration` are statistically significant. The $R^2$ metric has increased from 0.82 to 0.85.

```{r}
mpg_poly = lm(mpg~.-name + year:cylinders + I(horsepower^2)
+ I(acceleration^2),data=Auto)
summary(mpg_poly)
```

```{r}
mpg_poly2 = lm(mpg~.-name-cylinders + log(weight) + log(acceleration) +
sqrt(displacement),data=Auto)
summary(mpg_poly2)
```

   - Both `mpg_poly` and `mpg_poly2` models see an increase in $R^2$ metric from 0.82 to 0.86. There are differences in the statistical significance of some predictors between the transformed models and the multiple regression model in __(c)__.


__10.__ __(a)__
```{r}
#fix(Carseats)
carseats_lm = lm(Sales~Price+Urban+US,data=Carseats)
summary(carseats_lm)

```

__(b)__

   - The intercept represents the number of car seats sold on average when all other predictors are disregarded.
   - The `Price` coefficient is negative and so sales will fall by roughly 54 seats(0.054x1000)for every unit($1) increase in price.
   - The `Urban=Yes` coeff is not statistically significant. The `US=Yes` coeff is 1.2, and this means an average increase in car seat sales of 1200 units when `US=Yes`(this predictor likely refers to the shop being in the USA).

__(c)__

Dummy variables used by R:
```{r}
attach(Carseats)
contrasts(US)
contrasts(Urban)
```
   
Equation:

   $$Sales = 13.04\ + -0.05Price \ + -0.02Urban(Yes:1,No:0) \ + 1.20US(Yes:1,No:0)$$ 
   
__(d)__

Using all variables:

```{r}
carseats_all_lm = lm(Sales~.,data=Carseats)
summary(carseats_all_lm)
```


   - Null hypothesis can be rejected for `CompPrice`, `Income`, `Advertising`, `Price`, `ShelvelocGood`, `ShelvelocMedium` and `Age`.

__(e)__
```{r}
carseats_all_lm2 = lm(Sales~.-Education-Urban-US-Population,data=Carseats)
summary(carseats_all_lm2)
```

__(f)__

   - The RSE goes down from 2.47 __model (a)__ to 1.02 __model (e)__. The R2 statistic goes up from 0.24 __(a)__ to 0.872 __(e)__ and the F-statistic goes up from 41.52 to 381.4. 
   - The statistical evidence clearly shows that __(e)__ is a much better fit.


__(g)__

```{r}
confint(carseats_all_lm2)
```

__(h)__
```{r}
par(mfrow=c(2,2))
plot(carseats_all_lm2)
```
  
   - The residuals v fitted values chart doesn't show any distinct shape, so the model appears to be a good fit to the data.
   - There appears to be some outliers. We can check as before by using studentized residuals. Observation 358 appears to an outlier.

```{r}
   rstudent(carseats_all_lm2)[which(rstudent(carseats_all_lm2)>3)]
```

   - There appears to be one high leverage observation. 
```{r}
hatvalues(carseats_all_lm2)[order(hatvalues(carseats_all_lm2), decreasing = T)][1]
```


__11.__ __(a)__

```{r}
set.seed (1)
x=rnorm (100)
y=2*x+rnorm (100)


lm.fit = lm(y~x+0)
summary(lm.fit)
#plot(y~x+0)
#abline(lm.fit, lwd =3, col ="red ")
```
  
   - The coefficient is 1.99 and the Std. Error is 0.11. The p-value means that the null hypothesis can be rejected, hence the coefficient is statistically significant.
   

__(b)__

```{r}
lm.fit2 = lm(x~y+0)
summary(lm.fit2)
#plot(x~y+0)
#abline(lm.fit2, lwd =3, col ="blue")
```
   
   - The coef estimate = 0.39, Std.Error = 0.02, t-statistic = 18.73, p-value < 2e-16. The t-statistic and so the p-values are exactly the same as with y onto x.
   

__(c)__

   - We observe the same value of t-statistic, and hence p-values for y onto x and x onto y regression. The regression line is exactly the same with only the axes being changed, so
   y = 2x + e can be expressed as x = (y-e)/2.


__(d)__

Assuming summation limits as being from i=1 to n, I will exclude them to make equations more legible.

$$ t^2 = \frac{\hat\beta^2}{SE(\hat\beta)^2} = \frac{\hat\beta^2}{\sum(y_i-x_i\hat\beta)^2/(n-1)\sum\ x_i^2} = \frac{(n-1)\sum(x_i^2)\hat\beta^2}{\sum(y_i-x_i\hat\beta)^2} $$
Replace $\hat\beta^2$ in the numerator and expanding the denominator:

$$t^2 = \frac{(n-1)\sum(x_iy_i)^2}{\sum(x_i)^2\sum(y_i-x_i\hat\beta)^2} = \frac{(n-1)\sum(x_iy_i)^2}{\sum\ x_i^2\sum\ y_i^2-\sum\ x_i^2\sum2\hat\beta\ x_iy_i + \sum\ x_i^2\sum (\hat\beta\ x_i)^2} $$ 

Replace $\hat\beta^2$ in the denominator and simplifying:

$$t^2 = \frac{(n-1)\sum(x_iy_i)^2}{\sum\ x_i^2\sum\ y_i^2-2\sum\ (x_iy_i)^2+ \sum\ (x_iy_i)^2} = \frac{(n-1)\sum(x_iy_i)^2}{\sum\ x_i^2\sum\ y_i^2 - \sum\ (x_iy_i)^2} $$
Finally:

$$t = \frac{\sqrt{(n-1)}\sum(x_iy_i)}{\sqrt{\sum\ x_i^2\sum\ y_i^2 - \sum\ (x_iy_i)^2}}$$


Confirming the above equation in R:
```{r}
eqn_top = sqrt(length(x)-1)*sum(x*y)
eqn_bottom = sqrt(sum(x^2)*sum(y^2) - sum(x*y)^2)
t_statistic = eqn_top/eqn_bottom
print(t_statistic)
```


__(e)__

   - It is obvious from the final result in (d) that replacing $x_i$ with $y_i$ or vice-versa gives the same t-statistic. 
   

__(f)__

```{r}
lm.fit3 = lm(y~x)
summary(lm.fit3)$coefficients[2,3]
lm.fit4 = lm(x~y)
summary(lm.fit4)$coefficients[2,3]

```

   - As can be seen, the t-statistic is the same for both regressions.



__12.__ __(a)__


   - For regression of y onto x: $\hat\beta = \sum_{i=1}^n(x_iy_i)/\sum_{i'=1}^n(x'_i)^2$, and for regression of x onto y: $\hat\beta' = \sum_{i=1}^n(x_iy_i)/\sum_{i'=1}^n(y'_i)^2$.
   - The coefficients are equal when the denominators are the same: $\sum_{i'=1}^n(x'_i)^2 = \sum_{i'=1}^n(y'_i)^2$




__(b)__

   - see Q11(a) and Q11(b).
   
   
__(c)__

```{r}

set.seed (1)
x1=rnorm(100)
y1=sample(x1) # Changes order of x1 whilst making sure sum(x1)=sum(x2)


# Regression fits.
lm.fit4 = lm(x1~y1+0)
lm.fit5 = lm(y1~x1+0)

# Coefficients
summary(lm.fit4)$coefficients[1,1]
summary(lm.fit5)$coefficients[1,1]
```

   - The coefficients are the same as expected.



__13.__ __(a)__ __(b)__ __(c)__ __(d)__ __(e)__ __(f)__


```{r}
set.seed(1)
x2 = rnorm(100, mean=0, sd=1)
eps = rnorm(100, mean=0, sd=0.5)
y2 = -1 +(0.5*x2) + eps
```

- Length of y2=100, $\beta_0=-1$, $\beta_1=0.5$

```{r}
plot(y2~x2, main= 'Scatter plot of x2 against y2', col='red')

# Linear regression line.
lm.fit6 = lm(y2~x2)
summary(lm.fit6)
abline(lm.fit6, lwd=1, col ="blue")

# Population regression line and legends.
abline(a=-1,b=0.5, lwd=1, col="red")
legend('bottomright', bty='n', legend=c('Least Squares Line', 'Population Line'), col=c('blue','red'), lty = c(1, 1))
```

   - A positive linear relationship exists between x2 and y2, with added variance introduced by the error terms.
   -  $\hat\beta_0 = -1.018$ and $\hat\beta_1 = 0.499$.The regression estimates are very close to the true values: $\beta_0=-1$, $\beta_1=0.5$. This is further confirmed by the fact that the regression and population lines are very close to each other. P-values are near zero and F-statistic is large so null hypothesis can be rejected.



__(g)__

```{r}
# Polynomial regression
lm.fit7 = lm(y2~x2+I(x2^2))
summary(lm.fit7)
```

   - The quadratic term does not improve the model fit. The F-statistic is reduced, and the p-value for the squared term is higher than 0.05 and shows that it isn't statistically significant.



__(h)__


```{r}
eps = rnorm(100, mean=0, sd=sqrt(0.01))
y2 = -1 +(0.5*x2) + eps

plot(y2~x2, main='Reduced Noise', col='red')
lm.fit7 = lm(y2~x2)
summary(lm.fit7)
abline(lm.fit7, lwd=1, col ="blue")

abline(a=-1,b=0.5, lwd=1, col="red")
legend('bottomright', bty='n', legend=c('Least Squares Line', 'Population Line'), col=c('blue','red'), lty = c(1, 1))
```



   - The points are closer to each other, the RSE is lower, R2 and F-statistic are much higher than with variance of 0.25. The linear regression and population lines are very close to each other as noise is reduced, and the relationship is much more linear.


__(i)__

```{r}
eps = rnorm(100, mean=0, sd=sqrt(0.5625))
y2 = -1 +(0.5*x2) + eps

plot(y2~x2, main='Increased Noise', col='red')
lm.fit8 = lm(y2~x2)
summary(lm.fit8)
abline(lm.fit8, lwd=1, col ="blue")

abline(a=-1,b=0.5, lwd=1, col="red")
legend('bottomright', bty='n', legend=c('Least Squares Line', 'Population Line'), col=c('blue','red'), lty = c(1, 1))
```

   - The points are more spread out and so the relationship is less linear. The RSE is higher, the R2 and F-statistic are lower than with variance of 0.25.
   


__(j)__

```{r}
# 95% confidence intervals for original, less noise and more noise datasets respectively.
confint(lm.fit6) 
confint(lm.fit7)
confint(lm.fit8)
```

   - Confidence interval values are narrowest for the lowest variance model, widest for the highest variance model and in-between these two for the original model.
   


__14.__ __(a)__ __(b)__ __(c)__

```{r}
set.seed (1)
x1 = runif(100)
x2 = 0.5*x1+rnorm(100)/10
y = 2+2*x1+0.3*x2+rnorm(100)
```

   - $Y = 2 + 2x_1 + 0.3x_2 + \epsilon$, where $\epsilon$ is a N(0,1) variable.
   - $\beta_0=2$, $\beta_1=2$, $\beta_2=0.3$ 
   
```{r}
cor(x1,x2) 
plot(x2~x1)
```


```{r}
lm.fit9 = lm(y~x1+x2)
summary(lm.fit9)
```

   - Coefficients from regression: $\hat\beta_0=2.13$, $\hat\beta_1=1.44$, $\hat\beta_2=1.00$. The Std. Error is high and increases from x1 to x2, and their respective regression coefficients $\hat\beta_1$ and $\hat\beta_2$ are inaccurate when compared to $\beta_0=2$ and $\beta_1=2$ .The p-value for $\hat\beta_1$ is below 0.05 and so we can reject $H_0 : \hat\beta_1 = 0$. The p-value for $\hat\beta_2$ is much higher than 0.05 and so we cannot reject $H_0 : \hat\beta_2 = 0$.
   
__(d)__
   
```{r}
lm.fit10 = lm(y~x1)
summary(lm.fit10)
```

   - RSE and R2 are similar to when using x1+x2, F-statistic is slightly greater.
   - P-value is near zero for x1 and so $H_0 : \hat\beta_1 = 0$ can be rejected.

__(e)__

```{r}
lm.fit11 = lm(y~x2)
summary(lm.fit11)
```

   - P-value is near zero for x2 and so $H_0 : \hat\beta_1 = 0$ can be rejected.
   

__(f)__

   - No, they do not contradict each other as the difference between __(c)__ and __(e)__ can be explained by the problem of collinearity. When using two variables that are highly collinear, the effect on the response of one variable can be masked by another. Collinearity also causes the standard error to increase - as can be seen the std. error of x1+x2 is greater than x1 or x2.


__(g)__

```{r}
x1=c(x1 , 0.1)
x2=c(x2 , 0.8)
y=c(y,6)

lm.fit9_g = lm(y~x1+x2)
lm.fit10_g = lm(y~x1)
lm.fit11_g = lm(y~x2)

plot(x1,x2)
text(x=0.1, y=0.8, labels="new-obs", pos=4, cex=.7, col="blue")

```
   
   - The new point (101) appears to be an outlier. We can further investigate by using diagnostic plots for each model.

```{r}
par(mfrow=c(2,2))
plot(lm.fit9_g)
```

   - Point 101 is high leverage but not an outlier.
   

```{r}
par(mfrow=c(2,2))
plot(lm.fit10_g)
```
   
   - Point 101 is an outlier.
   

```{r}
par(mfrow=c(2,2))
plot(lm.fit11_g)
```

   - Point 101 is high leverage.


__15.__ __(a)__


```{r}
library(MASS)
summary(Boston)
```



```{r}
#Linear regression of per capita crime onto each variable.
lm.zn = lm(crim~zn, data=Boston)
lm.indus = lm(crim~indus, data=Boston)
lm.chas = lm(crim~chas, data=Boston)
lm.nox = lm(crim~nox, data=Boston)
lm.rm = lm(crim~rm, data=Boston)
lm.age = lm(crim~age, data=Boston)
lm.dis = lm(crim~dis, data=Boston)
lm.rad = lm(crim~rad, data=Boston)
lm.tax = lm(crim~tax, data=Boston)
lm.ptratio = lm(crim~ptratio, data=Boston)
lm.black = lm(crim~black, data=Boston)
lm.lstat = lm(crim~lstat, data=Boston)
lm.medv = lm(crim~medv, data=Boston)

```

```{r}

# Dataframe with empty columns for p-values and coefficients.
df_pvalues = data.frame("p_values"= NA[1:13])
df_pvalues$coefficients = NA

# Change row name to predictor names.
row.names(df_pvalues) = names(Boston[2:14])

# For loop to extract and add to dataframe each p-value and coefficient.
for (i in 1: 13){
   lm_str = str2lang(paste("lm",row.names(df_pvalues)[i], sep="."))
   df_pvalues[i,1]= summary(eval(lm_str))$coefficients[2,4]
   df_pvalues[i,2]= summary(eval(lm_str))$coefficients[2,1]
   }

df_pvalues

```
   - The p-values show that all predictors except `chas` are statistically significant.
   - The coefficients show a positive linear relationship between `crim` and `ptratio` and a negative relationship between `crim` and `dis`. We should expect `crim` to increase as `ptratio` increases and decrease as `dis` increases. See charts below showing scatter plots with regression lines in each case.

```{r}
attach(Boston)
plot(ptratio,crim, main="Scatter plot of crim vs ptratio")
abline(lm.ptratio, lwd =3, col ="blue")

plot(dis,crim, main="Scatter plot of crim vs dis")
abline(lm.dis, lwd =3, col ="blue")
```

__(b)__ __(c)__

```{r}
# Regression using all predictors.
lm.fit_all = lm(crim~., data=Boston)
summary(lm.fit_all)
```


   - The coefficient estimates and statistical significance for predictors have changed. For example, `ptratio` has a negative coefficient here, whereas it had a positive one in simple regression. In simple regression the coefficient of a predictor is calculated whilst ignoring all other predictors, and in multiple regression it is calculated whilst holding other predictors fixed. The difference in values between results from (a) and (b) isn't contradictory if the variables have collinearity - this was explored in Q14.
   
   - Null hypothesis can be rejected for `zn`, `dis`, `rad`, `black` and `medv`.
   
```{r}
# Dataframe with coefficients from multiple regression and an empty column for coefficients from simple regression.
df_coefs = data.frame("multi_coefs"=summary(lm.fit_all)$coef[-1,1])
df_coefs$simple_coefs = NA 

# Loop through each predictor, run linear regression and add values to dataframe.
for(i in row.names(df_coefs)){
    reg_model =  lm(crim~eval(str2lang(i)), data=Boston)
    df_coefs[row.names(df_coefs)==i, "simple_coefs"] = coef(reg_model)[2] 
}


# Plot chart.
plot(df_coefs$simple_coefs, df_coefs$multi_coefs, xlab="Simple Regression Coefficients", ylab="Multiple Regression Coefficients")

```

__(d)__

```{r}
# Dataframe with columns for p-values of all polynomial terms.
df_poly = data.frame("variables"=names(Boston[2:14]))
df_poly$P_values_deg1 = NA
df_poly$P_values_deg2 = NA
df_poly$P_values_deg3 = NA

# Removed CHAS as it is a qualitative variable. It also caused error : 'degree' must be less than number of unique points.
df_poly = df_poly[-3,]
row.names(df_poly) <- NULL # Reset row numbers


# Loop through variables, run polynomial regression and add p-values to dataframe.
# Regression formula created from strings of each variable combined using paste.
for(i in 1:12){
    frmla1 = paste("poly(",paste(df_poly$variables[i],3,sep=","),")",sep="")
    frmla2 = paste("crim",frmla1,sep="~")
    frmla3 = as.formula(frmla2)
    poly_model = lm(frmla3, data=Boston)
    df_poly[i,2] = summary(poly_model)$coefficients[2,4]
    df_poly[i,3] = summary(poly_model)$coefficients[3,4]
    df_poly[i,4] = summary(poly_model)$coefficients[4,4]
}


df_poly

```


   - The degree 1 coefficients are all statistically significant - as expected.
   - The degree 2 (squared fit) coefficients for zn, indus, nox, rm, age, dis, rad, tax, ptratio, lstat and medv are statistically significant. 
   - The degree 3 (cubic fit) coefficients of medv, dis, age, nox, ptratio and indus are statistically significant.
   - The p-values support a quadratic fit for all variables except black, and also support a cubic fit for medv, dis, age, nox, ptratio and indus. Therefore, there is evidence of a non-linear relationship (either quadratic or cubic) for all variables except black.















