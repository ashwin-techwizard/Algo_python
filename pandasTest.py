import pandas as pd
excel_file = 'D:\Work\PythonWorkSpace\PadasDemo\Sample Data.xlsx'
movies = pd.read_excel(excel_file,sheet_name="SALES")
movies.describe()

print(movies.columns)
sorted_by_gross = movies.sort_values(['FINAL_BILL'], ascending=False)
# sorted_by_gross = movies.sort_values(['Gross Earnings'], ascending=False)

import matplotlib.pyplot as plt

# sorted_by_gross['FINAL_BILL'].head(10).plot(kind="barh")
# plt.show()

# movies['IMDB Score'].plot(kind="hist")
# plt.show()

# movies.describe()

# movies["FINAL_BILL"].mean()

movies_subset = movies[['Year', 'Gross Earnings']]
movies_subset.head()
earnings_by_year = movies_subset.pivot_table(index=['Year'])
# earnings_by_year.head()

earnings_by_year.plot()
plt.show()