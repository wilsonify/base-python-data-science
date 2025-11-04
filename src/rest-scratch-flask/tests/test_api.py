import pytest
import json
from app import create_app


@pytest.fixture
def app():
    """Create test app."""
    app = create_app()
    app.config['TESTING'] = True
    return app


@pytest.fixture
def client(app):
    """Create test client."""
    return app.test_client()


@pytest.fixture
def headers():
    """Default headers for requests."""
    return {'Content-Type': 'application/json'}


class TestHealthCheck:
    """Test health check endpoints."""
    
    def test_health_check(self, client):
        """Test health check endpoint."""
        response = client.get('/health')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['status'] == 'healthy'
        assert 'message' in data
    
    def test_api_info(self, client):
        """Test API info endpoint."""
        response = client.get('/')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert 'name' in data
        assert 'version' in data
        assert 'endpoints' in data


class TestKNN:
    """Test KNN endpoints."""
    
    def test_knn_classify_success(self, client, headers):
        """Test successful KNN classification."""
        data = {
            "k": 3,
            "point": [1.0, 2.0],
            "training_data": [
                {"point": [1.1, 2.1], "label": "A"},
                {"point": [3.0, 4.0], "label": "B"},
                {"point": [1.2, 2.2], "label": "A"}
            ]
        }
        
        response = client.post('/api/knn/classify', 
                             data=json.dumps(data), 
                             headers=headers)
        assert response.status_code == 200
        
        result = json.loads(response.data)
        assert 'prediction' in result
        assert result['k'] == 3
        assert result['point'] == [1.0, 2.0]
    
    def test_knn_classify_missing_fields(self, client, headers):
        """Test KNN classification with missing fields."""
        data = {
            "k": 3,
            "point": [1.0, 2.0]
            # Missing training_data
        }
        
        response = client.post('/api/knn/classify', 
                             data=json.dumps(data), 
                             headers=headers)
        assert response.status_code == 400
        
        result = json.loads(response.data)
        assert 'error' in result
    
    def test_knn_batch_classify(self, client, headers):
        """Test KNN batch classification."""
        data = {
            "k": 3,
            "points": [[1.0, 2.0], [3.0, 4.0]],
            "training_data": [
                {"point": [1.1, 2.1], "label": "A"},
                {"point": [3.1, 4.1], "label": "B"}
            ]
        }
        
        response = client.post('/api/knn/batch_classify', 
                             data=json.dumps(data), 
                             headers=headers)
        assert response.status_code == 200
        
        result = json.loads(response.data)
        assert 'predictions' in result
        assert len(result['predictions']) == 2
    
    def test_knn_info(self, client):
        """Test KNN info endpoint."""
        response = client.get('/api/knn/info')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert 'algorithm' in data
        assert 'parameters' in data


class TestNaiveBayes:
    """Test Naive Bayes endpoints."""
    
    def test_naive_bayes_classify_success(self, client, headers):
        """Test successful Naive Bayes classification."""
        data = {
            "message": "buy viagra now cheap pills",
            "training_data": [
                {"message": "buy viagra now", "is_spam": True},
                {"message": "hello friend", "is_spam": False},
                {"message": "cheap pills online", "is_spam": True}
            ],
            "smoothing": 0.5
        }
        
        response = client.post('/api/naive-bayes/classify', 
                             data=json.dumps(data), 
                             headers=headers)
        assert response.status_code == 200
        
        result = json.loads(response.data)
        assert 'is_spam' in result
        assert 'spam_probability' in result
        assert 'ham_probability' in result
    
    def test_naive_bayes_batch_classify(self, client, headers):
        """Test Naive Bayes batch classification."""
        data = {
            "messages": ["buy viagra", "hello friend"],
            "training_data": [
                {"message": "buy viagra now", "is_spam": True},
                {"message": "hello friend", "is_spam": False}
            ]
        }
        
        response = client.post('/api/naive-bayes/batch_classify', 
                             data=json.dumps(data), 
                             headers=headers)
        assert response.status_code == 200
        
        result = json.loads(response.data)
        assert 'results' in result
        assert len(result['results']) == 2
    
    def test_naive_bayes_info(self, client):
        """Test Naive Bayes info endpoint."""
        response = client.get('/api/naive-bayes/info')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert 'algorithm' in data
        assert 'parameters' in data


class TestDecisionTrees:
    """Test Decision Trees endpoints."""
    
    def test_decision_tree_classify_success(self, client, headers):
        """Test successful decision tree classification."""
        data = {
            "instance": {"level": "Senior", "lang": "Java"},
            "training_data": [
                {"features": {"level": "Senior", "lang": "Java"}, "label": True},
                {"features": {"level": "Junior", "lang": "Python"}, "label": False},
                {"features": {"level": "Senior", "lang": "Python"}, "label": True}
            ],
            "split_candidates": ["level", "lang"]
        }
        
        response = client.post('/api/decision-trees/classify', 
                             data=json.dumps(data), 
                             headers=headers)
        assert response.status_code == 200
        
        result = json.loads(response.data)
        assert 'prediction' in result
        assert isinstance(result['prediction'], bool)
    
    def test_decision_tree_batch_classify(self, client, headers):
        """Test decision tree batch classification."""
        data = {
            "instances": [
                {"level": "Senior", "lang": "Java"},
                {"level": "Junior", "lang": "Python"}
            ],
            "training_data": [
                {"features": {"level": "Senior", "lang": "Java"}, "label": True},
                {"features": {"level": "Junior", "lang": "Python"}, "label": False}
            ]
        }
        
        response = client.post('/api/decision-trees/batch_classify', 
                             data=json.dumps(data), 
                             headers=headers)
        assert response.status_code == 200
        
        result = json.loads(response.data)
        assert 'results' in result
        assert len(result['results']) == 2
    
    def test_decision_tree_info(self, client):
        """Test decision tree info endpoint."""
        response = client.get('/api/decision-trees/info')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert 'algorithm' in data
        assert 'parameters' in data


class TestClustering:
    """Test Clustering endpoints."""
    
    def test_kmeans_clustering_success(self, client, headers):
        """Test successful K-means clustering."""
        data = {
            "data": [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0], [1.1, 2.1]],
            "k": 2,
            "max_iterations": 50
        }
        
        response = client.post('/api/clustering/kmeans', 
                             data=json.dumps(data), 
                             headers=headers)
        assert response.status_code == 200
        
        result = json.loads(response.data)
        assert 'clusters' in result
        assert 'assignments' in result
        assert 'means' in result
        assert result['k'] == 2
    
    def test_clustering_analyze(self, client, headers):
        """Test clustering analysis."""
        data = {
            "data": [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]],
            "assignments": [0, 1, 0],
            "means": [[1.5, 2.5], [4.0, 5.0]]
        }
        
        response = client.post('/api/clustering/analyze', 
                             data=json.dumps(data), 
                             headers=headers)
        assert response.status_code == 200
        
        result = json.loads(response.data)
        assert 'total_squared_error' in result
        assert 'cluster_sizes' in result
    
    def test_clustering_info(self, client):
        """Test clustering info endpoint."""
        response = client.get('/api/clustering/info')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert 'algorithms' in data
        assert 'parameters' in data


class TestNeuralNetworks:
    """Test Neural Networks endpoints."""
    
    def test_sigmoid_function(self, client, headers):
        """Test sigmoid activation function."""
        data = {"x": 1.0}
        
        response = client.post('/api/neural-networks/sigmoid', 
                             data=json.dumps(data), 
                             headers=headers)
        assert response.status_code == 200
        
        result = json.loads(response.data)
        assert 'sigmoid' in result
        assert 0 < result['sigmoid'] < 1
    
    def test_step_function(self, client, headers):
        """Test step function."""
        data = {"x": 1.0}
        
        response = client.post('/api/neural-networks/step', 
                             data=json.dumps(data), 
                             headers=headers)
        assert response.status_code == 200
        
        result = json.loads(response.data)
        assert 'step' in result
        assert result['step'] in [0, 1]
    
    def test_perceptron(self, client, headers):
        """Test perceptron prediction."""
        data = {
            "weights": [0.5, -0.5],
            "bias": -0.1,
            "inputs": [1.0, 0.5]
        }
        
        response = client.post('/api/neural-networks/perceptron', 
                             data=json.dumps(data), 
                             headers=headers)
        assert response.status_code == 200
        
        result = json.loads(response.data)
        assert 'output' in result
        assert 'weighted_sum' in result
    
    def test_neuron_activation(self, client, headers):
        """Test neuron activation."""
        data = {
            "weights": [0.5, -0.5],
            "inputs": [1.0, 0.5]
        }
        
        response = client.post('/api/neural-networks/neuron', 
                             data=json.dumps(data), 
                             headers=headers)
        assert response.status_code == 200
        
        result = json.loads(response.data)
        assert 'output' in result
        assert 0 < result['output'] < 1
    
    def test_feed_forward(self, client, headers):
        """Test feed forward propagation."""
        data = {
            "network": [
                [[0.5, -0.5], 0.0],  # Hidden layer
                [[1.0, 1.0], 0.0]    # Output layer
            ],
            "inputs": [1.0, 1.0]
        }
        
        response = client.post('/api/neural-networks/feed_forward', 
                             data=json.dumps(data), 
                             headers=headers)
        assert response.status_code == 200
        
        result = json.loads(response.data)
        assert 'layer_outputs' in result
        assert 'final_output' in result
    
    def test_neural_networks_info(self, client):
        """Test neural networks info endpoint."""
        response = client.get('/api/neural-networks/info')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert 'algorithms' in data
        assert 'functions' in data


class TestErrorHandling:
    """Test error handling across endpoints."""
    
    def test_invalid_json(self, client):
        """Test handling of invalid JSON."""
        response = client.post('/api/knn/classify', 
                             data="invalid json", 
                             headers={'Content-Type': 'application/json'})
        assert response.status_code == 400
    
    def test_missing_content_type(self, client):
        """Test handling of missing content type."""
        data = {"k": 3, "point": [1.0, 2.0]}
        response = client.post('/api/knn/classify', 
                             data=json.dumps(data))
        # Should still work but may not be properly parsed
        assert response.status_code in [400, 200]
    
    def test_empty_request_body(self, client, headers):
        """Test handling of empty request body."""
        response = client.post('/api/knn/classify', 
                             data="", 
                             headers=headers)
        assert response.status_code == 400
