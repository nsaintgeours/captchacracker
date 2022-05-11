# Captcha Cracker

The Captcha Cracker app' is available here: https://captchacracker.herokuapp.com/  

The app' uses lightweight model for optical character recognition from Hugging Face: 
https://huggingface.co/microsoft/trocr-small-printed

## Run locally

```
> streamlit run src/app.py
```

## Deploy on Heroku 

I have followed these two tutorials: 
- https://towardsdatascience.com/deploying-a-basic-streamlit-app-to-heroku-be25a527fcb3  
- https://towardsdatascience.com/a-quick-tutorial-on-how-to-deploy-your-streamlit-app-to-heroku-874e1250dadd

I installed Heroku CLI, then:
```
> heroku login
> heroku git:remote -a captchacracker
> heroku buildpacks:set heroku/python
> git push heroku master
```