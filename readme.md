### **Cross-sectional approach (using panel data):**

Let $r_{i,t}$ denote the period $t$ return of asset $i$ in excess of the risk free rate (i.e. the risk premium). The period $t+1$ excess return of asset $i$ can be expressed in terms of an additive prediction error model:

$$
r_{i,t+1} = \mathbb{E}_t[r_{i,t+1} \mid \mathcal{F}_t] + \varepsilon_{i,t+1},
$$

with

$$
\mathbb{E}_t[r_{i,t+1} \mid \mathcal{F}_t] = g(x_{i,t}),
$$

where 

- $\mathbb{E}_t[r_{i,t+1} \mid \mathcal{F}_t]$ is the time $t$ conditional expectation of $r_{i,t+1}$, given the information set $\mathcal{F}_t$ 
- $\varepsilon_{t,i+1}$ is a zero-mean unpredictable disturbance term
- $g(.)$ is a flexible function of predictor variables, which are expressed in terms of the P-dimensional vector $x_{i,t}$

The function $g(.)$ does neither depend on $i$ nor on $t$. This allows the model to leverage information from the entire panel (across stocks and  time) and lends stability to the model estimates (at least in theory).
  
<br>

### **Time-series approach:**

Let the S&P500 be the **only** asset under consideration (only a single time-series is now of interest). The ovearching model reduces to

$$
r_{t+1} = \mathbb{E}_t[r_{t+1} \mid \mathcal{F}_t] + \varepsilon_{t+1},
$$

with


$$
\mathbb{E}_t[r_{t+1} \mid \mathcal{F}_t] = g(x_{t}).
$$

Since the S&P500 is a good proxy for the US equity market as a whole, its excess return can be understood  as the equity risk premium (i.e. the market premium for bearing equity risk).

Machine Learning methods are employed to provide an estimate of $g(.)$ by training on known $(r_{t+1}, x_t)$ pairs (labeled examples, supervised learning). The estimated model, whose functional form depends on the chosen method, is then used to generate the forecasts: $\hat g(.) = \hat r_{t+1}$.

The set of supervised ML methods to choose from includes:
- simple (non-)linear models wihtout regularization (possible baseline)
- Lasso/Ridge/ElasticNet Regression
- Principal Component Regression, Partial Least Squares
- Random Trees/Forests, (Gradient) Boosted Trees (e.g. XGBoost, CatBoost)
- Neural Networks
- ... and other methods (used for regression tasks)

ML methods are characterized by:

- the functional form of $g(.)$ (i.e. the model)
- an algorithm used to optimize model parameters based on an objective function (training the model)
- an algorithm used to optimize hyperparameters (model parameters that are not learned from data) (tuning the model)

<br>

### **Data: (so far)**

1980 - 2023, ~ 1800 individual stocks in total (unbalanced panel), 50+ features, monthly frequency

<br>

### **Performance evaluation:**

The out-of-sample $R^2$ statistic (Campbell and Thompson, 2008) is an evaluation metric commonly found in the return prediction literature (notation assumes a single time-series):

$$
R^2_{\textit{OOS}} = 1 - \frac{\sum (r_t-\hat r_{t\mid t-1})^2}{\sum (r_t-\bar r_{t\mid t-1})^2},
$$

where

- the sum runs over the observations in the test set
- $\hat r_{t\mid t-1}$ is the time $t-1$ prediction for $r_t$ (using only information available at time $t-1$, i.e. $\in \mathcal F_{t-1}$)
- $\bar r_{t\mid t-1}$ is the historical average excess return measured at time $t-1$ (sometimes set to 0)

The $R^2_{\textit{OOS}}$ measure compares the oos-performance of the trained model, $\hat g(.)$, to a model which assumes that returns are generated by the process $r_{t+1} = \mu + \varepsilon_{t+1}$ and therefore unpredictable.

<br>

---

<br>

## Related literature

Shihao Gu, Bryan Kelly, Dacheng Xiu, **Empirical Asset Pricing via Machine Learning**, The Review of Financial Studies, Volume 33, Issue 5, May 2020, Pages 2223–2273.  
https://academic.oup.com/rfs/article/33/5/2223/5758276

Rapach, David and Zhou, Guofu, **Asset Pricing: Time-Series Predictability** (March 24, 2022). Oxford Research Encyclopedia of Economics and Finance.  
https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3941499

Goyal, Amit and Welch, Ivo and Zafirov, Athanasse, **A Comprehensive 2021 Look at the Empirical Performance of Equity Premium Prediction II** (January 31, 2023). Swiss Finance Institute Research Paper No. 21-85.  
https://ssrn.com/abstract=3929119 

John Y. Campbell, Samuel B. Thompson, **Predicting Excess Stock Returns Out of Sample: Can Anything Beat the Historical Average?**, The Review of Financial Studies, Volume 21, Issue 4, July 2008, Pages 1509–1531.  
https://academic.oup.com/rfs/article/21/4/1509/1567518

Allan Timmermann, Clive W.J. Granger, **Efficient market hypothesis and forecasting**, International Journal of Forecasting, Volume 20, Issue 1, 2004, Pages 15-27.  
https://www.sciencedirect.com/science/article/abs/pii/S0169207003000128

Rapach, David and Zhou, Guofu, **Time-Series and Cross-Sectional Stock Return Forecasting: New Machine Learning Methods** (July 27, 2019).  
https://ssrn.com/abstract=3428095 

Sewell, Martin. "**The efficient market hypothesis: Empirical evidence.**" International Journal of Statistics and Probability 1.2 (2012): 164.  
https://pdfs.semanticscholar.org/22f4/a700d40e94d184eeab3f61a9793848a92bb2.pdf

Rossi, Alberto G. "**Predicting stock market returns with machine learning.**" (2018).  
https://mendoza.nd.edu/wp-content/uploads/2019/07/2018-Alberto-Rossi-Fall-Seminar-Paper-1-Stock-Market-Returns.pdf

Zhifeng Dai, Huan Zhu, Jie Kang, **New technical indicators and stock returns predictability**, International Review of Economics & Finance,Volume 71, 2021, Pages 127-142.  
https://parsproje.com/articles/hesabdari/h604.pdf

Books:

Cochrane, John. **Asset pricing**: Revised edition. Princeton university press, 2009.

Bali, Turan G., Robert F. Engle, and Scott Murray. **Empirical asset pricing: The cross section of stock returns**. John Wiley & Sons, 2016.

Nagel, Stefan. **Machine learning in asset pricing**. Vol. 1. Princeton University Press, 2021.

Pesaran, M. Hashem. **Time series and panel data econometrics**. Oxford University Press, 2015.
