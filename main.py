from flask import Flask, request, jsonify

from facebook_acount import FacebookAccount

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "root"

@app.route('/', methods=['GET'])
def welcome():
    return "Welcome again"
@app.route('/fetch', methods=['POST'])
def fetch():
    email = request.form['email']
    password = request.form['password']

    my_accont = FacebookAccount(email, password)
    my_accont.login()
    cookies = my_accont.get_cookies()
    script_result = my_accont.execute_script()
    result = {'cookies': cookies, 'script_result': script_result}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True) 
