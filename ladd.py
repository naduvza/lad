from bs4 import BeautifulSoup
import requests
import os


class WeatherScraper:
    def __init__(self, region_urls):
        self.region_urls = region_urls

    def get_temperature(self, region):
        url_weather = self.region_urls.get(region)
        if url_weather:
            response_weather = requests.get(url_weather)
            if response_weather.status_code == 200:
                soup_weather = BeautifulSoup(response_weather.text, features="html.parser")
                temp = soup_weather.find("p", class_="today-temp").text.strip()
                return temp


class WeatherApp:
    def __init__(self, scraper):
        self.scraper = scraper

    def display_regions(self):
        print("Виберіть західну область України для перевірки температури:")
        for i, region in enumerate(self.scraper.region_urls.keys(), 1):
            print(f"{i}. {region}")

    def run(self):
        self.display_regions()
        try:
            choice = int(input("Введіть номер області: "))
            if 1 <= choice <= len(self.scraper.region_urls):
                region_name = list(self.scraper.region_urls.keys())[choice - 1]
                print(f"Температура в {region_name}: {self.scraper.get_temperature(region_name)}")
            else:
                print("Невірний номер області.")
        except ValueError:
            print("Введено некоректне значення.")


if __name__ == "__main__":
    os.system("chcp 65001")
    regions = {
        "Lviv": "https://ua.sinoptik.ua/погода-львів",
        "Ivano-Frankivsk": "https://ua.sinoptik.ua/погода-івано-франківськ",
        "Rivne": "https://ua.sinoptik.ua/погода-ривне",
        "Ternopil": "https://ua.sinoptik.ua/погода-тернопіль",
        "Chernivtsi": "https://ua.sinoptik.ua/погода-чернівці",
    }

    scraper = WeatherScraper(regions)
    app = WeatherApp(scraper)
    app.run()
