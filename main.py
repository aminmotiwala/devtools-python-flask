from flask import Flask, render_template, request, jsonify
from utilities import util

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

@app.route('/')
def loadHomePage():
    return render_template('index.html')

@app.route('/password-generator')
def loadPasswordGenerator():
    return render_template('password-generator.html', strong_password=util.generatePassword())

@app.route('/json-beautifier')
def loadJsonBeautifier():
    return render_template('json-beautifier.html')

@app.route('/base64-encoder')
def loadBase64Encoder():
    return render_template('/base64-encoder.html')

@app.route('/base64-decoder')
def loadBase64Decoder():
    return render_template('/base64-decoder.html')

@app.route('/beautify-json', methods=['POST'])
def beautify_json():
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Validate and beautify the JSON
        input_text = data.get('inputText', '')
        beautified_json, error_message = util.beautify(input_text)

        if error_message:
            return jsonify({'error': error_message}), 400
        else:
            return beautified_json

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run()

