AI Assignment 2

Name: Naga Sai Jathin Madineni 
Roll Number: SE24UCSE015

About this assignment:
This assignment contains three Python programs based on Artificial Intelligence concepts. The programs demonstrate search algorithms, CAPTCHA generation, and a reflex agent for
calculating Air Quality Index (AQI).

1.  Missionaries and Cannibals Problem

This program solves the classic Missionaries and Cannibals problem using
different search algorithms.

In this problem, there are 3 missionaries and 3 cannibals on one side of
a river. They must cross the river using a boat that can carry only two
people at a time. The rule is that the number of cannibals should never
be greater than the number of missionaries on either side.

Each situation is represented as a state showing how many missionaries
and cannibals are on the left side and where the boat is located.

Algorithms implemented: - Breadth First Search (BFS) - Uniform Cost
Search (UCS) - Depth First Search (DFS) - Depth Limited Search (DLS) -
Iterative Deepening DFS (IDDFS)

Implementation file: missionaries and cannibals all bfs and dfs.py

2.  CAPTCHA Generator

This program generates a CAPTCHA image and asks the user to enter the
text shown in the image.

A random string containing letters and numbers is generated first. Then
an image is created using the Python PIL library and the text is drawn
on the image. Random lines and dots are added as noise so that bots
cannot easily read the CAPTCHA.

The image is displayed to the user and the user must enter the
characters correctly. If the input matches the generated CAPTCHA text,
the program prints a success message. Otherwise it shows that the
CAPTCHA is incorrect.

Implementation file: Captcha.py

3.  AQI Reflex Agent

This program implements a simple reflex agent that calculates the Air
Quality Index using pollution data.

The program reads pollutant values such as PM2.5, PM10, NO2, SO2, CO,
NH3, and O3 from a dataset and calculates the sub-index for each
pollutant using predefined AQI breakpoint ranges. The pollutant with the
highest sub-index becomes the dominant pollutant and determines the
final AQI.

Based on the AQI value, the air quality is categorized into levels such
as: Good, Satisfactory, Moderate, Poor, Very Poor, and Severe.

The dataset visakhapatnam_aqi.csv should be downloaded and kept in the
same folder as the program so that the program can read the data.

Implementation file: aqi_agent.py

Dataset used: visakhapatnam_aqi.csv

Tools and Libraries Used Python Pandas PIL (Python Imaging Library)

Conclusion Through this assignment, different AI concepts were
implemented using Python programs. The Missionaries and Cannibals
program demonstrates search algorithms, the CAPTCHA program shows a
simple human verification system, and the AQI reflex agent demonstrates
how an agent can make decisions based on environmental data.
