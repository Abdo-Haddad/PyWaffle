#!/usr/bin/python
# -*-coding: utf-8 -*-

# Run `python3 -m README_images.generate_plots` on root folder to generate plots for README

import matplotlib.pyplot as plt
from pywaffle.waffle import Waffle


image_folder = 'README_images/'

# Basic
fig = plt.figure(FigureClass=Waffle, rows=5, columns=10, values=[48, 46, 3])
fig.savefig(image_folder + 'basic.png', bbox_inches='tight', dpi=200)


# Use values in dictionary; use absolute value as block number, without defining columns
data = {'Democratic': 48, 'Republican': 46, 'Libertarian': 3}
fig = plt.figure(FigureClass=Waffle, rows=5, values=data, legend_conf={'loc': (0, -0.3)})
fig.savefig(image_folder + 'absolute_block_numbers.png', bbox_inches='tight', dpi=200)


# Add title, legend and background color; and change block color
data = {'Democratic': 48, 'Republican': 46, 'Libertarian': 3}
fig = plt.figure(FigureClass=Waffle, rows=5, values=data,
                 title_conf={'label': 'Vote Percentage in 2016 US Presidential Election', 'loc': 'left'},
                 colors=("#983D3D", "#232066", "#DCB732"),
                 labels=["{0} ({1}%)".format(k, v) for k, v in data.items()],
                 legend_conf={'loc': (0, -0.2), 'facecolor': '#EEEEEE', 'fontsize': 8})
fig.gca().set_facecolor('#EEEEEE')
fig.set_facecolor('#EEEEEE')
fig.savefig(image_folder + 'title_and_legend.png', bbox_inches='tight', dpi=200, facecolor='#EEEEEE')
