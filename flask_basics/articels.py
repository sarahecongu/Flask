from flask import Flask,jsonify


app = Flask(__name__)
@app.route("/")
def Article_World ():
    return "<p>hello sarah</p>"


    
@app.route("/my_articles")
def get_articles():
    my_articles= [{
        "Article_id":9,
        "Article_title":"Africa's Presidents",
        "Article message":"The presidents of Africa such as Uhuru Kenyata,jomo Kenyatta,donot wish to retire early,why?",
        "Article_author":"Tracy M"

    },
    {
        "Article_id":10,
        "Article_title":"Color World",
        "Article_message":"The are different types of colors and all these colors have diferent uses,findoutr more thank you",
        "Article_author":"Sarah O.K"


    }
    

    ]
    return jsonify(my_articles)

if __name__ == '__name__':
    app.run(debug=True)