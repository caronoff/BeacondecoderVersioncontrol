from flask import Flask, jsonify,request, render_template, Markup


app = Flask(__name__)



@app.route('/validatehex', methods=['GET','POST'])
def validatehex():
    ret_data =  str(request.args.get('hexcode'))
    if ret_data == 'craig':
        statuscheck='valid'
    else:
        statuscheck='not valid'
    return jsonify(echostatus=statuscheck)

@app.route('/output', methods=['GET','POST'])
def output():
    ## output will only process if hexcode has been validated.
    outputdata= str(request.args.get('hexcode'))
    username=str(request.args.get('name'))
    return render_template('output.html',hexcode=outputdata, username="test")

@app.route("/")
@app.route("/index")
def index():
    user ={'nickname': 'Craig Aronoff3'}  # fake user
    return render_template('child.html',title='Home',user=user)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5555)
