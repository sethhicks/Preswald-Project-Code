import preswald
from preswald import connect, get_df, query, plotly, table, text
import plotly.express as px

connect()  # Initialize connection to preswald.toml data sources
df = get_df("data/my_dataset.csv")  # Load data

sql = "SELECT d.City, AVG(CAST(d.Water_Quality_Index AS DOUBLE)) AS Average_Water_Quality FROM data/my_dataset.csv AS d GROUP BY (d.City);"
filtered_df = query(sql, "data/my_dataset.csv")

text("# Average Water Quality of Chinese Cities")

# Create a bar graph
fig = px.bar(filtered_df, x="City", y="Average_Water_Quality")
plotly(fig)

# Displays

