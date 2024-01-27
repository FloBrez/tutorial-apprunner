import os
import json
import boto3
from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        name = os.environ.get('NAME')
        if name == None or len(name) == 0:
            name = "world"
        message = "Good morning with Flask, " + name + "!\n"
        return message


    @app.route('/s3')
    def test_s3():
        s3 = boto3.resource('s3')
        try:
            message = json.loads(s3.Object('blommberch', 'daten/db-isin-test/AT0000272505.json').get().get('Body').read().decode())
        except:
            message = {'Error': 'S3 access failed.'}
        return message


    @app.route('/ddb')
    def test_ddb():
        try:
            WERTPAPIERE = boto3.resource('dynamodb').Table('Wertpapiere')
            message = WERTPAPIERE.get_item(Key={'PK': 'ISIN#DE000GP4MFJ1', 'SK': 'KURS#2024-01-12'}).get('Item')
        except:
            message = {'Error': 'DynamoDB access failed.'}
        return message


    #if __name__ == "__main__":
    #    port = int(os.environ.get("PORT"))
    #    app.run(host='0.0.0.0', port=5000)

    return app