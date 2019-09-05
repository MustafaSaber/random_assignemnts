from TextBlob.text_blob import TutorialTextBlob
from flask import Flask, render_template, request, jsonify, Response
import json
import urllib

app = Flask(__name__, template_folder="templates")
app.config['JSON_AS_ASCII'] = False


# @app.route("/")
# def home():
#     return render_template("home.html")


@app.route("/answer", methods=['POST'])
def preprocess():
    # print(urllib.parse.unquote_plus(request.get_data().decode('utf-8')))
    textobject = TutorialTextBlob(urllib.parse.unquote_plus(request.get_data().decode('utf-8')))
    # print(str(request.get_data()))
    list_of_all = [list(textobject.lemmatize()), str(textobject.text_correction()), list(textobject.part_of_speech)]
    json = jsonify(list_of_all)
    # render_template("ans.html", ans=json)
    return json


if __name__ == "__main__":
    app.run(debug=True)

