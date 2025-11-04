import {
    buildDecisionTree,
    classify,
    printTree,
    treeAccuracy,
    RandomForest,
    exampleData,
    candidateAttributes
} from '../ts-data-scratch/decision_trees';

describe('Decision Trees', () => {
    describe('Basic Tree Building', () => {
        test('buildDecisionTree should create a tree from data', () => {
            const data = [
                { features: { level: 'Senior', lang: 'Java' }, label: true },
                { features: { level: 'Senior', lang: 'Python' }, label: false },
                { features: { level: 'Junior', lang: 'Java' }, label: false },
                { features: { level: 'Junior', lang: 'Python' }, label: true }
            ];
            
            const attributes = ['level', 'lang'];
            const tree = buildDecisionTree(data, attributes);
            
            expect(tree).toBeDefined();
            expect(typeof tree).toBe('object');
        });

        test('buildDecisionTree should handle empty data', () => {
            const tree = buildDecisionTree([], ['attr1']);
            expect(tree).toBeDefined();
            expect(typeof tree).toBe('object');
        });

        test('buildDecisionTree should handle no attributes', () => {
            const data = [
                { features: {}, label: true },
                { features: {}, label: false }
            ];
            
            const tree = buildDecisionTree(data, []);
            expect(tree).toBeDefined();
            expect(typeof tree).toBe('object');
        });

        test('buildDecisionTree should handle single attribute', () => {
            const data = [
                { features: { color: 'red' }, label: true },
                { features: { color: 'blue' }, label: false },
                { features: { color: 'red' }, label: true },
                { features: { color: 'blue' }, label: false }
            ];
            
            const tree = buildDecisionTree(data, ['color']);
            expect(tree).toBeDefined();
        });

        test('buildDecisionTree should handle all same labels', () => {
            const data = [
                { features: { attr: 'a' }, label: true },
                { features: { attr: 'b' }, label: true },
                { features: { attr: 'c' }, label: true }
            ];
            
            const tree = buildDecisionTree(data, ['attr']);
            expect(tree.prediction).toBe(true);
        });
    });

    describe('Classification', () => {
        const trainingData = [
            { features: { level: 'Senior', lang: 'Java' }, label: true },
            { features: { level: 'Senior', lang: 'Python' }, label: false },
            { features: { level: 'Junior', lang: 'Java' }, label: false },
            { features: { level: 'Junior', lang: 'Python' }, label: true },
            { features: { level: 'Mid', lang: 'Java' }, label: true },
            { features: { level: 'Mid', lang: 'Python' }, label: true }
        ];

        test('classify should make predictions', () => {
            const tree = buildDecisionTree(trainingData, ['level', 'lang']);
            
            const prediction1 = classify(tree, { level: 'Senior', lang: 'Java' });
            const prediction2 = classify(tree, { level: 'Junior', lang: 'Python' });
            
            expect(typeof prediction1).toBe('boolean');
            expect(typeof prediction2).toBe('boolean');
        });

        test('classify should handle unseen feature values', () => {
            const tree = buildDecisionTree(trainingData, ['level', 'lang']);
            
            const prediction = classify(tree, { level: 'Intern', lang: 'Ruby' });
            expect(typeof prediction).toBe('boolean');
        });

        test('classify should handle missing features', () => {
            const tree = buildDecisionTree(trainingData, ['level', 'lang']);
            
            const prediction = classify(tree, { level: 'Senior' });
            expect(typeof prediction).toBe('boolean');
        });

        test('classify should handle empty features', () => {
            const tree = buildDecisionTree(trainingData, ['level', 'lang']);
            
            const prediction = classify(tree, {});
            expect(typeof prediction).toBe('boolean');
        });

        test('classify should be consistent', () => {
            const tree = buildDecisionTree(trainingData, ['level', 'lang']);
            
            const prediction1 = classify(tree, { level: 'Senior', lang: 'Java' });
            const prediction2 = classify(tree, { level: 'Senior', lang: 'Java' });
            
            expect(prediction1).toBe(prediction2);
        });
    });

    describe('Tree Accuracy', () => {
        test('treeAccuracy should calculate correct accuracy', () => {
            const tree = buildDecisionTree(exampleData, candidateAttributes);
            const accuracy = treeAccuracy(tree, exampleData);
            
            expect(typeof accuracy).toBe('number');
            expect(accuracy).toBeGreaterThanOrEqual(0);
            expect(accuracy).toBeLessThanOrEqual(1);
        });

        test('treeAccuracy should handle perfect predictions', () => {
            const data = [
                { features: { x: 1 }, label: true },
                { features: { x: 2 }, label: true }
            ];
            
            const tree = buildDecisionTree(data, ['x']);
            const accuracy = treeAccuracy(tree, data);
            
            expect(accuracy).toBe(1);
        });

        test('treeAccuracy should handle test data', () => {
            const trainingData = [
                { features: { a: 1 }, label: true },
                { features: { a: 2 }, label: false }
            ];
            
            const testData = [
                { features: { a: 1 }, label: true },
                { features: { a: 2 }, label: false },
                { features: { a: 3 }, label: true }
            ];
            
            const tree = buildDecisionTree(trainingData, ['a']);
            const accuracy = treeAccuracy(tree, testData);
            
            expect(typeof accuracy).toBe('number');
            expect(accuracy).toBeGreaterThanOrEqual(0);
            expect(accuracy).toBeLessThanOrEqual(1);
        });

        test('treeAccuracy should handle empty test data', () => {
            const tree = buildDecisionTree(exampleData, candidateAttributes);
            const accuracy = treeAccuracy(tree, []);
            
            expect(accuracy).toBe(0);
        });
    });

    describe('Random Forest', () => {
        test('RandomForest should create ensemble of trees', () => {
            const forest = new RandomForest(exampleData, candidateAttributes, 3, 0.8, 2);
            
            expect(forest).toBeDefined();
            expect(forest.trees).toHaveLength(3);
        });

        test('RandomForest should make predictions', () => {
            const forest = new RandomForest(exampleData, candidateAttributes, 5, 0.8, 2);
            
            const prediction = forest.predict({ level: 'Senior', lang: 'Java' });
            expect(typeof prediction).toBe('boolean');
        });

        test('RandomForest should handle different tree counts', () => {
            const forest1 = new RandomForest(exampleData, candidateAttributes, 3, 0.8, 2);
            const forest2 = new RandomForest(exampleData, candidateAttributes, 10, 0.8, 2);
            
            expect(forest1.trees).toHaveLength(3);
            expect(forest2.trees).toHaveLength(10);
        });

        test('RandomForest should handle different sample sizes', () => {
            const forest1 = new RandomForest(exampleData, candidateAttributes, 5, 0.5, 2);
            const forest2 = new RandomForest(exampleData, candidateAttributes, 5, 1.0, 2);
            
            expect(forest1.trees).toHaveLength(5);
            expect(forest2.trees).toHaveLength(5);
        });

        test('RandomForest should handle different feature subsets', () => {
            const forest1 = new RandomForest(exampleData, candidateAttributes, 5, 0.8, 1);
            const forest2 = new RandomForest(exampleData, candidateAttributes, 5, 0.8, 2);
            
            expect(forest1.trees).toHaveLength(5);
            expect(forest2.trees).toHaveLength(5);
        });

        test('RandomForest should calculate accuracy', () => {
            const forest = new RandomForest(exampleData, candidateAttributes, 5, 0.8, 2);
            
            const accuracy = forest.calculateAccuracy(exampleData);
            expect(typeof accuracy).toBe('number');
            expect(accuracy).toBeGreaterThanOrEqual(0);
            expect(accuracy).toBeLessThanOrEqual(1);
        });

        test('RandomForest should handle single tree', () => {
            const forest = new RandomForest(exampleData, candidateAttributes, 1, 0.8, 2);
            
            expect(forest.trees).toHaveLength(1);
            
            const prediction = forest.predict({ level: 'Senior', lang: 'Java' });
            expect(typeof prediction).toBe('boolean');
        });

        test('RandomForest should handle empty data', () => {
            expect(() => {
                new RandomForest([], ['attr1'], 3, 0.8, 2);
            }).toThrow();
        });

        test('RandomForest should handle no attributes', () => {
            const data = [
                { features: {}, label: true },
                { features: {}, label: false }
            ];
            
            const forest = new RandomForest(data, [], 3, 0.8, 2);
            expect(forest.trees).toHaveLength(3);
        });
    });

    describe('Tree Visualization', () => {
        test('printTree should generate tree string', () => {
            const tree = buildDecisionTree(exampleData, candidateAttributes);
            
            expect(() => {
                const treeString = printTree(tree);
                expect(typeof treeString).toBe('string');
                expect(treeString.length).toBeGreaterThan(0);
            }).not.toThrow();
        });

        test('printTree should handle simple trees', () => {
            const data = [
                { features: { x: 1 }, label: true }
            ];
            
            const tree = buildDecisionTree(data, ['x']);
            const treeString = printTree(tree);
            
            expect(typeof treeString).toBe('string');
            expect(treeString.length).toBeGreaterThan(0);
        });

        test('printTree should handle leaf nodes', () => {
            const tree = { prediction: true };
            const treeString = printTree(tree);
            
            expect(typeof treeString).toBe('string');
            expect(treeString).toContain('true');
        });
    });

    describe('Example Data', () => {
        test('exampleData should be properly formatted', () => {
            expect(exampleData.length).toBeGreaterThan(0);
            
            exampleData.forEach(item => {
                expect(item).toHaveProperty('features');
                expect(item).toHaveProperty('label');
                expect(typeof item.label).toBe('boolean');
                expect(typeof item.features).toBe('object');
            });
        });

        test('candidateAttributes should be array of strings', () => {
            expect(Array.isArray(candidateAttributes)).toBe(true);
            expect(candidateAttributes.length).toBeGreaterThan(0);
            
            candidateAttributes.forEach(attr => {
                expect(typeof attr).toBe('string');
            });
        });
    });

    describe('Edge Cases', () => {
        test('should handle large datasets', () => {
            const largeData = [];
            const attributes = ['attr1', 'attr2', 'attr3'];
            
            for (let i = 0; i < 100; i++) {
                largeData.push({
                    features: {
                        attr1: `value${i % 10}`,
                        attr2: `value${i % 5}`,
                        attr3: `value${i % 2}`
                    },
                    label: i % 2 === 0
                });
            }
            
            const start = Date.now();
            const tree = buildDecisionTree(largeData, attributes);
            const duration = Date.now() - start;
            
            expect(tree).toBeDefined();
            expect(duration).toBeLessThan(5000); // Should complete within 5 seconds
        });

        test('should handle many attributes', () => {
            const data = [];
            const attributes = [];
            
            // Create 20 attributes
            for (let i = 0; i < 20; i++) {
                attributes.push(`attr${i}`);
            }
            
            for (let i = 0; i < 50; i++) {
                const features = {};
                attributes.forEach(attr => {
                    features[attr] = `value${i % 3}`;
                });
                data.push({ features, label: i % 2 === 0 });
            }
            
            const tree = buildDecisionTree(data, attributes);
            expect(tree).toBeDefined();
        });

        test('should handle unique feature values', () => {
            const data = [];
            for (let i = 0; i < 10; i++) {
                data.push({
                    features: { unique: `value${i}` },
                    label: i % 2 === 0
                });
            }
            
            const tree = buildDecisionTree(data, ['unique']);
            expect(tree).toBeDefined();
        });

        test('should handle boolean feature values', () => {
            const data = [
                { features: { flag: true, value: 'high' }, label: true },
                { features: { flag: false, value: 'low' }, label: false },
                { features: { flag: true, value: 'low' }, label: true },
                { features: { flag: false, value: 'high' }, label: false }
            ];
            
            const tree = buildDecisionTree(data, ['flag', 'value']);
            expect(tree).toBeDefined();
            
            const prediction = classify(tree, { flag: true, value: 'medium' });
            expect(typeof prediction).toBe('boolean');
        });

        test('should handle numeric string values', () => {
            const data = [
                { features: { score: '10', level: 'high' }, label: true },
                { features: { score: '5', level: 'low' }, label: false },
                { features: { score: '8', level: 'medium' }, label: true }
            ];
            
            const tree = buildDecisionTree(data, ['score', 'level']);
            expect(tree).toBeDefined();
        });
    });

    describe('Performance Tests', () => {
        test('should handle rapid classification', () => {
            const tree = buildDecisionTree(exampleData, candidateAttributes);
            
            const start = Date.now();
            for (let i = 0; i < 1000; i++) {
                classify(tree, { level: 'Senior', lang: 'Java' });
            }
            const duration = Date.now() - start;
            
            expect(duration).toBeLessThan(1000); // Should complete 1000 classifications within 1 second
        });

        test('should handle multiple tree building', () => {
            const start = Date.now();
            for (let i = 0; i < 10; i++) {
                buildDecisionTree(exampleData, candidateAttributes);
            }
            const duration = Date.now() - start;
            
            expect(duration).toBeLessThan(3000); // Should build 10 trees within 3 seconds
        });
    });

    describe('Consistency Tests', () => {
        test('should produce consistent trees for same data', () => {
            const tree1 = buildDecisionTree(exampleData, candidateAttributes);
            const tree2 = buildDecisionTree(exampleData, candidateAttributes);
            
            // Trees should be identical for same data and same random seed
            const acc1 = treeAccuracy(tree1, exampleData);
            const acc2 = treeAccuracy(tree2, exampleData);
            
            expect(acc1).toBe(acc2);
        });

        test('should handle deterministic behavior', () => {
            const testFeatures = { level: 'Senior', lang: 'Java' };
            
            const tree = buildDecisionTree(exampleData, candidateAttributes);
            const pred1 = classify(tree, testFeatures);
            const pred2 = classify(tree, testFeatures);
            
            expect(pred1).toBe(pred2);
        });
    });

    describe('Error Handling', () => {
        test('should handle malformed data gracefully', () => {
            const malformedData = [
                { features: null, label: true },
                { features: undefined, label: false },
                { features: { attr: 'value' }, label: null }
            ];
            
            expect(() => {
                buildDecisionTree(malformedData, ['attr']);
            }).toThrow();
        });

        test('should handle null attributes', () => {
            const data = [
                { features: { attr: 'value' }, label: true }
            ];
            
            expect(() => {
                buildDecisionTree(data, null as any);
            }).toThrow();
        });

        test('should handle undefined attributes', () => {
            const data = [
                { features: { attr: 'value' }, label: true }
            ];
            
            expect(() => {
                buildDecisionTree(data, undefined as any);
            }).toThrow();
        });
    });
});
