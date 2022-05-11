# Captcha Cracker

The Captcha Cracker app' is available here: https://captchacracker.herokuapp.com/  

The app' uses lightweight model for optical character recognition from Hugging Face: 
https://huggingface.co/microsoft/trocr-small-printed

## Run locally

To run the project locally:

```
> python model/api.py
> streamlit run src/app.py
```

## Deploy on Heroku 

I have followed these two tutorials: 
- https://towardsdatascience.com/deploying-a-basic-streamlit-app-to-heroku-be25a527fcb3  
- https://towardsdatascience.com/a-quick-tutorial-on-how-to-deploy-your-streamlit-app-to-heroku-874e1250dadd

I installed Heroku CLI on my computer, then I deploy CaptchaCracker model and CaptchaCracker web app'
on two different Heroku dynos:

```
> heroku login
> heroku git:remote -a captchacracker-model
> heroku buildpacks:set heroku/python
> git subtree push --prefix model heroku master
```

```
> heroku login
> heroku git:remote -a captchacracker
> heroku buildpacks:set heroku/python
> git subtree push --prefix webapp heroku master
```