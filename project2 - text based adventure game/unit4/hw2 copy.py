# creating 2D list
weatherList = [
    ["mon", [10, 0, "slightly cloudy and light rain 🌦️"]],
    ["tue", [14, 2, "sunny and passing clouds 🌤️"]],
    ["wed", [10, 4, "cloudy and light rain 🌧️"]],
    ["thu", [7, -2, "slightly cloudy and sunny ⛅️"]],
    ["fri", [10, -1, "cloudy and light rain 🌧️"]],
    ["sat", [7, 2, "slightly cloudy and sunny 🌤️"]],
    ["sun", [2, -2, "lots of snow :) ❄️"]]
]

# printing list
print("weather forecast from nov 3 to nov 9: ")
for day in weatherList:
    print(f"{day[0]}: high = {day[1][0]}°C, low = {day[1][1]}°C, the weather is {day[1][2]}")