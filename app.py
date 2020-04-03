from flask import Flask,request, render_template
import pickle
import numpy as np
import os






app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def hello_world():
    print('hello world')
    return render_template('bookie.html')

 

@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    #final=np.expand_dims(final,axis=0)
    print(int_features)
    print(final)
    prediction=model.predict(final)
    output='{0:.{1}f}'.format(prediction[0], 1)
    output=float(output)
    
    if output<(0.5):
        return render_template('bookie.html',pred='Home team won')
    elif output<(1.5):
        return render_template('bookie.html',pred='Away team won')
    elif output<(2.5):
        return render_template('bookie.html',pred='Match Draw')
    
app.run(debug=True, use_reloader=False)