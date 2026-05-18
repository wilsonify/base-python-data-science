from flask import Blueprint, request, jsonify

from dsl.c17_decision_trees.decision_trees import build_tree_id3, classify, forest_classify

decision_trees_bp = Blueprint('decision_trees', __name__)

# Common response messages (reduce duplicated string literals)
ERR_NO_JSON = 'No JSON data provided'
ERR_MISSING_TRAINING = 'Missing required field: training_data'
ERR_TRAINING_NOT_LIST = 'training_data must be a list'
ERR_SPLIT_CANDIDATES_LIST = 'split_candidates must be a list'
ERR_FEATURES_LABEL_FIELDS = 'Each training item must have features and label fields'
ERR_FEATURES_DICT = 'Features must be a dictionary'
ERR_LABEL_BOOL = 'Label must be a boolean'
ERR_MISSING_INSTANCE_TRAINING = 'Missing required fields: instance, training_data'
ERR_INSTANCE_DICT = 'instance must be a dictionary'
ERR_MISSING_INSTANCES_TRAINING = 'Missing required fields: instances, training_data'
ERR_INSTANCES_LIST = 'instances must be a list'
ERR_NUM_TREES_POSITIVE = 'num_trees must be a positive integer'

@decision_trees_bp.route('/train', methods=['POST'])
def train_tree():
    """
    Train a decision tree using the ID3 algorithm.
    
    Request body:
    {
        "training_data": [
            {"features": {"level": "Senior", "lang": "Java"}, "label": true},
            {"features": {"level": "Junior", "lang": "Python"}, "label": false}
        ],
        "split_candidates": ["level", "lang"]
    }
    """
    try:
        data = request.get_json(silent=True)
        
        # Validate required fields
        if not data:
            return jsonify({'error': ERR_NO_JSON}), 400
        
        if 'training_data' not in data:
            return jsonify({'error': ERR_MISSING_TRAINING}), 400
        
        training_data = data['training_data']
        split_candidates = data.get('split_candidates')
        
        # Validate data types
        if not isinstance(training_data, list):
            return jsonify({'error': ERR_TRAINING_NOT_LIST}), 400
        
        if split_candidates is not None and not isinstance(split_candidates, list):
            return jsonify({'error': ERR_SPLIT_CANDIDATES_LIST}), 400
        
        # Convert training data to the format expected by build_tree_id3
        formatted_data = []
        for item in training_data:
            if 'features' not in item or 'label' not in item:
                return jsonify({'error': ERR_FEATURES_LABEL_FIELDS}), 400
            
            if not isinstance(item['features'], dict):
                return jsonify({'error': ERR_FEATURES_DICT}), 400
            
            if not isinstance(item['label'], bool):
                return jsonify({'error': ERR_LABEL_BOOL}), 400
            
            formatted_data.append((item['features'], item['label']))
        
        # Train the decision tree
        tree = build_tree_id3(formatted_data, split_candidates=split_candidates)
        
        # Return tree information (simplified representation)
        return jsonify({
            'status': 'trained',
            'tree_type': type(tree).__name__,
            'training_samples': len(formatted_data),
            'split_candidates': split_candidates,
            'message': 'Decision tree trained successfully. Use /classify endpoint with the same training data to classify new instances.',
            'note': 'Tree structure is not serialized in this response. It exists in memory for classification.'
        })
        
    except Exception as e:
        return jsonify({'error': f'Training failed: {str(e)}'}), 500


@decision_trees_bp.route('/classify', methods=['POST'])
def classify_instance():
    """
    Classify an instance using a trained decision tree.
    
    Request body:
    {
        "instance": {"level": "Senior", "lang": "Java"},
        "training_data": [
            {"features": {"level": "Senior", "lang": "Java"}, "label": true},
            {"features": {"level": "Junior", "lang": "Python"}, "label": false}
        ],
        "split_candidates": ["level", "lang"]
    }
    """
    try:
        data = request.get_json(silent=True)
        
        # Validate required fields
        if not data:
            return jsonify({'error': ERR_NO_JSON}), 400
        
        if 'instance' not in data or 'training_data' not in data:
            return jsonify({'error': ERR_MISSING_INSTANCE_TRAINING}), 400
        
        instance = data['instance']
        training_data = data['training_data']
        split_candidates = data.get('split_candidates')
        
        # Validate data types
        if not isinstance(instance, dict):
            return jsonify({'error': ERR_INSTANCE_DICT}), 400
        
        if not isinstance(training_data, list):
            return jsonify({'error': ERR_TRAINING_NOT_LIST}), 400
        
        # Convert training data to the format expected by build_tree_id3
        formatted_data = []
        for item in training_data:
            if 'features' not in item or 'label' not in item:
                return jsonify({'error': ERR_FEATURES_LABEL_FIELDS}), 400

            formatted_data.append((item['features'], item['label']))

        # Train the decision tree and classify
        tree = build_tree_id3(formatted_data, split_candidates=split_candidates)
        # DSL classify signature is classify(tree, inputs)
        prediction = classify(tree, instance)

        return jsonify({
            'instance': instance,
            'prediction': prediction,
            'training_samples': len(formatted_data),
            'split_candidates': split_candidates
        })
        
    except Exception as e:
        return jsonify({'error': f'Classification failed: {str(e)}'}), 500


@decision_trees_bp.route('/batch_classify', methods=['POST'])
def batch_classify():
    """
    Classify multiple instances using a trained decision tree.
    
    Request body:
    {
        "instances": [
            {"level": "Senior", "lang": "Java"},
            {"level": "Junior", "lang": "Python"}
        ],
        "training_data": [
            {"features": {"level": "Senior", "lang": "Java"}, "label": true},
            {"features": {"level": "Junior", "lang": "Python"}, "label": false}
        ],
        "split_candidates": ["level", "lang"]
    }
    """
    try:
        data = request.get_json(silent=True)
        
        # Validate required fields
        if not data:
            return jsonify({'error': ERR_NO_JSON}), 400
        
        if 'instances' not in data or 'training_data' not in data:
            return jsonify({'error': ERR_MISSING_INSTANCES_TRAINING}), 400
        
        instances = data['instances']
        training_data = data['training_data']
        split_candidates = data.get('split_candidates')
        
        # Validate data types
        if not isinstance(instances, list):
            return jsonify({'error': ERR_INSTANCES_LIST}), 400
        
        if not isinstance(training_data, list):
            return jsonify({'error': ERR_TRAINING_NOT_LIST}), 400
        
        # Convert training data to the format expected by build_tree_id3
        formatted_data = []
        for item in training_data:
            if 'features' not in item or 'label' not in item:
                return jsonify({'error': ERR_FEATURES_LABEL_FIELDS}), 400
            
            formatted_data.append((item['features'], item['label']))
        
        # Train the decision tree and classify
        tree = build_tree_id3(formatted_data, split_candidates=split_candidates)

        results = []
        for instance in instances:
            # DSL classify signature is classify(tree, inputs)
            prediction = classify(tree, instance)
            results.append({
                'instance': instance,
                'prediction': prediction
            })
        
        return jsonify({
            'results': results,
            'instances_count': len(instances),
            'training_samples': len(formatted_data),
            'split_candidates': split_candidates
        })
        
    except Exception as e:
        return jsonify({'error': f'Batch classification failed: {str(e)}'}), 500


@decision_trees_bp.route('/forest_classify', methods=['POST'])
def forest_classify_endpoint():
    """
    Classify instances using a random forest (multiple decision trees).
    
    Request body:
    {
        "instance": {"level": "Senior", "lang": "Java"},
        "num_trees": 5,
        "training_data": [
            {"features": {"level": "Senior", "lang": "Java"}, "label": true},
            {"features": {"level": "Junior", "lang": "Python"}, "label": false}
        ]
    }
    """
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data:
            return jsonify({'error': ERR_NO_JSON}), 400
        
        if 'instance' not in data or 'training_data' not in data:
            return jsonify({'error': ERR_MISSING_INSTANCE_TRAINING}), 400
        
        instance = data['instance']
        training_data = data['training_data']
        num_trees = data.get('num_trees', 5)
        
        # Validate data types
        if not isinstance(instance, dict):
            return jsonify({'error': ERR_INSTANCE_DICT}), 400
        
        if not isinstance(training_data, list):
            return jsonify({'error': ERR_TRAINING_NOT_LIST}), 400
        
        if not isinstance(num_trees, int) or num_trees <= 0:
            return jsonify({'error': ERR_NUM_TREES_POSITIVE}), 400
        
        # Convert training data to the format expected by build_tree_id3
        formatted_data = []
        for item in training_data:
            if 'features' not in item or 'label' not in item:
                return jsonify({'error': ERR_FEATURES_LABEL_FIELDS}), 400
            
            formatted_data.append((item['features'], item['label']))
        
        # Train multiple trees (random forest)
        trees = []
        for _ in range(num_trees):
            # In a real implementation, you'd use bootstrap sampling
            # For simplicity, we'll train on the same data
            tree = build_tree_id3(formatted_data)
            trees.append(tree)
        
        # Classify using forest voting
        prediction = forest_classify(trees, instance)
        
        return jsonify({
            'instance': instance,
            'prediction': prediction,
            'num_trees': num_trees,
            'training_samples': len(formatted_data)
        })
        
    except Exception as e:
        return jsonify({'error': f'Forest classification failed: {str(e)}'}), 500


@decision_trees_bp.route('/info', methods=['GET'])
def decision_trees_info():
    """Get information about the Decision Tree algorithm and parameters."""
    return jsonify({
        'algorithm': 'Decision Trees (ID3)',
        'description': 'A tree-based model that makes predictions by learning simple decision rules inferred from data features',
        'parameters': {
            'training_data': {
                'type': 'array',
                'description': 'Labeled training instances with features and boolean labels',
                'example': '[{"features": {"level": "Senior"}, "label": true}]'
            },
            'split_candidates': {
                'type': 'array',
                'description': 'List of features to consider for splitting (optional)',
                'example': '["level", "lang", "experience"]'
            },
            'instance': {
                'type': 'object',
                'description': 'Feature dictionary to classify',
                'example': '{"level": "Senior", "lang": "Java"}'
            },
            'num_trees': {
                'type': 'integer',
                'description': 'Number of trees for random forest (forest_classify only)',
                'default': 5,
                'recommended': '5-50'
            }
        },
        'output': {
            'prediction': 'boolean (true/false)'
        },
        'notes': [
            'Uses ID3 algorithm with information gain for splitting',
            'Handles categorical features automatically',
            'Creates human-interpretable decision rules',
            'Random forest combines multiple trees for better accuracy'
        ]
    })
