import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    print("Event result ", event)
    
    body = json.loads(event["Records"][0]["body"])
    print("Body: ", body)
    
    process_v_assgn_queue(body)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }    



def process_v_assgn_queue(body):
    s3 = boto3.client("s3")
    print("Processing Queue messages")
    
    filename = body['Timestamp']+".txt"
    fileContent = body['Message']
    print("Writing Data to S3 Bucket")
    s3.put_object(Bucket="v-assement-bucket", Key=filename, Body=fileContent)
    
    
