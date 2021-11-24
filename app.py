from flask import Flask, render_template, request
from blockchain.scripts.deploy_lottery import deploy_lottery, start_lottery, enter_lottery, end_lottery

app = Flask(__name__)

@app.route('/user', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        account = request.form.get('account')
        usdEntryFee = request.form.get('usdEntryFee')
        print(account)
        #deploy_lottery()
        #enter_lottery(account=account, value=usdEntryFee)

    return render_template('index.html') 

@app.route('/admin', methods=['POST', 'GET'])
def admin_start():
    if request.method == 'POST':
        #deploy_lottery()
        #start_lottery()
        pass

    return render_template('admin.html')

@app.route('/admin', methods=['POST', 'GET'])
def admin_end():
    if request.method == 'POST':
        #deploy_lottery()
        #winner = end_lottery()
        #return render_template('admin.html', winner=winner)
        pass

    return render_template('admin.html')

if __name__ == '__app__':
    app.run(debug=True)
