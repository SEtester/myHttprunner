from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

# 模拟一个数据库
books = [
    {
        "id": 1,
        "title": "Python编程：从入门到实践",
        "author": "Eric Matthes",
        "publication_date": "2016-11-01",
    },
    {
        "id": 2,
        "title": "流畅的Python",
        "author": "Luciano Ramalho",
        "publication_date": "2018-07-20",
    }
]

your_secret_token = "h7Gk4YJcV6"


def authenticate():
    """
    检查请求是否具有有效的身份验证
     cookie：token=h7Gk4YJcV6
     json: {"token": h7Gk4YJcV6"}
     headers: token: h7Gk4YJcV6
    """
    auth_cookie = request.cookies.get("token")
    body_token = None
    if request.method == "POST":
        if request.args.get("token"):
            body_token = request.args.get("token")
        elif request.json.get("token"):
            body_token = request.json.get("token")

    headers_token = request.headers.get("token")

    if auth_cookie == your_secret_token \
            or body_token == your_secret_token \
            or headers_token == your_secret_token:
        return True
    return False


# 获取所有书籍
@app.route('/api/books', methods=['GET'])
def get_books():
    if not authenticate():
        return jsonify(
            {
                "code": "401",
                "message": "请先登录"
            }
        ), 401
    return jsonify(
        {
            "code": "200",
            "message": "书籍查询成功",
            "result": books
        }
    )


# 获取单个书籍
@app.route('/api/books/<int:id>', methods=['GET'])
def get_book(id):
    if not authenticate():
        return jsonify(
            {
                "code": "401",
                "message": "请先登录"
            }
        ), 401
    book = next(filter(lambda x: x['id'] == id, books), None)
    if book:
        return jsonify(
            {
                "code": "200",
                "message": "书籍查询成功",
                "result": book
            }
        )
    return jsonify({
        "code": "404",
        "message": "未找到书籍"
    }), 404


# 新增书籍
@app.route('/api/books', methods=['POST'])
def add_book():
    if not authenticate():
        return jsonify(
            {
                "code": "401",
                "message": "请先登录"
            }
        ), 401
    book = {
        "id": max(b["id"] for b in books) + 1,
        "title": request.json["title"],
        "author": request.json["author"],
        "publication_date": request.json["publication_date"],
    }
    books.append(book)

    version = 1
    if "version" in request.json:
        version = request.json.pop("version")

    if version == 1:
        return jsonify(
            {
                "code": "200",
                "message": "保存成功",
                "result": book
            }
        ), 201
    elif version == 2:
        return jsonify(
            {
                "code": "200",
                "message": "保存成功"
            }
        ), 201
    elif version == 3:
        return jsonify(
            {
                "code": "200",
                "message": "保存成功",
                "result": {
                    "id": book["id"],
                    "title": book["title"]
                }
            }
        ), 201
    else:
        return jsonify(
            {
                "code": "200",
                "message": "保存成功",
                "result": book
            }
        ), 201


# 修改书籍
@app.route('/api/books/<int:id>', methods=['PUT'])
def update_book(id):
    if not authenticate():
        return jsonify(
            {
                "code": "401",
                "message": "请先登录"
            }
        ), 401
    book = next(filter(lambda x: x['id'] == id, books), None)

    version = 1
    if "version" in request.json:
        version = request.json.pop("version")

    if book:
        if version == 1:
            book.update(request.json)
            return jsonify(
                {
                    "code": "200",
                    "message": "更新成功",
                    "result": book
                }
            )
        elif version == 2:
            book.update(request.json)
            return jsonify(
                {
                    "code": "200",
                    "message": "更新成功",
                }
            )
        else:
            book.update(request.json)
            return jsonify(
                {
                    "code": "200",
                    "message": "更新成功",
                    "result": book
                }
            )

    return jsonify(
        {
            "code": "404",
            "message": "修改数据信息失败，未找到书籍"
        }
    ), 404


# 删除书籍
@app.route('/api/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    if not authenticate():
        return jsonify(
            {
                "code": "401",
                "message": "请先登录"
            }
        ), 401
    book = next(filter(lambda x: x['id'] == id, books), None)
    if book:
        books.remove(book)
        return jsonify(
            {
                "code": "200",
                "message": "书籍已删除"
            }
        )
    return jsonify(
        {
            "code": "404",
            "message": "删除失败，未找到书籍"
        }
    ), 404


# 登录
@app.route('/api/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    # 在这里添加实际的身份验证逻辑
    if username == "xiaoming" and password == "123456":
        json_data = jsonify(
            {
                "code": "200",
                "message": "登录成功",
                "token": your_secret_token
            }
        )
        resp = make_response(json_data)
        resp.set_cookie("token", your_secret_token)
        return resp
    return jsonify(
        {
            "code": "401",
            "message": "用户名或密码错误"
        }
    ), 401


if __name__ == '__main__':
    app.run(debug=True)
