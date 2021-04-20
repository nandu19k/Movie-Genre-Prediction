# Importing essential libraries
from flask import Flask, render_template, request
import pickle

# Load the models
classifier = pickle.load(open('model.pkl', 'rb'))
cv = pickle.load(open('cv.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
    	message = request.form['message']
    	data = [message]
    	vector = cv.transform(data).toarray()
    	my_prediction = classifier.predict(vector)
    	return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
	app.run(debug=True)
