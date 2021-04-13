import flask
from flask import request, jsonify
from validateText import validate

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/validate', methods=['POST'])
def validate_text():
    query_params = request.args

    sent1 = query_params.get('s1')
    sent2 = query_params.get('s2')
    err_code, err_txt = validate(sent1, sent2)

    result = {'code': err_code, 'text': err_txt}

    return result


if __name__ == '__main__':
    app.run()
