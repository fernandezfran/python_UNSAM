#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# dataset típico : Clasificación de especies de flores iris
iris_dataset = load_iris()
iris_df = pd.DataFrame(iris_dataset['data'], columns=iris_dataset.feature_names)

# visualización de los datos
#pd.plotting.scatter_matrix(iris_df, c=iris_dataset['target'], figsize=(15,15),
#                           marker='o', hist_kwds={'bins': 20}, s=60, alpha=0.5)
iris_df['target'] = iris_dataset['target']
sns.pairplot(iris_df, hue='target')
plt.show()
