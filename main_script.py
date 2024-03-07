import os
import json
from ml.processing import process_csv, generate_model, evaluate_model
import requests
from utils import upload_ml_model_to_s3

csv_file_location = os.environ.get('CSV_FILE_LOCATION')
target_column = os.environ.get('TARGET_COLUMN')

def main():
    tenant_res = call_api("http://127.0.0.1:5000/api/tenant", {"name":"name"})
    tenant_id = json.loads(tenant_res.text).get('id')

    data = process_csv(csv_file_location)
    model = generate_model(data, target_column)
    results = evaluate_model(model, data, tenant_id, target_column)

    s3_location = upload_ml_model_to_s3(model)

    payload = {
        "tenant": tenant_id,
        "csv_location": csv_file_location,
        "s3_location": s3_location,
        "results": results
    }
    response = call_api("http://127.0.0.1:5000/api/project_metadata", payload)

    print (response.text)

def call_api(url, payload):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response

if __name__ == "__main__":
    main()
