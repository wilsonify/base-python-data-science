#include <vector>
#include <string>

class NaiveBayesClassifier
{
public:
    NaiveBayesClassifier(double k = 0.5);
    void train(const std::vector<std::pair<std::string, bool>>& training_set);
    double classify(const std::string& message);

private:
    double k;
    std::vector<std::tuple<std::string, double, double>> word_probs;
};

