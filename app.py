from flask import Flask, flash, render_template, request, url_for, redirect
import os
import openai
import jinja2
from werkzeug.utils import secure_filename
import replicate
from chgen import ChineseGen
from Img import ImageModify

app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = 'static/upload/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.secret_key = 'Admin123!'
#os.environ["REPLICATE_API_TOKEN"] = 'YOUR_REPO_TOKEN'
#os.environ["API_TOKEN"] = 'YOUR_OPENA|_TOKEN'

chgen = ChineseGen()
imgm = ImageModify()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
        user_input = request.form["user_text_input"]
        openai.api_key = os.getenv("API_TOKEN")
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=user_input,
            max_tokens=2040,
            temperature=0
        )
        result = response.choices[0].text
        return render_template("index.html", ai_answer=result)
    return render_template('index.html')

@app.route('/imageGen', methods=['GET','POST'])
def getImage():
    if request.method == "POST":
        user_input = request.form["user_img_input"]
        openai.api_key = os.getenv("API_TOKEN")
        response = openai.Image.create(
            prompt=user_input,
            n=1,
            size="1024x1024"
        )
        result = response.data[0].url
        return render_template("image.html", ai_answer=result, requested="GeneratedImg")
    return render_template('image.html', ai_answer='False')

@app.route('/imageUp', methods=['GET','POST'])
def chgImage():
    if request.method == "POST":
        file = request.files["upfile"]
        if file.filename == '':
            flash('No image selected for uploading')
            return render_template('imgupload.html', ai_answer='False', user_image='False')
        replicate_token = os.getenv("REPLICATE_API_TOKEN")
        if not replicate_token:
            flash('No replication token defined')
            return render_template('imgupload.html', ai_answer='False', user_image='False')

        imgFidelity = float(request.form["imgFidelity"])
        imgScale = int(request.form["imgScale"])

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('Image successfully uploaded and displayed below')
            nfile = imgm.chgImg(os.path.join(app.config['UPLOAD_FOLDER'], filename), imgScale, imgFidelity)
            return render_template('imgupload.html', ai_answer=nfile, user_image=filename)
        else:
            flash('Allowed image types are -> png, jpg, jpeg, gif')
            return render_template('imgupload.html', ai_answer='False', user_image='False')

    return render_template('imgupload.html', ai_answer='False', user_image='False')

@app.route('/display/<filename>')
def display_image(filename):
    print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='upload/' + filename), code=301)

@app.route('/siGen', methods=['GET','POST'])
def getSiWen():
    methods = {
        1: "genSi",
        2: "genCouplet",
        3: "genSS",
        4: "genSiWithHead"
    }
    if request.method == "POST":
        user_input = request.form["user_input"]

        chLine = int(request.form["chLine"])
        chType = int(request.form["chType"])
        mname = methods[chType]
        func = getattr(chgen, mname)

        chWord = int(request.form["chWord"])
        results = func(user_input, chLine, chWord)
        result = '<br/>'.join(results)
        return render_template("chinese.html", ai_answer=result, requested="GeneratedSi")
    return render_template('chinese.html', ai_answer='False')

if __name__ == '__main__':
    app.run(debug=True, port=8080)