import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/CoronaTimeSeries.csv')

# Preparing data
#Takes one value which is recovered
#uses the day and month to track this one value on the x and y axis
# color scale set to jet to vary the color value
data = [go.Heatmap(x=df['Day'],
                   y=df['WeekofMonth'],
                   z=df['Recovered'].values.tolist(),
                   colorscale='Jet')]

# Preparing layout
#This takes the title x and y axis text
layout = go.Layout(title='Corona Virus Recovered Cases', xaxis_title="Day of Week",
                   yaxis_title="Week of Month")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='heatmap.html')
