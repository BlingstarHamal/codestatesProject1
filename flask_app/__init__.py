import pickle
import numpy as np
import math
from flask import Flask, render_template, redirect, request, url_for
from catboost import CatBoostClassifier, Pool

model=CatBoostClassifier()
model.load_model('cat_model')

def create_app():
    
    app = Flask(__name__)

    # from routes import customer_routes
    # app.register_blueprint(customer_routes.bp)

    @app.route('/', methods=['POST', 'GET'])
    def index():
        if request.method == 'POST':
            return redirect(url_for(''))
        return render_template('index.html')
    
    @app.route('/app', methods=['POST', 'GET'])
    def app_page():
        return render_template('app.html')
    
    @app.route('/result', methods=['POST'])
    def result():
        contents = '신용등급 예측 결과'
        val1 = request.form['gender'] 
        val2 = request.form['car'] 
        val3 = request.form['reality'] #
        val5 = int(request.form['income_total'])
        val6 = request.form['edu_type']
        val7 = request.form['family_type']
        val8 = request.form['house_type']
        val9 = request.form['occyp_type']
        val10 = request.form['EMPLOYED_group']
        val11 = int(request.form['begin_month'])
        val12 = int(request.form['child_num'])
        val13 = int(request.form['YEARS_BIRTH'])
        val14 = int(request.form['family_size'])
        val15 = request.form['income_type']
        val16= int(val5)/int(val14) #income_avg incomtotl= val 5 famliy size=val 14
        val4 = (math.trunc(val13)//10)*10 # Age_group
    
        #['gender', 'car', 'reality', 'child_num', 'income_total', 'income_type',
        #'edu_type', 'family_type', 'house_type', 'occyp_type', 'family_size',
        #'begin_month', 'YEARS_BIRTH', 'Age_group', 'EMPLOYED_group',
        #'income_avg']
        
        try:
            data = np.array([val1,val2,val3,int(val12),int(val5),val15,val6,val7,val8,
                            val9,val14,val11,val13,val4,val10,val16])
            
            y_pred = model.predict(data)[0]
            if y_pred == 0:
                return  render_template('result_0.html', title=contents, result=y_pred)
            elif y_pred == 1:
                return  render_template('result_1.html', title=contents, result=y_pred)
            elif y_pred == 2:
                return render_template('result_2.html', title=contents, result=y_pred)
        except: 
            y_pred = '작성되지 않은 내용이 있습니다. 다시 입력해주세요'        
            return render_template('result_0.html', title=contents, result=y_pred)
                    
    return app

if __name__=='__main__':
    app = create_app()
    app.run(debug=True);



