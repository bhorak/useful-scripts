# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.2
#   kernelspec:
#     display_name: Python 3
#     name: python3
# ---

import pandas as pd
import os
import sidetable
from pathlib import Path

data = pd.read_csv('__path__')

data.head()

data.info()

data.stb.missing(style=True)



