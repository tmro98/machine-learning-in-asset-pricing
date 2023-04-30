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

- the $\mathbb{E}_t[.]$ term is the time $t$ conditional expectation of $r_{i,t+1}$, given the information set $\mathcal{F}_t$ 
- $\varepsilon_{t,i+1}$ is a zero-mean unpredictable disturbance term
- $g(.)$ is a flexible function of predictor variables, which are expressed in terms of the P-dimensional vector $x_{i,t}$

The function $g(.)$ does neither depend on $i$ nor on $t$. This allows the model to leverage information from the entire panel (across stocks and  time) and lends stability to the model estimates (at least in theory).
  
<br>

### **Time-series approach (using a single multivariate time-series):**

Let the S&P500 be the **only** asset under consideration (only a single time-series is now of interest). The ovearching model reduces to

$$
r_{t+1} = \mathbb{E}_t[r_{t+1} \mid \mathcal{F}_t] + \varepsilon_{t+1},
$$

with


$$
\mathbb{E}_t[r_{t+1} \mid \mathcal{F}_t] = g(x_{t}).
$$

Since the S&P500 is a good proxy for the US equity market as a whole, its excess return can be understood  as the equity risk premium (i.e. the market premium for bearing equity risk).

Machine Learning methods are employed to provide an estimate of $g(.)$.

---

<br>

## Related literature

Shihao Gu, Bryan Kelly, Dacheng Xiu (2020), **Empirical Asset Pricing via Machine Learning**. The Review of Financial Studies, Volume 33, Issue 5, Pages 2223–2273.  
https://academic.oup.com/rfs/article/33/5/2223/5758276

Rapach, David and Zhou, Guofu (2022), **Asset Pricing: Time-Series Predictability**. Oxford Research Encyclopedia of Economics and Finance.  
https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3941499

Goyal, Amit and Welch, Ivo and Zafirov, Athanasse (2023) **A Comprehensive 2021 Look at the Empirical Performance of Equity Premium Prediction II**. Swiss Finance Institute Research Paper No. 21-85.  
https://ssrn.com/abstract=3929119 

John Y. Campbell, Samuel B. Thompson (2008) **Predicting Excess Stock Returns Out of Sample: Can Anything Beat the Historical Average?**, The Review of Financial Studies, Volume 21, Issue 4, Pages 1509–1531.  
https://academic.oup.com/rfs/article/21/4/1509/1567518

Allan Timmermann, Clive W.J. Granger (2004), **Efficient market hypothesis and forecasting**. International Journal of Forecasting, Volume 20, Issue 1, Pages 15-27.  
https://www.sciencedirect.com/science/article/abs/pii/S0169207003000128

Rapach, David and Zhou, Guofu (2019) **Time-Series and Cross-Sectional Stock Return Forecasting: New Machine Learning Methods**.  
https://ssrn.com/abstract=3428095 

Rossi, Alberto G. "**Predicting stock market returns with machine learning.**" (2018).  
https://mendoza.nd.edu/wp-content/uploads/2019/07/2018-Alberto-Rossi-Fall-Seminar-Paper-1-Stock-Market-Returns.pdf

Books:

Cochrane, John (2009), **Asset pricing**: Revised edition. Princeton university press.

Bali, Turan G., Robert F. Engle, and Scott Murray (2016), **Empirical asset pricing: The cross section of stock returns**. John Wiley & Sons.

Nagel, Stefan (2021), **Machine learning in asset pricing**. Vol. 1. Princeton University Press.

Pesaran, M. Hashem (2015), **Time series and panel data econometrics**. Oxford University Press.
