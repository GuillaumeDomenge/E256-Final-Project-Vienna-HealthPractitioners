import geopandas as gpd
from shapely.geometry import Polygon
import matplotlib.pyplot as plt

# Define the polygons and associated values
data = {
    'geometry': [
        Polygon([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]),
        Polygon([[1, 1], [2, 1], [2, 2], [1, 2], [1, 1]]),
    ],
    'value': [10, 20]
}

# Create a GeoDataFrame
gdf = gpd.GeoDataFrame(data)

# Set the geometry column explicitly
gdf.set_geometry('geometry', inplace=True)

# Plot the choropleth map
fig, ax = plt.subplots()
gdf.plot(column='value', cmap='viridis', ax=ax, legend=True)
plt.title('Choropleth Map')
plt.show()