from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid
from datetime import datetime

app = Flask(__name__)
CORS(app)

# ===============================
# IN-MEMORY STORAGE (TEMP DB)
# ===============================
leads = []
bids = []

# ===============================
# ROOT ROUTE (FIXES NOT FOUND)
# ===============================
@app.route('/')
def home():
    return {"status": "NestNudge API running"}

# ===============================
# SUBMIT LEAD
# ===============================
@app.route('/submit-lead', methods=['POST'])
def submit_lead():
    try:
        data = request.json

        if not data:
            return jsonify({"error": "No data received"}), 400

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

        print("✅ Lead received:", lead)

        return jsonify({
            "message": "Lead received",
            "lead": lead
        }), 200

    except Exception as e:
        print("❌ Error submitting lead:", str(e))
        return jsonify({"error": "Server error"}), 500


# ===============================
# GET LEADS (PARTNERS VIEW)
# ===============================
@app.route('/partners', methods=['GET'])
def get_leads():
    return jsonify(leads), 200


# ===============================
# PLACE BID
# ===============================
@app.route('/bids', methods=['POST'])
def place_bid():
    try:
        data = request.json

        bid = {
            "id": str(uuid.uuid4()),
            "lead_id": data.get("lead_id"),
            "partner_id": data.get("partner_id"),
            "amount": data.get("amount"),
            "timestamp": datetime.utcnow().isoformat()
        }

        bids.append(bid)

        print("💰 Bid placed:", bid)

        return jsonify({
            "message": "Bid placed",
            "bid": bid
        }), 200

    except Exception as e:
        print("❌ Error placing bid:", str(e))
        return jsonify({"error": "Server error"}), 500


# ===============================
# SIMPLE AUTH (PLACEHOLDER)
# ===============================
@app.route('/auth', methods=['POST'])
def auth():
    try:
        data = request.json

        return jsonify({
            "message": "Authenticated",
            "user": {
                "email": data.get("email")
            }
        }), 200

    except Exception as e:
        return jsonify({"error": "Auth failed"}), 500


# ===============================
# RUN LOCAL (NOT USED ON RENDER)
# ===============================
if __name__ == '__main__':
    app.run(debug=True)
