from logging import FileHandler,WARNING
from flask import Flask,render_template,request
app=Flask(__name__,template_folder="template")
import pickle
model=pickle.load(open(r'D:/ProjFlask/model.pkl','rb'))
@app.route('/')
def helloworld():
    return render_template("index.html")
@app.route('/login',methods=['POST'])
def login():
    a=request.form["sex"]
    b=request.form["status"]
    c=request.form["Education"]
    d=request.form["Type"]
    e=request.form["history"]
    f=request.form["housing"]
    g=request.form["Locality"]
    h=request.form["Dependents"]
    i=request.form["Income"]
    j=request.form["CoIncome"]
    k=request.form["Loan"]
    l=request.form["term"]
    if(a=="male"):
        a1=1
    if(a=="female"):
        a1=0
    if(b=="married"):
        b1=1
    if(b=="unmarried"):
        b1=0
    if(c=="educated"):
        c1=1
    if(c=="uneducated"):
        c1=0
    if(d=="salaried"):
        d1=1
    if(d=="self"):
        d1=0
    if(e=="yes"):
        e1=1
    if(e=="no"):
        e1=0
    if(f=="yes1"):
        f1=1
    if(f=="no1"):
        f1=0
    if(g=="in"):
        g1=1
    if(g=="out"):
        g1=2
    if(g=="inter"):
        g1=3
    t=[[int(a1),int(b1),int(c1),int(d1),int(e1),int(f1),int(g1),int(h),int(i),int(j),int(k),int(l)]]
    output=model.predict(t)
    print(output)
    return render_template("index.html",y="Chances of Fraud is "+str(output[0]))
if __name__ =='__main__':
    app.run(debug=True)