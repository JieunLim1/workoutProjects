'''importing'''
import ssl
import json
import urllib.request
import urllib.error



def get_weather_data(latitude, longitude,days):
    '''getting data from API'''

    # pylint: disable=W0212
    context = ssl._create_unverified_context()
    url = "https://api.open-meteo.com/v1/forecast?latitude=" + \
    latitude + "&longitude=" + longitude + "&hourly=temperature_2m&forecast_days=" + days
    try:
        response = urllib.request.urlopen(url,context=context)
    except urllib.error.HTTPError as e:
        print(f"{e}\nsomething went wrong with opening url")
    response_data = response.read()
    response.close()
    api_data_obj = json.loads(response_data)
    print(api_data_obj)
    return api_data_obj
