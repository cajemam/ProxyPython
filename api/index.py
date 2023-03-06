from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/')
def proxy():
  url = request.headers.get('url')
  if (url is None):
    return ('No URL specified in headers', 400)
  try:
    data = request.get_data()
    headers = {
      'Content-type': request.headers.get('Content-Type'),
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Headers': '*',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    }
    response = request.post(url, data=data, headers=headers)
    return (response.content, response.status_code, headers)
  except requests.exceptions.RequestException as e:
    return str(e), 500