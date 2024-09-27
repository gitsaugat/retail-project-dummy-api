from flask import Flask, jsonify
import json
from flask_cors import CORS
from flask import Flask, url_for


app = Flask(__name__)
CORS(app)

# Load your JSON data

# finance section

@app.route('/financial/unbooked-transactions/', methods=['GET'])
def get_data():
    with open('jsons/finance/api-financial-unbooked-transactions.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/financial-overview-General-client-table/', methods=['GET'])
def get_client_Table():
    with open('jsons/finance/api-financial-overview-General-client-table.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/client/payment-tracking/', methods=['GET'])
def fetch_payment_tracking():
    with open('jsons/finance/api-client-payment-tracking.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/financial-overview-General/', methods=['GET'])
def fetch_general_details():
    with open('jsons/finance/api-financial-overview-General.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/financial-transaction-data-perclient/', methods=['GET'])
def fetch_financial_transaction_data_per_client():
    with open('jsons/finance/financial-transaction-data-per-client.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/transaction-bank-details-perclient/', methods=['GET'])
def fetch_transaction_bank_details_per_client():
    with open('jsons/finance/transaction-bank-details-per-client.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/transaction-invoice-detail-perclient/', methods=['GET'])
def fetch_transaction_invoice_detail_per_client():
    with open('jsons/finance/transaction-invoice-detail-perclient.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/api/bank-and-invoice-details-time-period', methods=['GET'])
def fetch_bank_and_invoice_details_perclient_timeperiod():
    with open('jsons/finance/financial-bank-and-invoice-data-perclient-time-period.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/api/paymenttracker-lastweek/', methods=['GET'])
def payment_tracking_weekly():
    with open('jsons/finance/payment-tracker-weekly.json') as f:
        data = json.load(f)
    return jsonify(data)

#labels section



@app.route('/api/list-all-labels-grouped-by-type/', methods=['GET'])
def list_labels_by_group():
    with open('jsons/labels/get_labels_grouped_by_type.json') as f:
        data = json.load(f)
    return jsonify(data)



@app.route("/api/Create-New-label-for-type/", methods=['POST'])
def create_labels():
    
    return jsonify({'success':True,'message':'Label Created'})

@app.route('/api/Edit-Label-name-for-type/', methods=['PUT'])
def update_labels():
    return jsonify({'success':True,'message':'Label Updated'})


@app.route('/api/Delete-label-for-type/', methods=['DELETE'])
def delete_labels():
    return jsonify({'success':True,'message':'Label Deleted'})

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


@app.route("/site-map")
def site_map():
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))

    return jsonify(links)

if __name__ == '__main__':
    app.run(debug=True , port=5500)
