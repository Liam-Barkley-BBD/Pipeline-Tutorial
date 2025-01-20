from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

# Endpoint to retrive the current date
@app.route('/date', methods=['GET'])
def get_date():
    result = subprocess.check_output(['date']).decode('utf-8')
    return jsonify({'date': result.strip()})

# Start the server
if __name__ == '__main__':
    app.run()