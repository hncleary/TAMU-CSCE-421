import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from scipy.optimize import minimize
import scipy.stats as stats
import pymc3 as pm3
import numdifftools as ndt
import statsmodels.api as sm
from statsmodels.base.model import GenericLikelihoodModel


# def MLEFunction(X, Y):
#     x = X
#     y = Y
#
#     df = pd.DataFrame({'y':y, 'x':x})
#     df['constant'] = 1
#
#     # sns.regplot(df.x, df.y)


