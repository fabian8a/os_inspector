from flask import Flask, request, jsonify
import json
import boto3
from datetime import datetime

app = Flask(__name__)

@app.route('/collect', methods=['POST'])
def collect_data():
    data = request.json 
    print(data)
    
    server_ip = data['server_ip']
    server_ip2 = server_ip.replace("." , "_")
    date_str = datetime.now().strftime('%Y-%m-%d')
    filename = f"{server_ip2}_{date_str}.json"


    with open(filename,'w') as file_json:
         json.dump(data, file_json, indent=4)
    upload_s3(filename,'os-inspector-data', filename)     
    return jsonify({"status": "success"}), 200

@app.route('/health', methods=['GET'] )
def validate_health():
    return jsonify({"health": "ok"}), 200

def upload_s3(file, bucket, identifier):
    try:
        s3.upload_file(file, bucket, identifier)
        print("uploaded")
    except FileNotFoundError:
        print("file not found")
    except NoCredentialsError:
        print(" auth error")

if __name__ == '__main__':
    s3 = boto3.client('s3')
    app.run(host='0.0.0.0', port=5000)