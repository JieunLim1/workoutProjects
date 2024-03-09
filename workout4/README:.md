README:

This program is designed to practice visualizing hourly temperture data from web API.

It has 4 modules that deal with web API, one to deal with file I/O, one to generate visualizations, and user interface that is responsible for asking the user some parameters of the API to use.

It uses matplotlib to plot the figure based ont he data collected from the web Open-Meteo. It is open source weather API.

The API endpoint /v1/forecast accepts a geographical coordinate, a list of weather variables and responds with a JSON hourly weather forecast for 7 days. Time always starts at 0:00 today and contains 168 hours. You can change the days of forecasts.

To start the program, first go to the starter point, which is ui.py module. Run the program.
For the latitude and longitude, it would be better to use the actual number of your location. 
For exmaple, latitude: 52.52, longitude: 13.41