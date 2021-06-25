# NLP_WebApplication
This is a web application of NLP tasks made with [Django](https://docs.djangoproject.com/en/3.2/).  

The tasks include text generation, sentimental analysis, fill mask, machine translation, question answering and text summarization. [HuggingFace](https://huggingface.co/) is used for the pre-trained machine learning models used in the project.  

I usually use [Heroku](https://www.heroku.com/) to host websites, but due to the enormous size of the dependencies (specifically [TensorFlow](https://www.tensorflow.org/) and [PyTorch](https://pytorch.org/)), Heroku cannot be used to host this app. [AWS EC2](https://aws.amazon.com/ec2/?ec2-whats-new.sort-by=item.additionalFields.postDateTime&ec2-whats-new.sort-order=desc) and [Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/) could work, but I don’t see the necessity to host this website considering the fees associated with running instances. So the application can only run locally for now. However, you can folk the repo and follow the steps to reproduce the web application and host it on AWS or other cloud platforms if you are interested.  

- Create a virtual environment by ``` virtualenv <my_env_name>```
- Activate the env by ```<my_env_name>/bin/activate```
- Clone my Repo by ``` git clone <the https of the repo>```
- Get into the dir where manage.py is by ```cd HuggingFace```
- Install required packages by ``` pip install -r requirements.txt```.
- Make migrations by ``` python3 manage.py makemigrations```, then ``` python3 manage.py migrate```
- Run the application by ``` python3 manage.py runserver```

The functionality and screenshots of the web pages are shown as follows.

<p align="center">
  <img width="350" src="https://github.com/fangyiyu/Bitcoin_Prediction_Django/blob/master/structure.png">
</p>
