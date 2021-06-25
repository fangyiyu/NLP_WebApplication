# NLP_WebApplication
This is a web application of NLP tasks made with [Django](https://docs.djangoproject.com/en/3.2/).  

The tasks include text generation, sentimental analysis, fill mask, machine translation, question answering and text summarization. [HuggingFace](https://huggingface.co/) is used for the pre-trained machine learning models used in the project.  

I usually use [Heroku](https://www.heroku.com/) to host websites, but due to the enormous size of the dependencies (specifically [TensorFlow](https://www.tensorflow.org/) and [PyTorch](https://pytorch.org/)), Heroku cannot be used to host this app. [AWS EC2](https://aws.amazon.com/ec2/?ec2-whats-new.sort-by=item.additionalFields.postDateTime&ec2-whats-new.sort-order=desc) and [Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/) could work, but I don’t see the necessity to host this website considering the fees associated with running instances. So the application can only run locally for now. However, you can folk the repo and follow the steps to reproduce the web application and host it on AWS or other cloud platforms if you are interested. You may need to make some Django configurations related to static files and security when hosting it publicly depending on which cloud service you use, refer to the documentations linked previously.


### Run the application locally
- Create a virtual environment by ``` virtualenv <my_env_name>```
- Activate the env by ```<my_env_name>/bin/activate```
- Clone my Repo by ``` git clone <the https of the repo>```
- Get into the directory where manage.py is.
- Install required packages by ``` pip install -r requirements.txt```.
- Make migrations by ``` python3 manage.py makemigrations```, then ``` python3 manage.py migrate```
- Run the application by ``` python3 manage.py runserver```

The functionality and screenshots of the web pages are shown as follows.

_Homepage_
<p align="center">
  <img width="900" src="https://github.com/fangyiyu/NLP_WebApplication/blob/master/images/1.png">
</p>

_Text Generation_
<p align="center">
  <img width="900" src="https://github.com/fangyiyu/NLP_WebApplication/blob/master/images/2.png">
</p>
<p align="center">
  <img width="900" src="https://github.com/fangyiyu/NLP_WebApplication/blob/master/images/3.png">
</p>

_Text Summarization_
<p align="center">
  <img width="900" src="https://github.com/fangyiyu/NLP_WebApplication/blob/master/images/4.png">
</p>
<p align="center">
  <img width="900" src="https://github.com/fangyiyu/NLP_WebApplication/blob/master/images/5.png">
</p>

_Question Answering_
<p align="center">
  <img width="900" src="https://github.com/fangyiyu/NLP_WebApplication/blob/master/images/6.png">
</p>
<p align="center">
  <img width="900" src="https://github.com/fangyiyu/NLP_WebApplication/blob/master/images/7.png">
</p>

_Sentimental Analysis_
<p align="center">
  <img width="900" src="https://github.com/fangyiyu/NLP_WebApplication/blob/master/images/8.png">
</p>
<p align="center">
  <img width="900" src="https://github.com/fangyiyu/NLP_WebApplication/blob/master/images/9.png">
</p>

_Machine Translation_
<p align="center">
  <img width="900" src="https://github.com/fangyiyu/NLP_WebApplication/blob/master/images/10.png">
</p>
<p align="center">
  <img width="900" src="https://github.com/fangyiyu/NLP_WebApplication/blob/master/images/11.png">
</p>

