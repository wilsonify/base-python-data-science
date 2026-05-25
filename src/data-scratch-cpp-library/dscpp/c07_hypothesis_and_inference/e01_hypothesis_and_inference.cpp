#include <iostream>
#include <random>
#include <vector>
#include "hypothesis_and_inference.h"

int main() {
    auto [mu_0, sigma_0] = normal_approximation_to_binomial(1000, 0.5);
    std::cout << "mu_0 " << mu_0 << "\n";
    std::cout << "sigma_0 " << sigma_0 << "\n";

    auto [lo, hi] = normal_two_sided_bounds(0.95, mu_0, sigma_0);
    std::cout << "normal_two_sided_bounds(0.95, mu_0, sigma_0) " << lo << " " << hi << "\n";

    std::cout << "power of a test\n";
    std::cout << "95% bounds based on assumption p is 0.5\n";
    std::cout << "lo " << lo << "\n";
    std::cout << "hi " << hi << "\n";

    auto [mu_1, sigma_1] = normal_approximation_to_binomial(1000, 0.55);
    std::cout << "mu_1 " << mu_1 << "\n";
    std::cout << "sigma_1 " << sigma_1 << "\n";

    double type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1);
    double power = 1.0 - type_2_probability;
    std::cout << "type 2 probability " << type_2_probability << "\n";
    std::cout << "power " << power << "\n";

    std::cout << "one-sided test\n";
    double hi_one = normal_upper_bound(0.95, mu_0, sigma_0);
    std::cout << "hi " << hi_one << "\n";
    type_2_probability = normal_probability_below(hi_one, mu_1, sigma_1);
    power = 1.0 - type_2_probability;
    std::cout << "type 2 probability " << type_2_probability << "\n";
    std::cout << "power " << power << "\n";

    std::cout << "two_sided_p_value(529.5, mu_0, sigma_0) "
              << two_sided_p_value(529.5, mu_0, sigma_0) << "\n";
    std::cout << "two_sided_p_value(531.5, mu_0, sigma_0) "
              << two_sided_p_value(531.5, mu_0, sigma_0) << "\n";
    std::cout << "upper_p_value(525, mu_0, sigma_0) "
              << upper_p_value(525, mu_0, sigma_0) << "\n";
    std::cout << "upper_p_value(527, mu_0, sigma_0) "
              << upper_p_value(527, mu_0, sigma_0) << "\n";

    std::cout << "P-hacking\n";
    int n_experiments = 1000;
    int num_rejections = 0;
    for (int i = 0; i < n_experiments; ++i) {
        auto exp = run_experiment();
        if (reject_fairness(exp)) ++num_rejections;
    }
    std::cout << "rejections: " << num_rejections << " out of " << n_experiments << "\n";

    std::cout << "A/B testing\n";
    double z = a_b_test_statistic(1000, 200, 1000, 180);
    std::cout << "a_b_test_statistic(1000, 200, 1000, 180) " << z << "\n";
    std::cout << "p-value " << two_sided_p_value(z) << "\n";

    z = a_b_test_statistic(1000, 200, 1000, 150);
    std::cout << "a_b_test_statistic(1000, 200, 1000, 150) " << z << "\n";
    std::cout << "p-value " << two_sided_p_value(z) << "\n";

    return 0;
}
