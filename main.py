import requests


def main():
    places = ['svo', 'london', 'cherepovets']
    url_template = 'https://wttr.in/{0}'
    payload = {
        'M': '',
        'n': '',
        'q': '',
        'T': '',
        'lang': 'ru',
    }

    for place in places:
        url = url_template.format(place)
        response = requests.get(url, params=payload)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()