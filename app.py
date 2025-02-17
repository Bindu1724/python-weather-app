import requests

api_key='76928f391536214dc3babc0791ea0707'

##getting user input
user_input = input("Enter city: ")

#print(user_input)
##API requests
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}"
)
##displaying weather data status code if 200 then successful
#print(weather_data.status_code)

##displaying weather data
#print(weather_data.json())

##error handling
if weather_data.json()['cod'] == '404':
    print("No city found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    pressure = weather_data.json()['main']['pressure']
    humidity = weather_data.json()['main']['humidity']


    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}°F")
    print(f"The pressure in {user_input} is: {pressure}")
    print(f"The humidity in {user_input} is: {humidity}")




