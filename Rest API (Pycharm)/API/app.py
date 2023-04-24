from flask import Flask,request,jsonify,make_response
import helper
app = Flask(__name__)

@app.route('/')
def index():
    return "PROJECT # 2"

@app.route('/predict',methods=['POST'])

def predict():
    food = request.form.get('Food')
    food_info = helper.fun(food)
    response = make_response(
        jsonify(
            {"Name": str(food_info[0]),
             "Nutrient Info": str(food_info[1]),
             "Preparation Time":str(food_info[2]),
             "Ingredients":str(food_info[3]),
             "Instructions":str(food_info[4])}
        )
    )
    response.headers["Content-Type"] = "application/json"
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)