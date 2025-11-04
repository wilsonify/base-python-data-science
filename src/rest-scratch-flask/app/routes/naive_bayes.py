from flask import Blueprint, request, jsonify
import sys
import os

# Add the data-scratch-library to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..', 'data-scratch-library'))

from dsl.c13_naive_bayes.naive_bayes import NaiveBayesClassifier

naive_bayes_bp = Blueprint('naive_bayes', __name__)

@naive_bayes_bp.route('/train', methods=['POST'])
def train_classifier():
    """
    Train a Naive Bayes classifier for spam detection.
    
    Request body:
    {
        "training_data": [
            {"message": "buy viagra now", "is_spam": true},
            {"message": "hello friend", "is_spam": false}
        ],
        "smoothing": 0.5
    }
    """
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        if 'training_data' not in data:
            return jsonify({'error': 'Missing required field: training_data'}), 400
        
        training_data = data['training_data']
        smoothing = data.get('smoothing', 0.5)
        
        # Validate data types
        if not isinstance(training_data, list):
            return jsonify({'error': 'training_data must be a list'}), 400
        
        if not isinstance(smoothing, (int, float)) or smoothing < 0:
            return jsonify({'error': 'smoothing must be a non-negative number'}), 400
        
        # Convert training data to the format expected by NaiveBayesClassifier
        training_set = []
        for item in training_data:
            if 'message' not in item or 'is_spam' not in item:
                return jsonify({'error': 'Each training item must have message and is_spam fields'}), 400
            
            if not isinstance(item['message'], str):
                return jsonify({'error': 'Message must be a string'}), 400
            
            if not isinstance(item['is_spam'], bool):
                return jsonify({'error': 'is_spam must be a boolean'}), 400
            
            training_set.append((item['message'], item['is_spam']))
        
        # Train the classifier
        classifier = NaiveBayesClassifier(k=smoothing)
        classifier.train(training_set)
        
        # Store the classifier in session or return as serialized data
        # For simplicity, we'll return basic training info
        spam_count = sum(1 for _, is_spam in training_set if is_spam)
        ham_count = len(training_set) - spam_count
        
        return jsonify({
            'status': 'trained',
            'training_samples': len(training_set),
            'spam_samples': spam_count,
            'ham_samples': ham_count,
            'smoothing_parameter': smoothing,
            'message': 'Classifier trained successfully. Use /classify endpoint with the same training data to classify messages.'
        })
        
    except Exception as e:
        return jsonify({'error': f'Training failed: {str(e)}'}), 500


@naive_bayes_bp.route('/classify', methods=['POST'])
def classify_message():
    """
    Classify a message as spam or ham using Naive Bayes.
    
    Request body:
    {
        "message": "buy viagra now",
        "training_data": [
            {"message": "buy viagra now", "is_spam": true},
            {"message": "hello friend", "is_spam": false}
        ],
        "smoothing": 0.5
    }
    """
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        if 'message' not in data or 'training_data' not in data:
            return jsonify({'error': 'Missing required fields: message, training_data'}), 400
        
        message = data['message']
        training_data = data['training_data']
        smoothing = data.get('smoothing', 0.5)
        
        # Validate data types
        if not isinstance(message, str):
            return jsonify({'error': 'message must be a string'}), 400
        
        if not isinstance(training_data, list):
            return jsonify({'error': 'training_data must be a list'}), 400
        
        # Convert training data to the format expected by NaiveBayesClassifier
        training_set = []
        for item in training_data:
            if 'message' not in item or 'is_spam' not in item:
                return jsonify({'error': 'Each training item must have message and is_spam fields'}), 400
            
            training_set.append((item['message'], item['is_spam']))
        
        # Train the classifier and classify
        classifier = NaiveBayesClassifier(k=smoothing)
        classifier.train(training_set)
        
        spam_probability = classifier.classify(message)
        is_spam = spam_probability > 0.5
        
        return jsonify({
            'message': message,
            'is_spam': is_spam,
            'spam_probability': spam_probability,
            'ham_probability': 1 - spam_probability,
            'training_samples': len(training_set),
            'smoothing_parameter': smoothing
        })
        
    except Exception as e:
        return jsonify({'error': f'Classification failed: {str(e)}'}), 500


@naive_bayes_bp.route('/batch_classify', methods=['POST'])
def batch_classify():
    """
    Classify multiple messages as spam or ham using Naive Bayes.
    
    Request body:
    {
        "messages": ["buy viagra now", "hello friend"],
        "training_data": [
            {"message": "buy viagra now", "is_spam": true},
            {"message": "hello friend", "is_spam": false}
        ],
        "smoothing": 0.5
    }
    """
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        if 'messages' not in data or 'training_data' not in data:
            return jsonify({'error': 'Missing required fields: messages, training_data'}), 400
        
        messages = data['messages']
        training_data = data['training_data']
        smoothing = data.get('smoothing', 0.5)
        
        # Validate data types
        if not isinstance(messages, list):
            return jsonify({'error': 'messages must be a list'}), 400
        
        if not isinstance(training_data, list):
            return jsonify({'error': 'training_data must be a list'}), 400
        
        # Convert training data to the format expected by NaiveBayesClassifier
        training_set = []
        for item in training_data:
            if 'message' not in item or 'is_spam' not in item:
                return jsonify({'error': 'Each training item must have message and is_spam fields'}), 400
            
            training_set.append((item['message'], item['is_spam']))
        
        # Train the classifier and classify
        classifier = NaiveBayesClassifier(k=smoothing)
        classifier.train(training_set)
        
        results = []
        for message in messages:
            spam_probability = classifier.classify(message)
            is_spam = spam_probability > 0.5
            
            results.append({
                'message': message,
                'is_spam': is_spam,
                'spam_probability': spam_probability,
                'ham_probability': 1 - spam_probability
            })
        
        return jsonify({
            'results': results,
            'messages_count': len(messages),
            'training_samples': len(training_set),
            'smoothing_parameter': smoothing
        })
        
    except Exception as e:
        return jsonify({'error': f'Batch classification failed: {str(e)}'}), 500


@naive_bayes_bp.route('/info', methods=['GET'])
def naive_bayes_info():
    """Get information about the Naive Bayes algorithm and parameters."""
    return jsonify({
        'algorithm': 'Naive Bayes Classifier',
        'description': 'A probabilistic classifier based on Bayes theorem with strong independence assumptions between features',
        'parameters': {
            'message': {
                'type': 'string',
                'description': 'The message to classify as spam or ham',
                'example': 'buy viagra now cheap pills'
            },
            'training_data': {
                'type': 'array',
                'description': 'Labeled training messages',
                'example': '[{"message": "buy viagra", "is_spam": true}]'
            },
            'smoothing': {
                'type': 'number',
                'description': 'Laplace smoothing parameter to handle zero frequency',
                'default': 0.5,
                'recommended': '0.5 to 1.0'
            }
        },
        'output': {
            'is_spam': 'boolean',
            'spam_probability': 'float (0-1)',
            'ham_probability': 'float (0-1)'
        },
        'notes': [
            'Uses bag-of-words model with tokenization',
            'Applies Laplace smoothing to handle unknown words',
            'Assumes conditional independence between words',
            'Works well for text classification tasks'
        ]
    })
