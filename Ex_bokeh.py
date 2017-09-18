# -*- coding: utf-8 -*-
"""
Created on Wes Nov 16 17:17:08 2016

@author: Yi Li
"""

from bokeh.io import show, output_file
from bokeh.models import (
    ColumnDataSource,
    HoverTool,
    LogColorMapper
)
#from bokeh.palettes import Viridis6 as palette
from bokeh.palettes import YlGn3 as palette
from bokeh.plotting import figure
# import sample data
from bokeh.sampledata.us_counties import data as counties
from bokeh.sampledata.unemployment import data as unemployment

palette.reverse()
# country name
counties = {
    code: county for code, county in counties.items() if county["state"] == "tx"
}
# counties' longitudes and latitudes
county_xs = [county["lons"] for county in counties.values()]
county_ys = [county["lats"] for county in counties.values()]
# counties' names, unemployment rates, and the color mapper
county_names = [county['name'] for county in counties.values()]
county_rates = [unemployment[county_id] for county_id in counties]
color_mapper = LogColorMapper(palette=palette)
#color_mapper = LogColorMapper(palette=small_palettes)
# data
source = ColumnDataSource(data=dict(
    x=county_xs,
    y=county_ys,
    name=county_names,
    rate=county_rates,
))
# bokeh tools to be used
TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"
# plot the figure
p = figure(
    title="Texas Unemployment, 2009", tools=TOOLS,
    x_axis_location=None, y_axis_location=None
)
p.grid.grid_line_color = None
# parameters for patches of the figure
p.patches('x', 'y', source=source,
          fill_color={'field': 'rate', 'transform': color_mapper},
          fill_alpha=0.7, line_color="white", line_width=0.5)
# display hover
hover = p.select_one(HoverTool)
hover.point_policy = "follow_mouse"
hover.tooltips = [
    ("Name", "@name"),
    ("Unemployment rate", "@rate%"),
    ("(Long, Lat)", "($x, $y)"),
]
# output to static HTML file
output_file(“Ex_bokeh1.html")
show(p)


##Another country
def Country2():
    # import sample data
    from bokeh.sampledata.us_counties import data as counties
    from bokeh.sampledata.unemployment import data as unemployment
    # country name
    counties = {
        code: county for code, county in counties.items() if county["state"] == "ca"
    }
    # counties' longitudes and latitudes
    county_xs = [county["lons"] for county in counties.values()]
    county_ys = [county["lats"] for county in counties.values()]
    # counties' names, unemployment rates, and the color mapper
    county_names = [county['name'] for county in counties.values()]
    county_rates = [unemployment[county_id] for county_id in counties]
    color_mapper = LogColorMapper(palette=palette)
    #color_mapper = LogColorMapper(palette=small_palettes)
    # data    
    source = ColumnDataSource(data=dict(
        x=county_xs,
        y=county_ys,
        name=county_names,
        rate=county_rates,
    ))
    # bokeh tools to be used
    TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"
    # plot the figure
    p2 = figure(
        title="CA Unemployment, 2009", tools=TOOLS,
        x_axis_location=None, y_axis_location=None
    )
    p2.grid.grid_line_color = None
    # parameters for patches of the figure
    p2.patches('x', 'y', source=source,
              fill_color={'field': 'rate', 'transform': color_mapper},
              fill_alpha=0.7, line_color="white", line_width=0.5)
    # display hover
    hover = p2.select_one(HoverTool)
    hover.point_policy = "follow_mouse"
    hover.tooltips = [
        ("Name", "@name"),
        ("Unemployment rate", "@rate%"),
        ("(Long, Lat)", "($x, $y)"),
    ]
    # output to static HTML file
    output_file(“Ex_bokeh2.html")
    show(p2)
Country2()