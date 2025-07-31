import requests


def main():
    places = ['svo', 'london', 'cherepovets']
    url_template = 'https://wttr.in/{0}?MnqT&lang=ru'

    for place in places:
        url = url_template.format(place)
        response = requests.get(url)
        print(response.text)


if __name__ == '__main__':
    main()