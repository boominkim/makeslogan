from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
from bson.objectid import ObjectId

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

app = Flask(__name__)

client = MongoClient('13.124.213.185', username='univ', password='univ')
db = client.dbuniv


@app.route('/')
def home():
    univlist = list(db.univ_info.find({}, {"korname": 1, "_id": 0}))
    return render_template('index.html', data=univlist)


# maker페이지 Preview로 데이터 보내는 API
@app.route('/maker', methods=['GET'])
def maker():
    id = request.args.get('id')
    userinfos = list(db.userinfo.find({"_id": ObjectId(id)},
                                      {"name": 1, "univ": 1, "major": 1, "year": 1, "univeng": 1, "imgurl": 1}))
    return render_template('maker.html', data=userinfos[0])


# 유저가 입력한 정보를 db에 저장하고, maker로 보내는 API
@app.route('/maker', methods=['POST'])
def save_userinfo():
    univ_receive = request.form['univ_give']
    name_receive = request.form['name_give']
    major_receive = request.form['major_give']
    year_receive = request.form['year_give']

    univinfo = db.univ_info.find_one({"korname": univ_receive}, {'_id': 0})
    univ_engname = univinfo["engname"]
    univ_imgurl = univinfo["imgurl"]

    user = {
        'name': name_receive,
        'univ': univ_receive,
        'univeng': univ_engname,
        'imgurl': univ_imgurl,
        'major': major_receive,
        'year': year_receive,
    }
    result = db.userinfo.insert_one(user)
    userid = str(result.inserted_id)

    return jsonify({'result': 'success', '_id': userid})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
