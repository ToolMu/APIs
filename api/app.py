from flask import Flask
from flask import jsonify

from processors.httporg.builder import HttporgBuilder
from processors.httporg.requester import HttporgRequester
from processors.httporg.responder import HttporgResponder
from processors.request_processor import RequestProcessor

from parsers.yaml_parsers import YamlParsers
from utils.constant import BASEDIR


app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"code": 200, "data": "OK index"})


@app.route('/list_app')
def list_app():
    return jsonify({"code": 200, "apps": [{"name": 'httpbin'}]})


@app.route('/<app_name>')
def app_api_doc(app_name):
    """
    提供应用相关信息
    """
    return jsonify({"code": 200, "data": app_name})


@app.route('/<app_name>/<mark>')
def app_func(app_name, mark):
    file_path = BASEDIR + '/conf/httporg.yaml'
    read_data = YamlParsers().parser(file_path)

    rp = RequestProcessor(HttporgBuilder(), HttporgRequester(), HttporgResponder())

    way = read_data[mark]
    res = rp(**way)
    return jsonify(res.json())


if __name__ == "__main__":
    app.run(debug=True)
