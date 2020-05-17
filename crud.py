import copy
import json
import os
from sqlalchemy import column

from flask import Flask, request, jsonify, abort
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from models.goods import Goods

with open('secret.json') as f:
    SECRET = json.load(f)

SQLALCHEMY_TRACK_MODIFICATIONS = False
DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class SmartGood(Goods, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kind_of_product = db.Column(db.String(32), unique=False)
    price_in_uah = db.Column(db.Integer, unique=False)
    country_of_producing = db.Column(db.String(32), unique=False)
    min_age_for_using = db.Column(db.Integer(), unique=False)

    def __init__(self, kind_of_product, price_in_uah, country_of_producing, min_age_for_using):
        super().__init__(kind_of_product, price_in_uah, country_of_producing, min_age_for_using)


class SmartGoodSchema(ma.Schema):
    class Meta:
        fields = ('kind_of_product', 'price_in_uah',
                  'country_of_producing', 'min_age_for_using')


smart_good_schema = SmartGoodSchema()
smart_goods_schema = SmartGoodSchema(many=True)


@app.route("/smart_good", methods=["POST"])
def add_smart_good():
    smart_good = SmartGood(
                                                  request.json['kind_of_product'],
                                                  request.json['price_in_uah'],
                                                  request.json['country_of_producing'],
                                                  request.json['min_age_for_using'])

    db.session.add(smart_good)
    db.session.commit()
    return smart_good_schema.jsonify(smart_good)


@app.route("/smart_good", methods=["GET"])
def get_smart_good():
    all_smart_good = SmartGood.query.all()
    result = smart_goods_schema.dump(all_smart_good)
    return jsonify({'smart_good': result})


@app.route("/smart_good/<id>", methods=["GET"])
def smart_good_detail(id):
    smart_good = SmartGood.query.get(id)
    if not smart_good:
        abort(404)
    return smart_good_schema.jsonify(smart_good)


@app.route("/smart_good/<id>", methods=["PUT"])
def smart_good_update(id):
    smart_good = SmartGood.query.get(id)
    if not smart_good:
        abort(404)
    old_smart_good = copy.deepcopy(smart_good)
    smart_good.kind_of_product = request.json['kind_of_product']
    smart_good.price_in_uah = request.json['price_in_uah']
    smart_good.country_of_producing = request.json['country_of_producing']
    smart_good.min_age_for_using = request.json['min_age_for_using']
    db.session.commit()
    return smart_good_schema.jsonify(old_smart_good)


@app.route("/smart_good/<id>", methods=["DELETE"])
def smart_good_delete(id):
    smart_good = SmartGood.query.get(id)
    if not smart_good:
        abort(404)
    db.session.delete(smart_good)
    db.session.commit()
    return smart_good_schema.jsonify(smart_good)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, host='127.0.0.1')