# Captcha Cracker

The Captcha Cracker app' is available here: https://captchacracker.herokuapp.com/  

The app' uses lightweight model for optical character recognition from Hugging Face: 
https://huggingface.co/microsoft/trocr-small-printed

## Launch the app' (local)

To run the project locally, start Docker daemon, and run the following command at the root of the project:

```
> docker compose -f docker-compose-dev.yaml up -d --build
```

Open a web browser, the Captcha Cracker app' is available at [http://localhost:8504/](http://localhost:8504/).


## Launch the app' (remote server)

To run the project on DT server, run the following command at the root of the project:

```
> docker compose -f docker-compose-prod.yaml up -d --build
```

Open a web browser, the Captcha Cracker app' is available at [http://localhost:8504/](http://localhost:8504/).

