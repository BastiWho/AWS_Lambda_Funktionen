import json
import boto3
import uuid

def lambda_handler(event, context):
    # TODO implement
    
    message = event["body"]
    
    s3 = boto3.client('s3')
    
    bucket_name = 'monday-s3-526241'
    file_name = str(uuid.uuid4()) + '.txt'
    file_content = message
    
    print("ok")
    response = s3.put_object(
    Body=file_content,
    Bucket=bucket_name,
    Key=file_name
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('https://5xn78djgb0.execute-api.eu-central-1.amazonaws.com/'+file_name)
    }
