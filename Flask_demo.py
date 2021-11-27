import json

from flask import Flask, jsonify

app = Flask(__name__)

books = [
    {"book_ID": "1", "book": "三国演义"},
    {"book_ID": "2", "book": "水浒传"},
    {"book_ID": "3", "book": "西游记"},
    {"book_ID": "4", "book": "红楼梦"},
]


@app.route('/')
def hello_world():
    return 'hello,aaaaaa'


@app.route('/book')
def book_list():
    json_book = json.dumps(books, ensure_ascii=False)
    print(json_book)
    return json_book


@app.route('/book/<string:bookid>')
def book(bookid):
    # 遍历books列表
    for book in books:
        if bookid == book["book_ID"]:
            return json.dumps(book, ensure_ascii=False)

    return f"ID为{bookid}的图书没有找到"


if __name__ == '__main__':
    app.run(debug=True)
