"""
Import libraries and read the CSV dataset into a pandas dataframe before displaying datatypes
Convert columns to numeric format then select values within the bounding map box
Create a geodataframe from the dataframe and plot the geodataframe on the map
"""
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

df = pd.read_csv("Growlocations.csv")
print(df.head(10))
print(df.dtypes)

df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")
df = df.dropna() # Drop missing or invalid values

Lat_min = 50.681 
Lat_max = 57.985
Lon_min = -10.592
Lon_man = 1.6848

# Columns reversed due error in CVS file
df = df[(df["Latitude"] >= Lon_min) & (df["Latitude"] <= Lon_man)]
df = df[(df["Longitude"] >= Lat_min) & (df["Longitude"] <= Lat_max)]
points = gpd.points_from_xy(df["Latitude"], df["Longitude"], crs="EPSG:4326")

gdf = gpd.GeoDataFrame(df, geometry=points) 
set = set(points)
print(len(set)) # Print number of points

img = mpimg.imread("map7.png")
fig, ax = plt.subplots(figsize=(10,10))
ax.imshow(img, extent=[Lon_min, Lon_man, Lat_min, Lat_max])
gdf.plot(ax=ax, color="purple", markersize=10)
plt.title("Locations of the GROW Sensors in the UK")
plt.show()

""" Reference:
Stack Overflow. (2023, January 31). Python - How to Display an Image. Retrieved December 30, 2023 from https://stackoverflow.com/questions/35286540/how-to-display-an-image
Stack Overflow. (2023, February 2). Python - hHow to Plot a Map Using Geopandas and Matplotlib. Retrieved December 30, 2023 from https://stackoverflow.com/questions/72322456/how-to-plot-a-map-using-geopandas-and-matplotlib
"""