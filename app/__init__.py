# __init__.py
from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
import boto3, s3fs


app = Flask(__name__)

app.config["MONGO_URI"]='mongodb+srv://Vedsu:CVxB6F2N700cQ0qu@cluster0.thbmwqi.mongodb.net/webinar-website'



mongo = PyMongo(app)

cors = CORS(app)

s3_resource = boto3.resource(
    service_name = "s3",
    region_name = 'us-east-1',
    aws_access_key_id = "AKIA4JNMSYDOLRUH6DHY",
    aws_secret_access_key = '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'

)
s3_client = boto3.client(
    service_name = "s3",
    region_name = 'us-east-1',
    aws_access_key_id = "AKIA4JNMSYDOLRUH6DHY",
    aws_secret_access_key = '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')

from app import routes
