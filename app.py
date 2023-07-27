from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)


@app.route('/success/<int:score>')
def success(score):
    # Determining the result based on average_marks
    result=""
    if score>=50:
        result="PASS"
    else:
        result='FAIL'
    my_dict={'score':score,'score_outcome':result}
    return render_template('outcome.html',results=my_dict)


@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method=='GET':
        return render_template('submit.html') # Renders an HTML form for input
    else:
        # Extracting the marks from the submitted form
        Maths=float(request.form['maths'])
        Science=float(request.form['science'])
        Statistics=float(request.form['statistics'])
        Data_science=float(request.form['datascience'])
        
        # Calculating the average marks
        average_score=(Science+Maths+Statistics+Data_science)/4

    # Redirecting to the appropriate route ("/success/<score>")
    return redirect(url_for('success',score=average_score))


if __name__=='__main__':
    app.run(debug=True)

