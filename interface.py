from flask import Flask,render_template,request,jsonify
from utils import Titanic

tt=Titanic()

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('home.html')


# @app.route('/get_emabrked')
# def get_emabrked():
#     embarked =  tt.get_emabrked()  
#     return jsonify({"embarked":embarked})
    

# @app.route('/get_gender')
# def get_gender():
#     gender =  tt.get_gender()  
#     return jsonify({"gender":gender})
    

@app.route('/get_prediction', methods = ['POST','GET'])
def predict_death():
    if request.method == 'POST':
        user_data = request.form
        #Pclass,Gender,Age,SibSp,Parch,Fare,Embarked
        Pclass = eval(user_data['Pclass'])
        Gender=user_data['Gender']
        Age=eval(user_data['Age'])
        SibSp=eval(user_data['SibSp'])
        Parch=eval(user_data['Parch'])
        Fare=eval(user_data['Fare'])
        Embarked=user_data['Embarked']



        print("yes")
        prediction = tt.get_prediction(Pclass,Gender,Age,SibSp,Parch,Fare,Embarked)
        print("bye")
        #return jsonify({"Message": f"Predicted  {prediction} "})
        return render_template('home.html', prediction_text = prediction)
        
        # if prediction==0:

        #     render_template("homelive.html")
        # elif prediction==1:
        #     render_template("homedead.html")
        




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)   
