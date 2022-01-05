from flask import Flask, render_template, request, url_for
import pickle
import sklearn.ensemble

app = Flask(__name__)

''' Here is the function used to get the values and
    predict the corresponding label using our model in a pickle file'''
def Predictor(predict_list):
    pred = [predict_list] # the predict function of our model requires an array of arrays
    pickle_model = pickle.load(open("rand_for.pkl","rb"))
    result = pickle_model.predict(pred)
    return result[0]

@app.route("/", methods=('GET', 'POST'))
def index():
    return render_template('index.html')

@app.route("/avila_bible", methods=('GET', 'POST'))
def show_bible():
    if request.method == 'POST':
        row = int(request.form["row"]) - 1
        if row > 10430: # since the dataset is in two parts we need to check between two files, and the first file have 10430 rows
            row -= 10430
            with open("../avila-ts.txt", 'r') as fs:
                row_value = fs.readlines()[row]
                return render_template("show_bible.html", row_value=row_value)
        else:
            with open("../avila-tr.txt", 'r') as fr:
                row_value = fr.readlines()[row]
                return render_template("show_bible.html", row_value=row_value)
    return render_template("show_bible.html")

@app.route("/predictions", methods=('GET', 'POST'))
def predict():
    if request.method == 'POST':
        predict_list = request.form.to_dict()
        predict_list = list(predict_list.values())
        predict_list = list(map(float, predict_list))
        result = Predictor(predict_list)
        prediction = str(result)
        return render_template("predict.html",prediction=prediction)
    return render_template('predict.html')