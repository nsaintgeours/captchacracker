""""
kl
"""
import uvicorn
from fastapi import FastAPI, UploadFile, File

from captcha_cracker import CaptchaCracker

cracker = CaptchaCracker()
api = FastAPI()


@api.post('/crack')
async def crack(file: UploadFile = File(...)):
    image_bytes = await file.read()
    return {"captcha_solution": cracker.crack(image_bytes=image_bytes)}


if __name__ == '__main__':
    uvicorn.run(api, host='127.0.0.1', port=8000)
