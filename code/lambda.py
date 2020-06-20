"""

This module includes the main AWS Lambda function for data transformation.

The `handler` Lambda function below is meant to be called within the AWS Kinesis Firehose.
See https://docs.aws.amazon.com/firehose/latest/dev/data-transformation.html
"""

import base64
import json


class Transformer:
    def __init__(self, weather_data):
        self.data = weather_data

    def transform(self):
        return {
            'description': self.data['weather'][0]['description'],
            'temperature': self.data['main']['temp'],
            'humidity': self.data['main']['humidity'],
            'wind_speed': self.data['wind']['speed'],
            'city': self.data['name']
        }


class Record:
    def __init__(self, payload):
        self.record_id = payload.get('recordId')

        self.encoded = payload.get('data')

    def process(self):
        data = json.loads(
            base64.standard_b64decode(self.encoded).decode("utf-8")
        )
        transformed = Transformer(data).transform()
        
        # encode and return as required by Kinesis Firehose
        payload = base64.standard_b64encode(
            json.dumps(transformed).encode("utf-8")
        )
        return {
            'recordId': self.record_id,
            'data': payload,
            'result': 'Ok'
        }


# entrypoint
def handler(event, _context):
    """Lambda entrypoint on KDF to handle data transformation."""
    return {
        'records': [
            Record(record).process()
            for record in event.get('records')
        ]
    }
