from flask import request, jsonify
from ..main import app
from ..services.neo4j_integration import Neo4jHandler

@app.route('/input_transit', methods=['POST'])
def input_transit():
    try:
        data = request.json
        # Extract necessary fields from the input data
        chart_id = data['chart_id']
        positions = data['positions']
        aspects = data['aspects']
        
        # Initialize Neo4j handler
        neo4j_handler = Neo4jHandler(uri="bolt://localhost:7687", user="neo4j", password="password")
        
        # Store the data in Neo4j
        neo4j_handler.save_chart(chart_id, positions, aspects)
        neo4j_handler.close()
        
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500