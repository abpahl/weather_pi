import requests
import argparse

#Global_variables

realtime_url = "https://api.climacell.co/v3/weather/realtime"
location = '"lat":"45.067846","lon":"-93.424426"'
#querystring = {"lat":"45.067846","lon":"-93.424426","unit_system":"us","fields":"temp,wind_speed,cloud_cover,cloud_base,surface_shortwave_radiation,precipitation,precipitation_type","apikey":"REDACTED"}

#response = requests.request("GET", url, params=querystring)

#print(response.text)


class SmartFormatter(argparse.HelpFormatter):

    def _split_lines(self, text, width):
        if text.startswith('R|'):
            return text[2:].splitlines()  
        # this is the RawTextHelpFormatter._split_lines
        return argparse.HelpFormatter._split_lines(self, text, width)



def weather_query(params):
	print("hello")
## Available params:
#precipitation, precipitation_type, temp, feels_like, dewpoint, wind_speed, wind_gust, baro_pressure, visibility, humidity, wind_direction, sunrise, sunset, cloud_cover, cloud_ceiling, cloud_base, surface_shortwave_radiation, moon_phase, weather_code




def main():
	parser = argparse.ArgumentParser(description='Python script to query the ClimaCell weather API and process the resulting dataset',formatter_class=SmartFormatter)
	parser.add_argument('--apikey',help='Provide an API key for ClimaCell')
	parser.add_argument('--weather_params',help='R| The list of weather parameters to query. \n Available Options: \n\t precipitation\n\t precipitation_type\n\t temp\n\t feels_like\n\t dewpoint\n\t wind_speed\n\t wind_gust\n\t baro_pressure\n\t visibility\n\t humidity\n\t wind_direction\n\t sunrise\n\t sunset\n\t cloud_cover\n\t cloud_ceiling\n\t cloud_base\n\t surface_shortwave_radiation\n\t moon_phase\n\t weather_code')
	args = parser.parse_args()

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()