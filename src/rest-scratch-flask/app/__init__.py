from flask import Flask, jsonify, send_from_directory
import os

# Try to import CORS, but make it optional
try:
    from flask_cors import CORS
    CORS_AVAILABLE = True
except ImportError:
    CORS_AVAILABLE = False

# Try to import Swagger UI, but make it optional
try:
    from flask_swagger_ui import get_swaggerui_blueprint
    SWAGGER_AVAILABLE = True
except ImportError:
    SWAGGER_AVAILABLE = False

def create_app():
    """Application factory pattern."""
    app = Flask(__name__)
    
    # Enable CORS if available
    if CORS_AVAILABLE:
        CORS(app)
    
    # Register blueprints
    from app.routes.knn import knn_bp
    from app.routes.naive_bayes import naive_bayes_bp
    from app.routes.decision_trees import decision_trees_bp
    from app.routes.clustering import clustering_bp
    from app.routes.neural_networks import neural_networks_bp
    
    app.register_blueprint(knn_bp, url_prefix='/api/knn')
    app.register_blueprint(naive_bayes_bp, url_prefix='/api/naive-bayes')
    app.register_blueprint(decision_trees_bp, url_prefix='/api/decision-trees')
    app.register_blueprint(clustering_bp, url_prefix='/api/clustering')
    app.register_blueprint(neural_networks_bp, url_prefix='/api/neural-networks')
    
    # Add Swagger UI if available
    if SWAGGER_AVAILABLE:
        SWAGGER_URL = '/docs'
        API_URL = '/openapi.yaml'
        
        swaggerui_blueprint = get_swaggerui_blueprint(
            SWAGGER_URL,
            API_URL,
            config={
                'app_name': "Data Scratch Library REST API",
                'dom_id': '#swagger-ui',
                'deepLinking': True,
                'showExtensions': True,
                'showCommonExtensions': True
            }
        )
        
        app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    
    # OpenAPI specification endpoint
    @app.route('/openapi.yaml', methods=['GET'])
    def openapi_spec():
        """Serve the OpenAPI specification."""
        try:
            # Get the directory containing this file
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # Go up one level to the rest-scratch-flask directory
            parent_dir = os.path.dirname(current_dir)
            spec_path = os.path.join(parent_dir, 'openapi.yaml')
            
            if os.path.exists(spec_path):
                return send_from_directory(parent_dir, 'openapi.yaml', 
                                         mimetype='application/x-yaml')
            else:
                return jsonify({'error': 'OpenAPI specification not found'}), 404
        except Exception as e:
            return jsonify({'error': f'Error serving OpenAPI spec: {str(e)}'}), 500
    
    # Health check endpoint
    @app.route('/health', methods=['GET'])
    def health_check():
        response = {'status': 'healthy', 'message': 'Data Scratch Library API is running'}
        if not CORS_AVAILABLE:
            response['note'] = 'CORS not available - install Flask-CORS for cross-origin support'
        if not SWAGGER_AVAILABLE:
            response['docs_note'] = 'Swagger UI not available - install flask-swagger-ui for API documentation'
        return response
    
    # Root endpoint with API info
    @app.route('/', methods=['GET'])
    def api_info():
        response = {
            'name': 'Data Scratch Library REST API',
            'version': '1.0.0',
            'cors_enabled': CORS_AVAILABLE,
            'swagger_ui_enabled': SWAGGER_AVAILABLE,
            'endpoints': {
                'knn': '/api/knn',
                'naive_bayes': '/api/naive-bayes',
                'decision_trees': '/api/decision-trees',
                'clustering': '/api/clustering',
                'neural_networks': '/api/neural-networks',
                'health': '/health',
                'openapi_spec': '/openapi.yaml'
            }
        }
        
        if SWAGGER_AVAILABLE:
            response['endpoints']['swagger_ui'] = '/docs'
        
        return response
    
    return app
