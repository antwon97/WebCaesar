from flask import Flask, request
from caesar import rotate_string
app = Flask('app')

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form method="post">
        <label> Rotate by: </label>
        <input type="text" name="rot" placeholder="0"/>
        
        <textarea name="text">{0}</textarea>
        <input type="submit" value="Submit Query"/>
      </form>

    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
  
    tempTxt = request.form['text']

    tempNum = int(request.form['rot'])

    tempRot = rotate_string(tempTxt, tempNum)

    return form.format(tempRot)

@app.route("/")
def index():

    return form.format("")


app.run()