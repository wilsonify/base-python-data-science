import {
    NaiveBayesClassifier,
    trainNaiveBayesClassifier,
    classifyMessage,
    naiveBayesCrossValidate,
    exampleMessages,
    exampleUsage
} from '../ts-data-scratch/naive_bayes';

describe('Naive Bayes', () => {
    describe('NaiveBayesClassifier', () => {
        const trainingMessages = [
            { message: 'buy viagra now cheap pills', isSpam: true },
            { message: 'limited time offer free money', isSpam: true },
            { message: 'hello friend how are you', isSpam: false },
            { message: 'meeting tomorrow at 3pm', isSpam: false },
            { message: 'project deadline next week', isSpam: false }
        ];

        test('should train classifier successfully', () => {
            const classifier = new NaiveBayesClassifier();
            classifier.train(trainingMessages);
            
            const info = classifier.getTrainingInfo();
            expect(info.isTrained).toBe(true);
            expect(info.vocabSize).toBeGreaterThan(0);
            expect(info.spamPrior).toBeGreaterThan(0);
            expect(info.hamPrior).toBeGreaterThan(0);
        });

        test('should classify spam messages correctly', () => {
            const classifier = new NaiveBayesClassifier();
            classifier.train(trainingMessages);
            
            const spamResult = classifier.classify('buy cheap pills online');
            expect(spamResult.isSpam).toBe(true);
            expect(spamResult.spamProbability).toBeGreaterThan(0.5);
            expect(spamResult.hamProbability).toBeLessThan(0.5);
        });

        test('should classify ham messages correctly', () => {
            const classifier = new NaiveBayesClassifier();
            classifier.train(trainingMessages);
            
            const hamResult = classifier.classify('hello my dear friend');
            expect(hamResult.isSpam).toBe(false);
            expect(hamResult.hamProbability).toBeGreaterThan(0.5);
            expect(hamResult.spamProbability).toBeLessThan(0.5);
        });

        test('should handle unknown words gracefully', () => {
            const classifier = new NaiveBayesClassifier();
            classifier.train(trainingMessages);
            
            const result = classifier.classify('completely new words here');
            expect(typeof result.isSpam).toBe('boolean');
            expect(typeof result.spamProbability).toBe('number');
            expect(typeof result.hamProbability).toBe('number');
            expect(result.spamProbability + result.hamProbability).toBeCloseTo(1, 5);
        });

        test('should handle empty message', () => {
            const classifier = new NaiveBayesClassifier();
            classifier.train(trainingMessages);
            
            const result = classifier.classify('');
            expect(typeof result.isSpam).toBe('boolean');
            expect(result.spamProbability).toBeGreaterThanOrEqual(0);
            expect(result.hamProbability).toBeGreaterThanOrEqual(0);
        });

        test('should throw error when classifying without training', () => {
            const classifier = new NaiveBayesClassifier();
            expect(() => classifier.classify('test message')).toThrow('Classifier must be trained before classification');
        });

        test('should handle different smoothing parameters', () => {
            const classifier1 = new NaiveBayesClassifier(0.1);
            const classifier2 = new NaiveBayesClassifier(1.0);
            
            classifier1.train(trainingMessages);
            classifier2.train(trainingMessages);
            
            const result1 = classifier1.classify('buy pills');
            const result2 = classifier2.classify('buy pills');
            
            expect(result1.spamProbability).not.toBe(result2.spamProbability);
        });

        test('should get word probabilities', () => {
            const classifier = new NaiveBayesClassifier();
            classifier.train(trainingMessages);
            
            const wordProbs = classifier.getWordProbabilities();
            expect(wordProbs.size).toBeGreaterThan(0);
            
            // Check that known words have probabilities
            if (wordProbs.has('buy')) {
                const probs = wordProbs.get('buy')!;
                expect(typeof probs.spam).toBe('number');
                expect(typeof probs.ham).toBe('number');
            }
        });

        test('should handle single class training data', () => {
            const singleClassData = [
                { message: 'spam message one', isSpam: true },
                { message: 'spam message two', isSpam: true }
            ];
            
            const classifier = new NaiveBayesClassifier();
            classifier.train(singleClassData);
            
            const result = classifier.classify('test message');
            expect(typeof result.isSpam).toBe('boolean');
        });
    });

    describe('Convenience Functions', () => {
        const trainingMessages = [
            { message: 'buy viagra now', isSpam: true },
            { message: 'hello friend', isSpam: false }
        ];

        test('trainNaiveBayesClassifier should return trained classifier', () => {
            const classifier = trainNaiveBayesClassifier(trainingMessages, 0.5);
            
            expect(classifier).toBeInstanceOf(NaiveBayesClassifier);
            const info = classifier.getTrainingInfo();
            expect(info.isTrained).toBe(true);
        });

        test('classifyMessage should classify without creating classifier instance', () => {
            const result = classifyMessage('buy cheap pills', trainingMessages, 0.5);
            
            expect(result).toHaveProperty('isSpam');
            expect(result).toHaveProperty('spamProbability');
            expect(result).toHaveProperty('hamProbability');
            expect(typeof result.isSpam).toBe('boolean');
        });
    });

    describe('Cross-Validation', () => {
        const messages = [
            { message: 'buy viagra now cheap pills', isSpam: true },
            { message: 'limited time offer free money', isSpam: true },
            { message: 'amazing discount click here', isSpam: true },
            { message: 'hello friend how are you', isSpam: false },
            { message: 'meeting tomorrow at 3pm', isSpam: false },
            { message: 'project deadline next week', isSpam: false },
            { message: 'lunch plans today', isSpam: false },
            { message: 'weekend trip arrangements', isSpam: false }
        ];

        test('naiveBayesCrossValidate should return accuracy between 0 and 1', () => {
            const accuracy = naiveBayesCrossValidate(messages, 4, 0.5);
            expect(accuracy).toBeGreaterThanOrEqual(0);
            expect(accuracy).toBeLessThanOrEqual(1);
        });

        test('naiveBayesCrossValidate should handle different fold counts', () => {
            const acc2 = naiveBayesCrossValidate(messages, 2, 0.5);
            const acc4 = naiveBayesCrossValidate(messages, 4, 0.5);
            
            expect(typeof acc2).toBe('number');
            expect(typeof acc4).toBe('number');
        });

        test('naiveBayesCrossValidate should handle small datasets', () => {
            const smallData = [
                { message: 'spam message', isSpam: true },
                { message: 'ham message', isSpam: false }
            ];
            
            const accuracy = naiveBayesCrossValidate(smallData, 2, 0.5);
            expect(typeof accuracy).toBe('number');
        });
    });

    describe('Example Data', () => {
        test('exampleMessages should be properly formatted', () => {
            expect(exampleMessages).toHaveLength(10);
            expect(exampleMessages[0]).toHaveProperty('message');
            expect(exampleMessages[0]).toHaveProperty('isSpam');
            expect(typeof exampleMessages[0].message).toBe('string');
            expect(typeof exampleMessages[0].isSpam).toBe('boolean');
        });

        test('exampleUsage should run without errors', () => {
            expect(() => exampleUsage()).not.toThrow();
        });
    });

    describe('Edge Cases', () => {
        test('should handle messages with only punctuation', () => {
            const classifier = new NaiveBayesClassifier();
            classifier.train([
                { message: 'normal message', isSpam: false },
                { message: 'spam message', isSpam: true }
            ]);
            
            const result = classifier.classify('!!! ??? ...');
            expect(typeof result.isSpam).toBe('boolean');
        });

        test('should handle messages with mixed case', () => {
            const classifier = new NaiveBayesClassifier();
            classifier.train([
                { message: 'BUY NOW', isSpam: true },
                { message: 'hello friend', isSpam: false }
            ]);
            
            const result1 = classifier.classify('buy now');
            const result2 = classifier.classify('BUY NOW');
            const result3 = classifier.classify('Buy Now');
            
            // All should give the same classification
            expect(result1.isSpam).toBe(result2.isSpam);
            expect(result2.isSpam).toBe(result3.isSpam);
        });

        test('should handle very long messages', () => {
            const classifier = new NaiveBayesClassifier();
            classifier.train([
                { message: 'spam', isSpam: true },
                { message: 'ham', isSpam: false }
            ]);
            
            const longMessage = 'word '.repeat(1000);
            const result = classifier.classify(longMessage);
            expect(typeof result.isSpam).toBe('boolean');
        });

        test('should handle messages with numbers', () => {
            const classifier = new NaiveBayesClassifier();
            classifier.train([
                { message: 'buy now for 99 dollars', isSpam: true },
                { message: 'meeting at 3pm', isSpam: false }
            ]);
            
            const result = classifier.classify('special offer 50% off');
            expect(typeof result.isSpam).toBe('boolean');
        });
    });

    describe('Performance Tests', () => {
        test('should handle large vocabulary efficiently', () => {
            const largeMessages = [];
            for (let i = 0; i < 100; i++) {
                largeMessages.push({
                    message: `unique word${i} common word`,
                    isSpam: i < 50
                });
            }
            
            const start = Date.now();
            const classifier = new NaiveBayesClassifier();
            classifier.train(largeMessages);
            const result = classifier.classify('unique word50 common word');
            const duration = Date.now() - start;
            
            expect(typeof result.isSpam).toBe('boolean');
            expect(duration).toBeLessThan(2000); // Should complete within 2 seconds
        });
    });

    describe('Probability Calculations', () => {
        test('should maintain probability constraints', () => {
            const classifier = new NaiveBayesClassifier();
            classifier.train([
                { message: 'spam spam spam', isSpam: true },
                { message: 'ham ham ham', isSpam: false }
            ]);
            
            const result = classifier.classify('spam ham');
            
            expect(result.spamProbability).toBeGreaterThanOrEqual(0);
            expect(result.spamProbability).toBeLessThanOrEqual(1);
            expect(result.hamProbability).toBeGreaterThanOrEqual(0);
            expect(result.hamProbability).toBeLessThanOrEqual(1);
            expect(result.spamProbability + result.hamProbability).toBeCloseTo(1, 10);
        });

        test('should handle zero probability cases with smoothing', () => {
            const classifier = new NaiveBayesClassifier(0.5);
            classifier.train([
                { message: 'only spam words', isSpam: true },
                { message: 'only ham words', isSpam: false }
            ]);
            
            // Test with word that only appears in spam
            const result = classifier.classify('only spam words unknown');
            expect(result.spamProbability).toBeGreaterThan(0);
            expect(result.hamProbability).toBeGreaterThan(0);
        });
    });
});
