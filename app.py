from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid
from datetime import datetime

app = Flask(__name__)
CORS(app)

# In-memory storage (replace with DB later)
leads = []
partners = []
bids = []

@app.route('/')
def home():
    return {"status": "NestNudge API running"}

# ✅ SUBMIT LEAD
@app.route('/submit-lead', methods=['POST'])
def submit_lead():
    data = request.json

    lead = {
        "id": str(uuid.uuid4()),
        "name": data.get("name"),
        "email": data.get("email"),
        "phone": data.get("phone"),
        "address": data.get("address"),
        "projectType": data.get("projectType"),
        "timestamp": datetime.utcnow().isoformat()
    }

    leads.append(lead)

    return jsonify({"message": "Lead received", "lead": lead}), 200


# ✅ GET LEADS (for partners)
@app.route('/partners', methods=['GET'])
def get_leads():
    return jsonify(leads)


# ✅ PLACE BID
@app.route('/bids', methods=['POST'])
def place_bid():
    data = request.json

    bid = {
        "id": str(uuid.uuid4()),
        "lead_id": data.get("lead_id"),
        "partner_id": data.get("partner_id"),
        "amount": data.get("amount"),
        "timestamp": datetime.utcnow().isoformat()
    }

    bids.append(bid)

    return jsonify({"message": "Bid placed", "bid": bid})


# ✅ SIMPLE AUTH (placeholder)
@app.route('/auth', methods=['POST'])
def auth():
    data = request.json

    return jsonify({
        "message": "Authenticated",
        "user": {
            "email": data.get("email")
        }
    })


if __name__ == '__main__':
    app.run(debug=True)
