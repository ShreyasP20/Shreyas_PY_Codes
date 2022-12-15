from flask import Flask, request, abort

app=Flask(__name__)

@app.route('/main',methods=['POST'])
def main():
    if request.method=='POST':
        print(request.json)
        return 'success',200
    else:
        abort(400)
    
if __name__=='__main__':
    app.run()