from flask import Flask, render_template , request , redirect, url_for
import model
app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def home():
    if request.method == "POST":
        rds = request.form['rds']
        ads = request.form['ads']
        mks = request.form['mks']
        loc = request.form['loc']
        if loc == "NY":
            values = [[0,0,1,rds,ads,mks]]
        elif loc == "CL":
            values = [[1,0,0,rds,ads,mks]]
        else:
            values = [[0,1,0,rds,ads,mks]]
        result = model.run(values)
        
        return render_template("result.html", result = result)
    else:
        return render_template("home.html")

if __name__ == "__main__":
    app.run(debug = True)