'''starter of the program'''
import weather
import generator
import writing_file

if __name__ =="__main__":
    lat = input("enter latitude:\n")
    long = input("enter longitude:\n")
    days = input("how many days of forecast?\n")
    file = input("enter a name of a file:\n")
    data = weather.get_weather_data(lat,long,days)
    writing_file.write_in_file(data,file)
    generator.generate(data['hourly'],file)
