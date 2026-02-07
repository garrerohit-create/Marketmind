# =========================================================
# MARKETMIND — AUTONOMOUS GTM INFRASTRUCTURE
# One-file hackathon-winning system
# =========================================================

from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
from dotenv import load_dotenv
import os, re

# ---------------- CONFIG ----------------
load_dotenv()
DEMO_MODE = False  # set True if internet fails

# ---------------- APP -------------------
app = Flask(__name__)
CORS(app)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ---------------- RAG KNOWLEDGE ----------------
COMPANY_KNOWLEDGE = """
Marketmind is an agentic sales & marketing intelligence platform.
It replaces manual campaign planning, SDR work, and lead qualification.
Customers achieve:
- 40% reduction in cost of sales
- 2x faster pipeline velocity
- 3x higher personalization
Pricing: consumption & outcome based
Target: B2B SaaS, mid-market, enterprise GTM teams
"""

# ---------------- AI CORE ----------------
def ai_call(system, user):
    if DEMO_MODE:
        return """
[DEMO MODE]
Autonomous reasoning complete.
Outcome: High-confidence strategy
Conversion Probability: 82%
"""
    try:
        prompt = f"""
INTERNAL KNOWLEDGE (TRUSTED):
{COMPANY_KNOWLEDGE}

USER REQUEST:
{user}
"""
        res = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1400
        )
        return re.sub(r"\*\*", "", res.choices[0].message.content)
    except:
        return "AI temporarily unavailable. Demo-safe intelligence engaged."

# ---------------- UI ----------------
HTML = """
<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<title>Marketmind</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
body{
margin:0;font-family:Inter,sans-serif;
background:linear-gradient(135deg,#0f0c29,#302b63,#24243e);
color:white}
.container{max-width:1300px;margin:auto;padding:40px}
h1{text-align:center;font-size:52px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(380px,1fr));gap:25px}
.card{
background:rgba(255,255,255,.12);
backdrop-filter:blur(18px);
border-radius:22px;padding:30px;
box-shadow:0 0 40px rgba(0,0,0,.4)}
input,textarea,select{
width:100%;padding:12px;margin-bottom:12px;
border:none;border-radius:10px}
button{
background:#7f5cff;color:white;
border:none;border-radius:30px;
padding:14px 32px;font-size:16px;
cursor:pointer}
button:hover{transform:scale(1.05)}
pre strong {
  color: #a78bfa;
  font-weight: 600;
}

pre b {
  color: #a78bfa;
}

pre{
  background: rgba(15, 15, 30, 0.85);
  padding: 20px;
  border-radius: 14px;
  white-space: pre-wrap;

  /* FONT FIX */
  font-family: 'Inter', sans-serif;
  font-size: 14.5px;
  line-height: 1.65;
  color: #e5e7eb;

  /* VISUAL POLISH */
  box-shadow: inset 0 0 0 1px rgba(255,255,255,0.06);
}

.loader{
border:6px solid #eee;
border-top:6px solid #7f5cff;
border-radius:50%;
width:40px;height:40px;
animation:spin 1s linear infinite;
margin:auto}
@keyframes spin{100%{transform:rotate(360deg)}}
</style>
</head>

<body>
<div class="container">
<h1>🚀 MARKETMIND</h1>
<p style="text-align:center;font-size:18px">
Autonomous Sales & Marketing Intelligence
</p>

<div class="grid">

<div class="card">
<h2>🎯 Campaign Generator</h2>
<input id="c_product" placeholder="Product">
<textarea id="c_audience" placeholder="Audience"></textarea>
<select id="c_platform"><option>LinkedIn</option><option>Instagram</option><option>Twitter</option></select>
<button onclick="campaign()">Generate</button>
<div id="c_out"></div>
</div>

<div class="card">
<h2>💼 Sales Pitch</h2>
<input id="p_product" placeholder="Product">
<textarea id="p_persona" placeholder="Persona"></textarea>
<button onclick="pitch()">Generate</button>
<div id="p_out"></div>
</div>

<div class="card">
<h2>🔥 Lead Scoring</h2>
<input id="l_name" placeholder="Name">
<textarea id="l_budget" placeholder="Budget"></textarea>
<textarea id="l_need" placeholder="Need"></textarea>
<textarea id="l_urgency" placeholder="Urgency"></textarea>
<button onclick="lead()">Score</button>
<div id="l_out"></div>
<canvas id="leadChart"></canvas>
</div>

<div class="card">
<h2>🤖 Jazon – Autonomous SDR</h2>
<input id="a_name" placeholder="Lead Name">
<input id="a_company" placeholder="Company / Role">
<textarea id="a_signal" placeholder="Trigger Event"></textarea>
<button onclick="agent()">Activate</button>
<div id="a_out"></div>
</div>

<div class="card">
<h2>🧠 Multi-Agent Swarm</h2>
<input id="s_product" placeholder="Product">
<textarea id="s_market" placeholder="Market / ICP"></textarea>
<button onclick="swarm()">Run Swarm</button>
<div id="s_out"></div>
</div>

<div class="card">
<h2>📈 ROI Simulator</h2>
<input id="r_size" placeholder="Company Size">
<input id="r_leads" placeholder="Monthly Leads">
<input id="r_deal" placeholder="Avg Deal Value">
<button onclick="roi()">Simulate</button>
<canvas id="roiChart"></canvas>
</div>

</div>
</div>

<script>
function load(id){document.getElementById(id).innerHTML='<div class="loader"></div>'}

async function campaign(){
load("c_out")
const r=await fetch("/campaign",{method:"POST",headers:{"Content-Type":"application/json"},
body:JSON.stringify({product:c_product.value,audience:c_audience.value,platform:c_platform.value})})
const d=await r.json();c_out.innerHTML="<pre>"+d.result+"</pre>"}

async function pitch(){
load("p_out")
const r=await fetch("/pitch",{method:"POST",headers:{"Content-Type":"application/json"},
body:JSON.stringify({product:p_product.value,persona:p_persona.value})})
const d=await r.json();p_out.innerHTML="<pre>"+d.result+"</pre>"}

async function lead(){
load("l_out")
const r=await fetch("/lead",{method:"POST",headers:{"Content-Type":"application/json"},
body:JSON.stringify({
name:l_name.value,budget:l_budget.value,
need:l_need.value,urgency:l_urgency.value})})
const d=await r.json()
l_out.innerHTML="<pre>"+d.result+"</pre>"
new Chart(leadChart,{type:"doughnut",
data:{labels:["Score","Remaining"],datasets:[{data:[d.score,100-d.score]}]}})
}

async function agent(){
load("a_out")
const r=await fetch("/agent",{method:"POST",headers:{"Content-Type":"application/json"},
body:JSON.stringify({
name:a_name.value,company:a_company.value,signal:a_signal.value})})
const d=await r.json();a_out.innerHTML="<pre>"+d.result+"</pre>"}

async function swarm(){
load("s_out")
const r=await fetch("/swarm",{method:"POST",headers:{"Content-Type":"application/json"},
body:JSON.stringify({product:s_product.value,market:s_market.value})})
const d=await r.json();s_out.innerHTML="<pre>"+d.result+"</pre>"}

async function roi(){
const r=await fetch("/roi",{method:"POST",headers:{"Content-Type":"application/json"},
body:JSON.stringify({
size:r_size.value,leads:r_leads.value,deal:r_deal.value})})
const d=await r.json()
new Chart(roiChart,{type:"bar",
data:{labels:["Cost Saved","Revenue Gain","Efficiency %"],
datasets:[{data:[d.cost,d.revenue,d.efficiency]}]}})
}
</script>
</body>
</html>
"""

# ---------------- ROUTES ----------------
@app.route("/")
def home(): return HTML

@app.route("/campaign",methods=["POST"])
def campaign():
    d=request.json
    return jsonify(result=ai_call(
        "You are a Chief Marketing Officer.",
        f"Create a campaign for {d['product']} targeting {d['audience']} on {d['platform']}. Include ideas, ads, metrics. Executive Summary."
    ))

@app.route("/pitch",methods=["POST"])
def pitch():
    d=request.json
    return jsonify(result=ai_call(
        "You are a Sales Director.",
        f"Create a high-conversion pitch for {d['product']} selling to {d['persona']}. Executive Summary."
    ))

@app.route("/lead",methods=["POST"])
def lead():
    d=request.json
    res=ai_call("You are a Sales Analyst.",
        f"Score lead 0-100. Name:{d['name']} Budget:{d['budget']} Need:{d['need']} Urgency:{d['urgency']}")
    score=int(re.findall(r"\d+",res)[0])
    return jsonify(result=res,score=score)

@app.route("/agent",methods=["POST"])
def agent():
    d=request.json
    return jsonify(result=ai_call(
        "You are JAZON, an autonomous SDR.",
        f"SENSE, REASON, ACT, EVALUATE lead {d['name']} at {d['company']} triggered by {d['signal']}. Include actions taken. Executive Summary."
    ))

@app.route("/swarm",methods=["POST"])
def swarm():
    d=request.json
    return jsonify(result=ai_call(
        "You orchestrate a multi-agent GTM system.",
        f"Planner, Strategist, Executor for {d['product']} in {d['market']}. Executive Summary."
    ))

@app.route("/roi",methods=["POST"])
def roi():
    d=request.json
    res=ai_call("You are a Revenue Analyst.",
        f"Estimate ROI for company size {d['size']} leads {d['leads']} deal {d['deal']}")
    nums=re.findall(r"\d+",res)
    return jsonify(cost=int(nums[0]),revenue=int(nums[1]),efficiency=int(nums[2]))

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)
