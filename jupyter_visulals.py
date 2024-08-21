import plotly.express as px
import pandas as pd

# get_average_sale_price_by_year() is defined and returns a list of tuples
data = get_average_sale_price_by_year()

# Convert to a DataFrame for easier manipulation
df = pd.DataFrame(data, columns=['Year Built', 'Average Sale Price'])

# Create a line chart using Plotly
fig = px.line(df, x='Year Built', y='Average Sale Price', title='Average Sale Price by Year Built')
fig.show()

result = session.query(
    HousingPricesTrain.neighborhood,
    func.avg(HousingPricesTrain.sale_price).label('average_sale_price')
).group_by(HousingPricesTrain.neighborhood)\
 .order_by(HousingPricesTrain.neighborhood)\
 .all()

df = pd.DataFrame(result, columns=['Neighborhood', 'Average Sale Price'])
fig = px.bar(df, x='Neighborhood', y='Average Sale Price', title='Average Sale Price by Neighborhood')
fig.show()

result = session.query(
    HousingPricesTrain.year_built,
    func.count(HousingPricesTrain.id).label('count')
).group_by(HousingPricesTrain.year_built)\
 .order_by(HousingPricesTrain.year_built)\
 .all()

df = pd.DataFrame(result, columns=['Year Built', 'Count'])
fig = px.bar(df, x='Year Built', y='Count', title='Count of Houses by Year Built')
fig.show()
