"""
Function that sends a request to the MLflow model REST API to get a prediction from some input data.
"""

import requests

MODEL_HOST = 'https://captchacracker.herokuapp.com'
MODEL_HOST = 'http://127.0.0.1:8000'


def crack_captcha(img_file) -> str:
    try:
        response = requests.post(url=f'{MODEL_HOST}/crack', files={'file': img_file})
        response.raise_for_status()
        output = response.json()['captcha_solution']
    except (requests.HTTPError, IOError) as err:
        output = str(err)
    return output


if __name__ == '__main__':
    from pathlib import Path

    with open(Path(__file__).parent.parent.parent / 'data' / 'sample2.png', 'rb') as file:
        print(crack_captcha(img_file=file))
