weather = input("Weather? (sunny/rainy/cloudy/snowy): ").lower()
emojis = {
    "sunny": "☀️",
    "rainy": "🌧️",
    "cloudy": "☁️",
    "snowy": "❄️"
}
print("Emoji:", emojis.get(weather, "🤷 Unknown"))
