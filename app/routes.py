from flask import render_template, request, jsonify
from app import app
from app.scraping import scrape_leads
from app.email import send_email
from app.ml import train_model
from app.ai_bots import generate_response
from app.chatbot import get_chatbot_response
from app.data_bot import process_data
from app.entity_extraction import extract_entities  # Add this import

@app.route('/')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/leads')
def leads():
    leads = scrape_leads('https://example.com/leads')
    return render_template('leads.html', leads=leads)

@app.route('/email_campaigns', methods=['GET', 'POST'])
def email_campaigns():
    if request.method == 'POST':
        subject = request.form['subject']
        content = request.form['content']
        recipient = request.form['recipient']
        status = send_email(recipient, subject, content)
        return jsonify({'status': status})
    return render_template('email_campaigns.html')

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')

@app.route('/model_training', methods=['GET', 'POST'])
def model_training():
    if request.method == 'POST':
        data = request.json['data']
        labels = request.json['labels']
        model, accuracy = train_model(data, labels)
        return jsonify({'accuracy': accuracy})
    return render_template('model_training.html')

@app.route('/generate_response', methods=['POST'])
def generate_response_route():
    email_content = request.json.get('content')
    response = generate_response(email_content)
    return jsonify({'response': response})

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('message')
    intent, entities = get_chatbot_response(user_message)
    return jsonify({'intent': intent, 'entities': entities})

@app.route('/process_data', methods=['POST'])
def process_data_route():
    data = request.json.get('data')
    clusters = process_data(data)
    return jsonify({'clusters': clusters.tolist()})

@app.route('/extract_entities', methods=['POST'])  # Add this route
def extract_entities_route():
    text = request.json.get('text')
    entities = extract_entities(text)
    return jsonify({'entities': entities})
