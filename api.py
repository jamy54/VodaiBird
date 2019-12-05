import flask
from flask_cors import CORS
import json
from flask import request
import datetime
import operator
import os


app = flask.Flask(__name__)
app.config["DEBUG"] = True

CORS(app)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/getscore', methods=['GET'])
def getscore():
    datastore = []
    if not os.path.isfile('data.json'):
        file = open("data.json", "w") 
        file.write("[]") 
        file.close() 
    with open('data.json', 'r') as f:
        datastore = json.load(f)
    return json.dumps(datastore,sort_keys=True)
    #return '[{"name": "bc", "score": 200, "time": "1 jan 2016"},{"name": "jamy", "score": 20, "time": "1 jan 2016"},{"name": "sadun", "score": 10, "time": "1 jan 2016"},{"name": "dipu", "score": 50, "time": "1 jan 2016"}]'
    #return '{"results":[{"gender":"male","name":{"title":"Mr","first":"Mahdi","last":"Koole"},"location":{"street":{"number":6676,"name":"Kruisallee"},"city":"Achtmaal","state":"Drenthe","country":"Netherlands","postcode":15478,"coordinates":{"latitude":"41.6786","longitude":"-136.8800"},"timezone":{"offset":"-10:00","description":"Hawaii"}},"email":"mahdi.koole@example.com","login":{"uuid":"961af010-47df-46d7-bbe9-ebcb5f7b5873","username":"whitemeercat888","password":"punisher","salt":"rBZ9y2ED","md5":"efba5f4c63a1abbe6c73dbae8ba24ea1","sha1":"8f3841040d390302ac13a18bd5fd8cf180a2a1ef","sha256":"07a91eedf35bf2bd75d3718bededef1d3c4459b95f2d90e7217e1a67faa67945"},"dob":{"date":"1981-11-08T23:23:19.113Z","age":38},"registered":{"date":"2015-05-29T09:28:42.626Z","age":4},"phone":"(394)-735-4291","cell":"(994)-708-6753","id":{"name":"BSN","value":"17177465"},"picture":{"large":"https://randomuser.me/api/portraits/men/72.jpg","medium":"https://randomuser.me/api/portraits/med/men/72.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/72.jpg"},"nat":"NL"},{"gender":"female","name":{"title":"Mrs","first":"Karlisa","last":"Almeida"},"location":{"street":{"number":4356,"name":"Rua São Paulo "},"city":"Presidente Prudente","state":"Pará","country":"Brazil","postcode":39592,"coordinates":{"latitude":"72.2073","longitude":"-134.0720"},"timezone":{"offset":"+10:00","description":"Eastern Australia, Guam, Vladivostok"}},"email":"karlisa.almeida@example.com","login":{"uuid":"ff6c0dbc-951b-42cc-b990-f805e6cb9576","username":"smallgorilla501","password":"krystal","salt":"EyDfDsiB","md5":"d90b375c20765f008c9f31254845d3b5","sha1":"f8321570d64ded9cb02d1ec2810bb3fa6191613e","sha256":"9a496203a00837362e070b1fcfee98d5b5fd2dccc0081e55b14ce4d05b1a5259"},"dob":{"date":"1973-05-14T09:14:30.368Z","age":46},"registered":{"date":"2011-06-04T01:56:54.936Z","age":8},"phone":"(16) 5566-9026","cell":"(67) 4833-2462","id":{"name":"","value":null},"picture":{"large":"https://randomuser.me/api/portraits/women/82.jpg","medium":"https://randomuser.me/api/portraits/med/women/82.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/women/82.jpg"},"nat":"BR"},{"gender":"male","name":{"title":"Monsieur","first":"Naim","last":"Blanc"},"location":{"street":{"number":4432,"name":"Rue du Moulin"},"city":"Zäziwil","state":"Vaud","country":"Switzerland","postcode":8324,"coordinates":{"latitude":"-5.2425","longitude":"-145.9779"},"timezone":{"offset":"+6:00","description":"Almaty, Dhaka, Colombo"}},"email":"naim.blanc@example.com","login":{"uuid":"74278c67-88d2-4b89-aaf0-3b9b7d554693","username":"sadbird422","password":"undertak","salt":"bqhW3N8v","md5":"bcdfacb699d9bbc6c3b598509c9aeafc","sha1":"bb456eed001986aa3ebddd2c914fdcceb84b3706","sha256":"dda3c2d0f0ffef9e41d5a53eee52859352b846228ae9e0b55a7c2e9fbfc0dc9a"},"dob":{"date":"1998-06-11T00:47:09.979Z","age":21},"registered":{"date":"2004-02-14T11:33:18.949Z","age":15},"phone":"076 521 41 98","cell":"076 240 87 79","id":{"name":"AVS","value":"756.5978.7356.99"},"picture":{"large":"https://randomuser.me/api/portraits/men/58.jpg","medium":"https://randomuser.me/api/portraits/med/men/58.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/58.jpg"},"nat":"CH"},{"gender":"male","name":{"title":"Mr","first":"Onur","last":"Bademci"},"location":{"street":{"number":1204,"name":"Tunalı Hilmi Cd"},"city":"Ardahan","state":"Denizli","country":"Turkey","postcode":73134,"coordinates":{"latitude":"-57.7495","longitude":"-103.5949"},"timezone":{"offset":"+2:00","description":"Kaliningrad, South Africa"}},"email":"onur.bademci@example.com","login":{"uuid":"b1c7dfef-041c-4eaf-9eb1-5f19d483261e","username":"greenbear629","password":"baddog","salt":"CEKaB5YY","md5":"b342a2944fb4f7b0677ca7941feb7f83","sha1":"00cef228e308e0fc7013faed929264a826730eb6","sha256":"abcd5967bf2bf7b19e14a5065853137cb031c49cd2d75803dba06b41267172cb"},"dob":{"date":"1957-06-28T00:51:01.347Z","age":62},"registered":{"date":"2004-12-12T08:08:10.588Z","age":15},"phone":"(261)-716-6359","cell":"(581)-677-7050","id":{"name":"","value":null},"picture":{"large":"https://randomuser.me/api/portraits/men/7.jpg","medium":"https://randomuser.me/api/portraits/med/men/7.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/7.jpg"},"nat":"TR"},{"gender":"male","name":{"title":"Mr","first":"Edward","last":"Zhang"},"location":{"street":{"number":7646,"name":"Clyde Street"},"city":"Greymouth","state":"Southland","country":"New Zealand","postcode":41627,"coordinates":{"latitude":"68.3547","longitude":"-47.8285"},"timezone":{"offset":"+4:30","description":"Kabul"}},"email":"edward.zhang@example.com","login":{"uuid":"360dbcf9-ebdc-448b-bfe5-d281ae3b7790","username":"redbird815","password":"qwaszx","salt":"YenITQKB","md5":"434de18a1801bee8d000c34545627c70","sha1":"9470e45ae09e880d5278865e35d193bbdd744a60","sha256":"0fb8aab229a552db6b893952d98be554808ea4e788d59938cb21617d043a0ddf"},"dob":{"date":"1967-12-11T05:58:27.435Z","age":52},"registered":{"date":"2002-08-14T20:41:37.768Z","age":17},"phone":"(863)-386-9504","cell":"(516)-664-6023","id":{"name":"","value":null},"picture":{"large":"https://randomuser.me/api/portraits/men/12.jpg","medium":"https://randomuser.me/api/portraits/med/men/12.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/12.jpg"},"nat":"NZ"},{"gender":"male","name":{"title":"Mr","first":"Jared","last":"Jennings"},"location":{"street":{"number":2536,"name":"Park Lane"},"city":"Monaghan","state":"Leitrim","country":"Ireland","postcode":66861,"coordinates":{"latitude":"-10.4458","longitude":"147.9632"},"timezone":{"offset":"+9:00","description":"Tokyo, Seoul, Osaka, Sapporo, Yakutsk"}},"email":"jared.jennings@example.com","login":{"uuid":"dc150932-1492-4c2a-948f-9d2bcbb081d2","username":"ticklishgoose751","password":"starcraf","salt":"LcZg5wuy","md5":"cafbb29064f5e77a0544cd9fd5a33e23","sha1":"84b2ecd5eb836dbb88c7099387e717514bf8affb","sha256":"3dea7dc64e55040e244164c122d4ed21ed5dcc954f9e07b96b33d4897cbb78c8"},"dob":{"date":"1986-08-08T11:25:07.585Z","age":33},"registered":{"date":"2010-12-31T19:39:03.699Z","age":9},"phone":"021-317-8977","cell":"081-702-1557","id":{"name":"PPS","value":"8706717T"},"picture":{"large":"https://randomuser.me/api/portraits/men/76.jpg","medium":"https://randomuser.me/api/portraits/med/men/76.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/76.jpg"},"nat":"IE"},{"gender":"male","name":{"title":"Mr","first":"Evangelista","last":"Gonçalves"},"location":{"street":{"number":1808,"name":"Rua Piauí "},"city":"Mauá","state":"Distrito Federal","country":"Brazil","postcode":79543,"coordinates":{"latitude":"-37.5305","longitude":"177.3614"},"timezone":{"offset":"+1:00","description":"Brussels, Copenhagen, Madrid, Paris"}},"email":"evangelista.goncalves@example.com","login":{"uuid":"ac23a5d1-38ba-497b-a0c6-02da55dae806","username":"yellowostrich273","password":"sydney","salt":"jYgEfa1R","md5":"e9b86377c18efff3dc3fd5a736a3ea72","sha1":"9765a299e982eb8af5907cf4e58cb189c17434fa","sha256":"ef6553b7f155060fb595617f7f74db51e82041dd402ebd80fe4e4853ad930e72"},"dob":{"date":"1991-04-17T19:56:34.073Z","age":28},"registered":{"date":"2014-10-17T21:12:52.495Z","age":5},"phone":"(06) 4508-3972","cell":"(95) 3376-1269","id":{"name":"","value":null},"picture":{"large":"https://randomuser.me/api/portraits/men/50.jpg","medium":"https://randomuser.me/api/portraits/med/men/50.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/50.jpg"},"nat":"BR"},{"gender":"male","name":{"title":"Mr","first":"Joshua","last":"Kleine"},"location":{"street":{"number":6694,"name":"Poststraße"},"city":"Ganderkesee","state":"Bayern","country":"Germany","postcode":17289,"coordinates":{"latitude":"9.5502","longitude":"-119.0228"},"timezone":{"offset":"+7:00","description":"Bangkok, Hanoi, Jakarta"}},"email":"joshua.kleine@example.com","login":{"uuid":"99a79135-9577-4e49-a8a9-0d1e556dd5bc","username":"organicduck682","password":"tophat","salt":"w49sv1BD","md5":"4349da8208d928b0c64f6d1c463fd7e2","sha1":"38f6dc8c93fd13a6b9d84be6e73748494803b1a9","sha256":"39699f32a5ed4d56ebe20688e2340eb72008b45e6410d4e6bba28eaf5c017b78"},"dob":{"date":"1967-01-11T02:31:22.931Z","age":52},"registered":{"date":"2018-11-28T22:20:10.878Z","age":1},"phone":"0635-3931403","cell":"0179-3048550","id":{"name":"","value":null},"picture":{"large":"https://randomuser.me/api/portraits/men/30.jpg","medium":"https://randomuser.me/api/portraits/med/men/30.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/30.jpg"},"nat":"DE"},{"gender":"female","name":{"title":"Mrs","first":"Ariane","last":"Chu"},"location":{"street":{"number":5700,"name":"Lake of Bays Road"},"city":"Armstrong","state":"Nova Scotia","country":"Canada","postcode":"B9T 3L3","coordinates":{"latitude":"0.2460","longitude":"94.9404"},"timezone":{"offset":"+11:00","description":"Magadan, Solomon Islands, New Caledonia"}},"email":"ariane.chu@example.com","login":{"uuid":"461bdecb-b042-489c-9c0a-b2b145772883","username":"beautifulbutterfly457","password":"102030","salt":"aWHHr961","md5":"b23c34bed3fdea80931f5785d1e54547","sha1":"c6fc147b4de09744023b3f5990e9226876b7e8b9","sha256":"c9525f64089e191f198ce3e1ae92b39cebb759735cf87d6b1d631007737e634f"},"dob":{"date":"1984-08-02T14:46:10.656Z","age":35},"registered":{"date":"2017-01-25T06:42:45.861Z","age":2},"phone":"864-507-5134","cell":"922-087-4283","id":{"name":"","value":null},"picture":{"large":"https://randomuser.me/api/portraits/women/14.jpg","medium":"https://randomuser.me/api/portraits/med/women/14.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/women/14.jpg"},"nat":"CA"},{"gender":"female","name":{"title":"Ms","first":"Caroline","last":"Hansen"},"location":{"street":{"number":5867,"name":"Åbakken"},"city":"Stokkemarke","state":"Danmark","country":"Denmark","postcode":55827,"coordinates":{"latitude":"49.0878","longitude":"-125.0186"},"timezone":{"offset":"-12:00","description":"Eniwetok, Kwajalein"}},"email":"caroline.hansen@example.com","login":{"uuid":"d1710dbe-fa3d-4b81-9691-d6ec3f855ba2","username":"crazymeercat489","password":"redleg","salt":"RrU1z6wQ","md5":"6b535c704bf21a8f0dd39c51382ec686","sha1":"8d5676c09721cbb8a33bd4ad30888b7ff369d306","sha256":"780234d3e257698369de8c1cd156b238a44a017f6167d500635411ba5ac490b4"},"dob":{"date":"1969-02-12T21:57:06.217Z","age":50},"registered":{"date":"2002-08-10T23:47:31.657Z","age":17},"phone":"78343302","cell":"82984240","id":{"name":"CPR","value":"120269-6935"},"picture":{"large":"https://randomuser.me/api/portraits/women/38.jpg","medium":"https://randomuser.me/api/portraits/med/women/38.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/women/38.jpg"},"nat":"DK"}],"info":{"seed":"0c7fcf144207cbc1","results":10,"page":1,"version":"1.3"}}'


@app.route('/savescore', methods=['GET','POST'])
def savescore():
    datastore = []
    today = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    modified = False
    name = request.args['name']
    score = request.args['score']
    if not os.path.isfile('data.json'):
        file = open("data.json", "w") 
        file.write("[]") 
        file.close() 
    with open('data.json', 'r') as f:
        datastore = json.load(f)
    for d in datastore:
        if(d['name'] == name):
            if (d['score'] < score):
                d['score'] = score
                d['time'] = str(today)
            modified = True
    
    temp = {"name": name, "score": score, "time": str(today)}
    if not modified:
        datastore.append(temp)
    
    #datastore.sort(key=operator.itemgetter('score'))
    datastore = sorted(datastore, key = lambda i: int(i['score']))

    with open('data.json', 'w') as f:
        json.dump(datastore, f)
        
    return name

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))