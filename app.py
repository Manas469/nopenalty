from flask import Flask, request, jsonify
import os

app = Flask(__name__)

RULES = {
    "KYC": ["only mobile", "no aadhaar", "no pan"],
    "AML": ["50 lakh", "high risk country"],
    "PEP": ["politician", "sanction list"]
}

@app.route('/')
def home():
    return "<h1>NoPenalty: Zero RBI Fines</h1><p>₹9,900/month</p>"

@app.route('/check', methods=['POST'])
def check():
    prompt = request.json.get('prompt','').lower()
    violations = [k for k, v in RULES.items() if any(x in prompt for x in v)]
    return jsonify({
        "fine_risk": bool(violations),
        "violations": violations or "None",
        "action": "Escalate" if violations else "Safe"
    })

# FIXED: Bind to Render's PORT & HOST
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    host = '0.0.0.0'  # Listen on all interfaces
    app.run(host=host, port=port, debug=False)  # No debug in production