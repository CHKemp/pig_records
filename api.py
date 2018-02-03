#!interpreter/bin/python
import dateutil.parser
from flask import Flask, jsonify, request, abort
from datetime import date

from db_connection import DataConnection
import weanings as wn

api = Flask(__name__)
db = DataConnection()

def parse_date(datestring):
    dt = dateutil.parser.parse(datestring).date()
    return dt

def jsoinfy_group(grp):
    """returns a jsonified version of a weaning group."""
    return jsonify(wean_date=grp.wean_date,
                   litters=grp.litters,
                   weaners=grp.weaners)


@api.route('/api/weanings', methods=['POST'])
def add_weaning():
    if not request.json or not 'date' in request.json:
        abort(400)
    dt = parse_date(request.json['date'])
    grp = wn.WeaningGroup(dt)
    grp.litters = request.json['litters']
    grp.weaners = request.json['weaners']

    db.save_weaning(grp.wean_date,
                    grp.litters,
                    grp.weaners)
    return jsoinfy_group(grp), 201


# @api.route('/api/weanings/<date:wean_date', methods=['GET'])
# def change_weaning(wean_date):
#     weaning = db.get_weaning(wean_date)




@api.route('/api/weanings', methods=['GET'])
def get_weanings():
    weanings = db.get_weanings()
    return jsonify({'weanings': weanings})

if __name__ == '__main__':
    api.run(debug=True)