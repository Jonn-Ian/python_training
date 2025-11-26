# (AR) Auto Regressive = P
    - It tells the model how many past values of your series are used to build the forecast equation.

    The autoregressive order p is the number of lagged values of the time series included as predictors in the ARIMA model. It captures how past observations Y_{t-1},Y_{t-2},... ,Y_{t-p} help explain the current value Y_t. A larger p allows the model to use a longer memory of the past to forecast the present, which can be powerful when the series shows persistence or cyclic autocorrelation.
