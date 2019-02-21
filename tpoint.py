from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/')
@app.route('/upload')
def upload_file():
    tData={"status":"Success"}
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
      
    return render_template('upload.html',tData=tData)
   #return render_template('upload.html',**tData)


"""	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
"""
		
if __name__ == '__main__':
   app.run(debug = True)