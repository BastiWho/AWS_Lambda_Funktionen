import json
import boto3

def lambda_handler(event, context):
    
    s3 = boto3.client('s3')
    bucket_name = 'monday-s3-526241'
    file_name = event["pathParameters"]["messageid"]
    
    response = s3.get_object(
    Bucket=bucket_name,
    Key=file_name,
    )
    
    data = response['Body'].read().decode('utf-8')
    
    response = s3.delete_object(
    Bucket=bucket_name,
    Key=file_name,
    )
    
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }
