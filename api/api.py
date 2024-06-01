from flask import Flask, request, jsonify
import json
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
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)