Title: Iron Blogging - Simplifying Workflows
Date: 2016-01-26
Modified: 2016-01-26
kind: article
author: Jacob Thebault-Spieker
published: true

> _This post is a part of the GroupLens Iron Blogging effort, so take that for what you will._

I do a fair amount of spatial data analysis, particularly in the space of trying to understand geographic disparity, and its effects on systems.

This workflow used to go something like:

1. Setup a [Postgresql](http://www.postgresql.org)/[PostGIS](http://postgis.net) database
2. import all the data (including points or polygons that reflect geographic regions)
	* this often involves replicating geometries because there are individual data points that apply to the same geometry
3. do any aggregation or summary statistics _per geometry_ that I needed to do, and apply these values to each Postgres record
4. use `pgsql2shp` command, to dump a database table (or a subset of the table, by query) to get a [shapefile](https://en.wikipedia.org/wiki/Shapefile)
	* this often involves at least one `GROUP BY` clause
5. Open this shapefile in [QGIS](http://qgis.org/en/site/), to do some exploratory mapping, and save the data as a CSV file for later
6. Open this shapefile in [GeoDa](https://geodacenter.asu.edu/software/downloads), to do some simple exploratory analysis
7. Import the aforementiond CSV file into R, and then write R code to do any data transformation needed
8. Use R for any analysis (normally spatial regressions, with `spdep`)

You'll notice here, that around step 7, we lose any concept of the geometry of this geographic data. Unfortunately, this means that if I any of the things below, that I need to start again at Step 3:

* a different geographic subset of the data for analysis, or
* a different geographic function (say, population density), or
* anything at the R stage that isn't already there



There is a better world.

For a different project, I recently started using [Jupyter](http://Jupyter.org), for easier collaboration.

At first, it was nice, because I could just import CSVs into Jupyter, and use _Python_ (specifically pandas, which is incredibly nice) for the data transformation. This is better for me than R. However, I quickly started wondering if there is a way insert Jupyter and python earlier into my workflow.

As it turns out, a lot of the geographic analysis software (QGIS, GeoDa, steps 5 and 6 respectively) is built on top of existing python libraries. That's a good sign, but it made me worry I'd have to drop down a level and code more, which would be a time sink. Enter: [GeoPandas](http://geopandas.org).

GeoPandas, or geographic extension to [Pandas](http://pandas.pydata.org), is a whole new game. GeoPandas lets me load a GeoDataFrame (you know, a DataFrame, with _geography_) either from a shapefile (we're now at step 4), or even better _directly from PostGIS_.

Because Pandas (and subsequently GeoPandas) has such nice `groupby()` and `agg()` functionality, I don't need to write these things in SQL. Because GeoPandas also has a concept of geometric operations (point in polygon, intersection, etc.) and _spatial joins_ (merging datasets based on geographic overlap) I can insert the Python/Jupyter workflow _after Step 2_.

I mentioned before that a lot of the geographic analysis software was built on python libraries. As it turns out, GeoDa is built on top of a library called [pysal](https://geodacenter.asu.edu/pysal). This means that I can do any analysis supported by GeoDa (including spatial regressions) directly from python.

My workflow now looks like:

1. Setup a Postgresql/PostGIS database
2. import all the data (including points or polygons that reflect geographic regions)
	* this often involves replicating geometries because there are individual data points that apply to the same geometry
3. Load this table into Jupyter (with GeoPandas), and perform any aggregation, summary statistics, or data transformation I need, which either become a new column, or perhaps a transformed GeoDataFrame (remember `groupby()`?)
4. Do any exploratory mapping, exploratory analysis, or more involved spatial analysis _directly within Jupyter_.

So, I've now cut the number of different steps in half, and dropped the number of different ways I work with this data (including different languages used) from 5 to 1 (or maybe 2, if you count the single line of SQL I'm writing to dump data out of my database).

I've long resisted Python, because I know Java or Javascript, and it wasn't clear what Python got me.

I was so wrong.
