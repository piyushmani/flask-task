import boto3

aws_access_key_id = 'access_key'
aws_secret_access_key = 'secret_key'
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

def upload_ml_model_to_s3(model):
    bucket_name = 'ml_models'
    model_key = 'model_key'
    model_bytes = model.encode('utf-8')

    try:
        s3.put_object(Bucket=bucket_name, Key=model_key, Body=model_bytes)
        return f"s3://{bucket_name}/{model_key}"
    except Exception as e:
        print(f"Error uploading model to S3: {e}")
        return None
