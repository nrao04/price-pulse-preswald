# import libs
from preswald import connect, get_df, query, table, text, slider, plotly
import pandas as pd
import plotly.express as px

# connect to preswald and load dataset
connect()
df = get_df("sample_csv")

# header and intro
text("# Price Pulse 📊")
text("Explore item sales and value")

# add slider to filter by value
threshold = slider("Set value threshold 🎚️", min_val=0, max_val=600, default=50)

# filter data based on slider
filtered_df = df[df["value"] > threshold]

# show filtered data table
table(filtered_df, title="items above selected value")

# scatter plot quantity vs value
fig = px.scatter(
    filtered_df,
    x="quantity",
    y="value",
    color="item",
    title="📈 quantity vs value of filtered items",
    labels={"quantity": "quantity sold", "value": "item value ($)"}
)

# style the plot
fig.update_traces(
    textposition='top center',
    marker=dict(size=12)
)
fig.update_layout(template='plotly_white')

# show the plot
plotly(fig)

# footer
text("made using preswald :)")