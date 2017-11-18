#!interpreter/bin/python
from flask import Flask, jsonify
from db_connection import DataConnection
import weanings as wn

api = Flask(__name__)
db = DataConnection()

@api.route('/api/weaning', methods=['PUT'])
def add_weaning(n_weaned, n_litters):
    grp = wn.WeaningGroup(n_litters, n_weaned)
    db.save_weaning(grp.num_litters,
                    grp.num_weaners,
                    grp.pigs_per_litter)

@api.route('/api/weanings', methods=['GET'])
def get_weanings():
    weanings = db.get_weanings()
    return jsonify({'weanings': weanings})



if __name__ == '__main__':
    api.run(debug=True)