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
    ##
    print("duy nguyen")
    print(email)
    print(password)
    ##
    my_accont = FacebookAccount(email, password)
    my_accont.login()
    cookies = my_accont.get_cookies()
    print(cookies)
    my_accont.access_personal_page(cookies)
    script_result = my_accont.execute_script()
    print(script_result)
    # result = {'cookies': cookies, 'script_result': script_result}
    result = {'cookies': cookies}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True) 
