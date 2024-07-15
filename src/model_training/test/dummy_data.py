import pandas as pd
import numpy as np

# Sample financial data
data = {
    'year': range(2000, 2021),
    'gdp_growth': np.random.uniform(1, 4, 21),
    'unemployment_rate': np.random.uniform(4, 10, 21)
}
df = pd.DataFrame(data)
print(df)
