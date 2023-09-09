import json
import numpy as np
import pandas as pd
import plotly.express as px

import plotly.io as pio
pio.renderers.default = 'browser'
india_states = json.load(open("states_india.geojson", "r"))


state_id_map = {}
for feature in india_states["features"]:
    feature["id"] = feature["properties"]["state_code"]
    state_id_map[feature["properties"]["st_nm"]] = feature["id"]

df = pd.read_csv("india_census.csv")
df["Density"] = df["Population"]#.apply(lambda x: int(x.split("/")[0].replace(",", "")))
df["id"] = df["State or union territory"].apply(lambda x: state_id_map[x])

df.head()

fig = px.choropleth(
    df,
    locations="id",
    geojson=india_states,
    color="Population",
    hover_name="State or union territory",
    hover_data=["Population"],
    title="India Population",
)
fig.update_geos(fitbounds="locations", visible=False)
fig.show()
