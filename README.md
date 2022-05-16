# Captcha Cracker

The Captcha Cracker app' is used to crack "cloud of words" captcha images, like this one:

![](data/sample.jpg)

The app' uses a lightweight model for optical character recognition from Hugging Face: 
https://huggingface.co/microsoft/trocr-small-printed

## Launch the app'

To run the project on your computer:

* clone the content of this Git repository:

```
> git clone git@gitlab.com:data-terrae/projects/captchacracker.git
```

* make sure you have Docker installed (version should be `>= 20.10`): 
  
`> docker version`

* make sure you have Docker Compose V2 installed (version should be `>= 2.2.3`)
  
`> docker compose version`

* start your Docker daemon


* run the following command at the root of the project:

```
> docker compose up -d --build
```

* open a web browser, the Captcha Cracker app' is available at [http://localhost:8504/](http://localhost:8504/).


## Launch the app' (Docker Compose V1)

In case you are using Docker Compose V1 instead of Docker Compose V2, you can launch the Captcha Cracker app' using a
slightly different Docker Compose file. Just run the following command at the root of the project:

```
> sudo docker compose -f docker-compose-prod.yaml up -d --build
```

Open a web browser, the Captcha Cracker app' is available at [http://localhost:8504/](http://localhost:8504/).

