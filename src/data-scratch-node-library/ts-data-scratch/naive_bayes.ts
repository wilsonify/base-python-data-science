// Type definitions
type LabeledMessage = { message: string; isSpam: boolean };
type WordProbabilities = Map<string, { spam: number; ham: number }>;
type ClassificationResult = {
    isSpam: boolean;
    spamProbability: number;
    hamProbability: number;
};

// Tokenize a message into words
function tokenize(message: string): string[] {
    return message.toLowerCase()
        .replace(/[^\w\s]/g, ' ') // Replace punctuation with spaces
        .split(/\s+/) // Split on whitespace
        .filter(word => word.length > 0); // Remove empty strings
}

// Count words in messages
function countWords(messages: LabeledMessage[]): {
    spamWords: Map<string, number>;
    hamWords: Map<string, number>;
    spamCount: number;
    hamCount: number;
} {
    const spamWords = new Map<string, number>();
    const hamWords = new Map<string, number>();
    let spamCount = 0;
    let hamCount = 0;

    for (const { message, isSpam } of messages) {
        const words = tokenize(message);
        
        if (isSpam) {
            spamCount++;
            for (const word of words) {
                spamWords.set(word, (spamWords.get(word) || 0) + 1);
            }
        } else {
            hamCount++;
            for (const word of words) {
                hamWords.set(word, (hamWords.get(word) || 0) + 1);
            }
        }
    }

    return { spamWords, hamWords, spamCount, hamCount };
}

// Calculate word probabilities with Laplace smoothing
function calculateWordProbabilities(
    spamWords: Map<string, number>,
    hamWords: Map<string, number>,
    spamCount: number,
    hamCount: number,
    smoothing: number = 0.5
): WordProbabilities {
    const vocab = new Set([...spamWords.keys(), ...hamWords.keys()]);
    const wordProbs = new Map<string, { spam: number; ham: number }>();

    const totalSpamWords = Array.from(spamWords.values()).reduce((a, b) => a + b, 0);
    const totalHamWords = Array.from(hamWords.values()).reduce((a, b) => a + b, 0);

    for (const word of vocab) {
        const spamWordCount = spamWords.get(word) || 0;
        const hamWordCount = hamWords.get(word) || 0;

        // Apply Laplace smoothing
        const spamProb = (spamWordCount + smoothing) / (totalSpamWords + smoothing * vocab.size);
        const hamProb = (hamWordCount + smoothing) / (totalHamWords + smoothing * vocab.size);

        wordProbs.set(word, { spam: spamProb, ham: hamProb });
    }

    return wordProbs;
}

// Naive Bayes classifier class
export class NaiveBayesClassifier {
    private wordProbs: WordProbabilities = new Map();
    private spamPrior: number = 0;
    private hamPrior: number = 0;
    private smoothing: number = 0.5;
    private isTrained: boolean = false;

    constructor(smoothing: number = 0.5) {
        this.smoothing = smoothing;
    }

    // Train the classifier
    train(messages: LabeledMessage[]): void {
        const { spamWords, hamWords, spamCount, hamCount } = countWords(messages);
        
        this.wordProbs = calculateWordProbabilities(
            spamWords, hamWords, spamCount, hamCount, this.smoothing
        );
        
        const totalMessages = messages.length;
        this.spamPrior = spamCount / totalMessages;
        this.hamPrior = hamCount / totalMessages;
        
        this.isTrained = true;
    }

    // Classify a single message
    classify(message: string): ClassificationResult {
        if (!this.isTrained) {
            throw new Error('Classifier must be trained before classification');
        }

        const words = tokenize(message);
        let logSpamProb = Math.log(this.spamPrior);
        let logHamProb = Math.log(this.hamPrior);

        for (const word of words) {
            const probs = this.wordProbs.get(word);
            if (probs) {
                logSpamProb += Math.log(probs.spam);
                logHamProb += Math.log(probs.ham);
            } else {
                // Handle unknown words with smoothing
                const vocabSize = this.wordProbs.size;
                const unknownProb = this.smoothing / (this.smoothing * vocabSize);
                logSpamProb += Math.log(unknownProb);
                logHamProb += Math.log(unknownProb);
            }
        }

        // Convert back from log probabilities
        const spamProb = Math.exp(logSpamProb);
        const hamProb = Math.exp(logHamProb);
        const totalProb = spamProb + hamProb;

        // Normalize
        const normalizedSpamProb = spamProb / totalProb;
        const normalizedHamProb = hamProb / totalProb;

        return {
            isSpam: normalizedSpamProb > normalizedHamProb,
            spamProbability: normalizedSpamProb,
            hamProbability: normalizedHamProb
        };
    }

    // Get training information
    getTrainingInfo(): {
        vocabSize: number;
        spamPrior: number;
        hamPrior: number;
        smoothing: number;
        isTrained: boolean;
    } {
        return {
            vocabSize: this.wordProbs.size,
            spamPrior: this.spamPrior,
            hamPrior: this.hamPrior,
            smoothing: this.smoothing,
            isTrained: this.isTrained
        };
    }

    // Get word probabilities
    getWordProbabilities(): WordProbabilities {
        return new Map(this.wordProbs);
    }
}

// Convenience function for training and classification
export function trainNaiveBayesClassifier(
    messages: LabeledMessage[],
    smoothing: number = 0.5
): NaiveBayesClassifier {
    const classifier = new NaiveBayesClassifier(smoothing);
    classifier.train(messages);
    return classifier;
}

// Classify a message without creating a classifier instance
export function classifyMessage(
    message: string,
    trainingMessages: LabeledMessage[],
    smoothing: number = 0.5
): ClassificationResult {
    const classifier = trainNaiveBayesClassifier(trainingMessages, smoothing);
    return classifier.classify(message);
}

// Cross-validation for Naive Bayes
export function naiveBayesCrossValidate(
    messages: LabeledMessage[],
    folds: number = 5,
    smoothing: number = 0.5
): number {
    // Shuffle the messages
    const shuffled = [...messages].sort(() => Math.random() - 0.5);
    const foldSize = Math.floor(shuffled.length / folds);
    let correctPredictions = 0;

    for (let i = 0; i < folds; i++) {
        // Create train/test split for this fold
        const testStart = i * foldSize;
        const testEnd = (i + 1) * foldSize;

        const testSet = shuffled.slice(testStart, testEnd);
        const trainSet = [
            ...shuffled.slice(0, testStart),
            ...shuffled.slice(testEnd)
        ];

        // Train and test
        const classifier = new NaiveBayesClassifier(smoothing);
        classifier.train(trainSet);

        for (const testMessage of testSet) {
            const result = classifier.classify(testMessage.message);
            const predictedIsSpam = result.isSpam;
            const actualIsSpam = testMessage.isSpam;

            if (predictedIsSpam === actualIsSpam) {
                correctPredictions++;
            }
        }
    }

    return correctPredictions / shuffled.length;
}

// Example training data
export const exampleMessages: LabeledMessage[] = [
    { message: "buy viagra now", isSpam: true },
    { message: "cheap pills online", isSpam: true },
    { message: "limited time offer", isSpam: true },
    { message: "click here for free money", isSpam: true },
    { message: "hello friend", isSpam: false },
    { message: "how are you today", isSpam: false },
    { message: "meeting at 3pm", isSpam: false },
    { message: "project deadline tomorrow", isSpam: false },
    { message: "congratulations you won", isSpam: true },
    { message: "lunch plans", isSpam: false }
];

// Example usage
export function exampleUsage(): void {
    const classifier = new NaiveBayesClassifier();
    classifier.train(exampleMessages);

    const testMessages = [
        "buy cheap viagra now",
        "hello my friend",
        "limited offer free money",
        "meeting tomorrow at 3pm"
    ];

    console.log("Naive Bayes Classification Examples:");
    for (const message of testMessages) {
        const result = classifier.classify(message);
        console.log(`"${message}" -> ${result.isSpam ? 'SPAM' : 'HAM'}`);
        console.log(`  Spam prob: ${result.spamProbability.toFixed(4)}`);
        console.log(`  Ham prob: ${result.hamProbability.toFixed(4)}`);
    }
}
