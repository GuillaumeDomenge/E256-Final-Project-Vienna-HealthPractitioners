from shapely.geometry import Polygon
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MplPolygon

# Define the vertices of the polygon
polygon_vertices = [(1, 1), (3, 1), (2, 3)]

# Create a shapely Polygon object
polygon = Polygon(polygon_vertices)

# Plotting the polygon with transparency
fig, ax = plt.subplots()

# Create a matplotlib Polygon patch from the shapely polygon
poly_patch = MplPolygon(polygon.exterior.coords, closed=True)

# Set the facecolor of the patch with transparency (alpha=0.5 for 50% transparency)
poly_patch.set_facecolor('blue')
poly_patch.set_alpha(0.1)

# Add the patch to the axes
ax.add_patch(poly_patch)
polygon_vertices = [ (3, 1), (2, 3),(4,3)]
polygon = Polygon(polygon_vertices)

# Plotting the polygon with transparency

# Create a matplotlib Polygon patch from the shapely polygon
poly_patch = MplPolygon(polygon.exterior.coords, closed=True)
poly_patch.set_facecolor('red')
poly_patch.set_alpha(0.3)

# Set the x and y axis limits
ax.set_xlim([0, 4])
ax.set_ylim([0, 4])

# Show the plot
plt.show()