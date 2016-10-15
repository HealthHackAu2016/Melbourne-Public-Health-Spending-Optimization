#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Test this with something like:
# curl -i -H "Content-Type: application/json" -X POST -d '{"compfood-min":"1", "compfood-max":"10"}' http://localhost:5000/api/v1.0/query

import flask
import sqlite3
import backend

app = flask.Flask(__name__)

@app.route('/api/v1.0/query', methods=['POST'])
def runQuery():
    # Abort if we didn't receive a JSON query
    if not flask.request.json:
        abort(400)

    # Map column/field full names to their short names used in the frontend
    fields = {  "Prophylactic zinc supplementation":         "zinc",
                "Vitamin A supplementation":                 "vitA",
                "Complementary feeding education":           "edu",
                "Public provision of complementary foods":   "compfood",
                "Breastfeeding provision":                   "bfpromo",
                "Balanced energy-provision supplementation": "beps",
                "Multiple micronutrient supplementation":    "micros"
                }

    # Begin constructing constraints
    interventionConstraints = {}
    for fullName, shortName in fields.iteritems():
      # For every field submitted, add the min and max values of that column to
      # the constraints IFF both min and max are non-NULL
      tmp_min = flask.request.json.get(shortName + "-min")
      tmp_max = flask.request.json.get(shortName + "-max")
      if(tmp_min and tmp_max):
        interventionConstraints[fullName] = {}
        interventionConstraints[fullName]['min'] = tmp_min
        interventionConstraints[fullName]['max'] = tmp_max

    # Make the query
    result = backend.getResult(interventionConstraints)
    # Format the result as a dictionary with short names readable by the
    # frontend
    output = {  'fval':     result[0],
                'zinc':     result[1],
                'vitA':     result[2],
                'edu':      result[3],
                'compfood': result[4],
                'bfpromo':  result[5],
                'beps':     result[6],
                'micros':   result[7]
                }

    # Send through the result
    return flask.jsonify({'result': output}), 200

if __name__ == '__main__':
    app.run(debug=True)
