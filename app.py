from flask import Flask, render_template_string, jsonify, request
import os
import json
from datetime import datetime
from pathlib import Path

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Departament Marketing AI - Control Panel</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 0; background: #f5f5f5; }
            .header { background: #2c3e50; color: white; padding: 20px; }
            .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
            .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }
            .card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            .status { color: #27ae60; font-weight: bold; font-size: 18px; }
            .metric { display: flex; justify-content: space-between; margin: 10px 0; }
            .btn { background: #3498db; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; }
            .btn:hover { background: #2980b9; }
            .log { background: #ecf0f1; padding: 10px; border-radius: 4px; font-family: monospace; font-size: 12px; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🤖 Departament Marketing AI - Control Panel</h1>
            <p class="status">● Status: Operational</p>
        </div>
        
        <div class="container">
            <div class="grid">
                <div class="card">
                    <h3>System Metrics</h3>
                    <div class="metric"><span>Content Engine:</span><span>✅ Active</span></div>
                    <div class="metric"><span>AI Roles:</span><span>3 Configured</span></div>
                    <div class="metric"><span>Workflows:</span><span>4 Active</span></div>
                    <div class="metric"><span>Uptime:</span><span id="uptime">{{ uptime }}</span></div>
                </div>
                
                <div class="card">
                    <h3>Performance Today</h3>
                    <div class="metric"><span>Content Generated:</span><span>0</span></div>
                    <div class="metric"><span>Avg Processing Time:</span><span>--</span></div>
                    <div class="metric"><span>Success Rate:</span><span>100%</span></div>
                    <div class="metric"><span>Errors:</span><span>0</span></div>
                </div>
                
                <div class="card">
                    <h3>Quick Actions</h3>
                    <button class="btn" onclick="triggerContent()">Generate Content</button>
                    <button class="btn" onclick="runMetrics()">Run Metrics</button>
                    <button class="btn" onclick="viewLogs()">View Logs</button>
                </div>
                
                <div class="card">
                    <h3>System Log</h3>
                    <div class="log" id="systemLog">
                        [{{ timestamp }}] System initialized<br>
                        [{{ timestamp }}] All components operational<br>
                        [{{ timestamp }}] Ready for content production
                    </div>
                </div>
            </div>
        </div>
        
        <script>
            function triggerContent() {
                fetch('/api/trigger-content', {method: 'POST'})
                .then(r => r.json())
                .then(data => {
                    document.getElementById('systemLog').innerHTML += 
                        `<br>[${new Date().toLocaleTimeString()}] ${data.message}`;
                });
            }
            
            function runMetrics() {
                fetch('/api/run-metrics', {method: 'POST'})
                .then(r => r.json())
                .then(data => {
                    document.getElementById('systemLog').innerHTML += 
                        `<br>[${new Date().toLocaleTimeString()}] ${data.message}`;
                });
            }
            
            function viewLogs() {
                window.open('/logs', '_blank');
            }
        </script>
    </body>
    </html>
    ''', uptime="2h 34m", timestamp=datetime.now().strftime("%H:%M:%S"))

@app.route('/api/trigger-content', methods=['POST'])
def trigger_content():
    return jsonify({"status": "success", "message": "Content generation triggered"})

@app.route('/api/run-metrics', methods=['POST'])
def run_metrics():
    return jsonify({"status": "success", "message": "Metrics collection started"})

@app.route('/logs')
def logs():
    return "<pre>System logs would appear here</pre>"

@app.route('/api/system-status')
def system_status():
    return jsonify({
        "roles": ["Content Strategist", "Performance Tracker", "Workflow Manager"],
        "workflows": ["Content Production", "Quality Check", "Distribution"],
        "metrics": ["Daily Performance", "Conversion Rate", "Error Tracking"],
        "status": "Operational"
    })

@app.route('/api/generate-content', methods=['POST'])
def generate_content():
    data = request.get_json()
    return jsonify({
        "content_type": data.get("type", "blog_post"),
        "status": "generated", 
        "processing_time": "00:02:15",
        "quality_score": 8.7
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
