"""
Function that sends a request to the MLflow model REST API to get a prediction from some input data.
"""

import os
from pathlib import Path

import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path=Path(__file__).parent.parent / '.env', override=False)
MODEL_HOST = os.getenv('MODEL_HOSTNAME')
MODEL_PORT = os.getenv('MODEL_PORT')


def crack_captcha(img_file) -> str:
    try:
        response = requests.post(url=f'{MODEL_HOST}:{MODEL_PORT}/crack', files={'file': img_file})
        response.raise_for_status()
        output = response.json()['captcha_solution']
    except (requests.HTTPError, IOError) as err:
        output = str(err)
    return output


if __name__ == '__main__':
    from pathlib import Path

    with open(Path(__file__).parent.parent.parent / 'data' / 'sample2.png', 'rb') as file:
        print(crack_captcha(img_file=file))
