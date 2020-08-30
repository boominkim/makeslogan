from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

app = Flask(__name__)

client = MongoClient('13.124.213.185', username='univ', password='univ')
db = client.dbuniv

# universities = [{"univnum": 1, "areanum": 1, "area": "서울", "korname": "서울대학교", "engname": "SEOUL NATIONAL UNIVERSITY",
#                  "imgurl": "https://univslogan.s3.ap-northeast-2.amazonaws.com/univimg/SNU.png"},
#                 {"univnum": 2, "areanum": 1, "area": "서울", "korname": "연세대학교", "engname": "YONSEI UNIVERSITY",
#                  "imgurl": "https://univslogan.s3.ap-northeast-2.amazonaws.com/univimg/YU.png"},
#                 {"univnum": 3, "areanum": 1, "area": "서울", "korname": "고려대학교", "engname": "KOREA UNIVERSITY",
#                  "imgurl": "https://univslogan.s3.ap-northeast-2.amazonaws.com/univimg/KU.png"},
#                 {"univnum": 4, "areanum": 1, "area": "서울", "korname": "서강대학교", "engname": "SOGANG UNIVERSITY",
#                  "imgurl": "https://univslogan.s3.ap-northeast-2.amazonaws.com/univimg/IHS.png"},
#                 {"univnum": 5, "areanum": 1, "area": "서울", "korname": "성균관대학교", "engname": "SUNGKYUNKWAN UNIVERSITY",
#                  "imgurl": "https://univslogan.s3.ap-northeast-2.amazonaws.com/univimg/SKKU.png"},
#                 {"univnum": 6, "areanum": 1, "area": "서울", "korname": "한양대학교", "engname": "HANYANG UNIVERSITY",
#                  "imgurl": "https://univslogan.s3.ap-northeast-2.amazonaws.com/univimg/HU.png"},
#                 {"univnum": 7, "areanum": 1, "area": "서울", "korname": "이화여자대학교", "engname": "EWHA WOMANS UNIVERSITY",
#                  "imgurl": "https://univslogan.s3.ap-northeast-2.amazonaws.com/univimg/EWU.png"}]

# db.univ_info.update_one({'korname': '성균관대학교'},
                        # {'$set': {'imgurl': 'https://univslogan.s3.ap-northeast-2.amazonaws.com/univimg/SKKU.png'}})

# db.univ_info.insert_many(universities)
# db.univ_info.delete_many({})
# return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})

#
# db.univ_info.update_one({'korname': '한양대학교'},
#                         {'$set': {'imgurl': 'https://www.hanyang.ac.kr/html-repositories/images/custom/introduction/img_hy0104_02_0102.png'}})
