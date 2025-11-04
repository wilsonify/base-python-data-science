import {
    erf,
    normal_cdf,
    inverse_normal_cdf,
    bernoulli_trial,
    binomial,
    binomial_distribution,
    normal_probability_below,
    normal_probability_above,
    normal_probability_between,
    normal_upper_bound,
    normal_lower_bound,
    normal_two_sided_bounds
} from '../ts-data-scratch/probability';

describe('Probability Functions', () => {
    describe('Error Function', () => {
        test('erf should calculate error function correctly', () => {
            expect(erf(0)).toBeCloseTo(0, 6);
            expect(erf(1)).toBeCloseTo(0.8427, 4);
            expect(erf(-1)).toBeCloseTo(-0.8427, 4);
            expect(erf(2)).toBeCloseTo(0.9953, 4);
            expect(erf(-2)).toBeCloseTo(-0.9953, 4);
        });

        test('erf should handle large values', () => {
            expect(erf(10)).toBeGreaterThan(0.9999);
            expect(erf(-10)).toBeLessThan(-0.9999);
        });

        test('erf should be odd function', () => {
            const x = 1.5;
            expect(erf(-x)).toBeCloseTo(-erf(x), 6);
        });

        test('erf should approach 1 and -1 asymptotically', () => {
            expect(erf(5)).toBeLessThan(1);
            expect(erf(5)).toBeGreaterThan(0.999);
            expect(erf(-5)).toBeGreaterThan(-1);
            expect(erf(-5)).toBeLessThan(-0.999);
        });
    });

    describe('Normal Distribution', () => {
        test('normal_cdf should calculate cumulative distribution function', () => {
            expect(normal_cdf(0, 0, 1)).toBeCloseTo(0.5, 4);
            expect(normal_cdf(1, 0, 1)).toBeCloseTo(0.8413, 4);
            expect(normal_cdf(-1, 0, 1)).toBeCloseTo(0.1587, 4);
            expect(normal_cdf(2, 0, 1)).toBeCloseTo(0.9772, 4);
        });

        test('normal_cdf should handle different means', () => {
            expect(normal_cdf(5, 5, 1)).toBeCloseTo(0.5, 4);
            expect(normal_cdf(6, 5, 1)).toBeCloseTo(0.8413, 4);
            expect(normal_cdf(4, 5, 1)).toBeCloseTo(0.1587, 4);
        });

        test('normal_cdf should handle different standard deviations', () => {
            expect(normal_cdf(1, 0, 2)).toBeCloseTo(0.6915, 4);
            expect(normal_cdf(2, 0, 2)).toBeCloseTo(0.8413, 4);
        });

        test('inverse_normal_cdf should calculate inverse CDF', () => {
            expect(inverse_normal_cdf(0.5, 0, 1)).toBeCloseTo(0, 4);
            expect(inverse_normal_cdf(0.8413, 0, 1)).toBeCloseTo(1, 3);
            expect(inverse_normal_cdf(0.1587, 0, 1)).toBeCloseTo(-1, 3);
        });

        test('inverse_normal_cdf should handle different parameters', () => {
            expect(inverse_normal_cdf(0.5, 5, 2)).toBeCloseTo(5, 4);
            expect(inverse_normal_cdf(0.8413, 5, 2)).toBeCloseTo(7, 3);
        });

        test('inverse_normal_cdf should handle edge probabilities', () => {
            expect(inverse_normal_cdf(0.001, 0, 1)).toBeLessThan(-3);
            expect(inverse_normal_cdf(0.999, 0, 1)).toBeGreaterThan(3);
        });

        test('normal_cdf and inverse_normal_cdf should be inverses', () => {
            const x = 1.5;
            const p = normal_cdf(x, 0, 1);
            const x_recovered = inverse_normal_cdf(p, 0, 1);
            expect(x_recovered).toBeCloseTo(x, 3);
        });
    });

    describe('Normal Probability Functions', () => {
        test('normal_probability_below should calculate P(X < x)', () => {
            expect(normal_probability_below(0, 0, 1)).toBeCloseTo(0.5, 4);
            expect(normal_probability_below(1, 0, 1)).toBeCloseTo(0.8413, 4);
        });

        test('normal_probability_above should calculate P(X > x)', () => {
            expect(normal_probability_above(0, 0, 1)).toBeCloseTo(0.5, 4);
            expect(normal_probability_above(1, 0, 1)).toBeCloseTo(0.1587, 4);
        });

        test('normal_probability_between should calculate P(a < X < b)', () => {
            expect(normal_probability_between(-1, 1, 0, 1)).toBeCloseTo(0.6826, 4);
            expect(normal_probability_between(-2, 2, 0, 1)).toBeCloseTo(0.9545, 4);
        });

        test('normal_upper_bound should find upper bound for probability', () => {
            const bound = normal_upper_bound(0.95, 0, 1);
            expect(normal_probability_below(bound, 0, 1)).toBeCloseTo(0.95, 3);
        });

        test('normal_lower_bound should find lower bound for probability', () => {
            const bound = normal_lower_bound(0.95, 0, 1);
            expect(normal_probability_above(bound, 0, 1)).toBeCloseTo(0.95, 3);
        });

        test('normal_two_sided_bounds should find symmetric bounds', () => {
            const [lower, upper] = normal_two_sided_bounds(0.95, 0, 1);
            const prob = normal_probability_between(lower, upper, 0, 1);
            expect(prob).toBeCloseTo(0.95, 3);
            expect(Math.abs(lower)).toBeCloseTo(Math.abs(upper), 6);
        });
    });

    describe('Binomial Distribution', () => {
        test('bernoulli_trial should return 0 or 1', () => {
            const trial = bernoulli_trial(0.5);
            expect([0, 1]).toContain(trial);
        });

        test('bernoulli_trial should respect probability', () => {
            // Test with p = 0 (always 0)
            for (let i = 0; i < 100; i++) {
                expect(bernoulli_trial(0)).toBe(0);
            }
            
            // Test with p = 1 (always 1)
            for (let i = 0; i < 100; i++) {
                expect(bernoulli_trial(1)).toBe(1);
            }
        });

        test('binomial should count successes in trials', () => {
            // With p = 0, should always return 0
            expect(binomial(100, 0)).toBe(0);
            
            // With p = 1, should always return n
            expect(binomial(50, 1)).toBe(50);
        });

        test('binomial should handle edge cases', () => {
            expect(binomial(0, 0.5)).toBe(0);
            expect(binomial(1, 0.5)).toBeGreaterThanOrEqual(0);
            expect(binomial(1, 0.5)).toBeLessThanOrEqual(1);
        });

        test('binomial_distribution should return probability mass function', () => {
            const pmf = binomial_distribution(10, 0.5);
            expect(pmf).toHaveLength(11); // 0 to 10 successes
            
            // Probabilities should sum to 1
            const sum = pmf.reduce((a, b) => a + b, 0);
            expect(sum).toBeCloseTo(1, 6);
            
            // All probabilities should be between 0 and 1
            pmf.forEach(p => {
                expect(p).toBeGreaterThanOrEqual(0);
                expect(p).toBeLessThanOrEqual(1);
            });
        });

        test('binomial_distribution should handle edge probabilities', () => {
            const pmf0 = binomial_distribution(5, 0);
            expect(pmf0[0]).toBeCloseTo(1, 6);
            expect(pmf0[5]).toBeCloseTo(0, 6);
            
            const pmf1 = binomial_distribution(5, 1);
            expect(pmf1[0]).toBeCloseTo(0, 6);
            expect(pmf1[5]).toBeCloseTo(1, 6);
        });

        test('binomial_distribution should handle single trial', () => {
            const pmf = binomial_distribution(1, 0.7);
            expect(pmf).toHaveLength(2);
            expect(pmf[0]).toBeCloseTo(0.3, 6);
            expect(pmf[1]).toBeCloseTo(0.7, 6);
        });
    });

    describe('Statistical Properties', () => {
        test('normal probabilities should sum correctly', () => {
            const p_below = normal_probability_below(1, 0, 1);
            const p_above = normal_probability_above(1, 0, 1);
            expect(p_below + p_above).toBeCloseTo(1, 6);
        });

        test('normal bounds should be symmetric for two-sided case', () => {
            const [lower, upper] = normal_two_sided_bounds(0.9, 0, 1);
            const prob_lower = normal_probability_below(lower, 0, 1);
            const prob_upper = normal_probability_above(upper, 0, 1);
            
            expect(prob_lower).toBeCloseTo(prob_upper, 4);
            expect(lower).toBeLessThan(0);
            expect(upper).toBeGreaterThan(0);
        });

        test('binomial distribution should have correct mean', () => {
            const n = 10;
            const p = 0.3;
            const pmf = binomial_distribution(n, p);
            
            // Calculate expected value
            let expected = 0;
            for (let k = 0; k <= n; k++) {
                expected += k * pmf[k];
            }
            
            expect(expected).toBeCloseTo(n * p, 3);
        });

        test('binomial distribution should have correct variance', () => {
            const n = 10;
            const p = 0.3;
            const pmf = binomial_distribution(n, p);
            
            // Calculate variance
            let expected = 0;
            let expected_sq = 0;
            for (let k = 0; k <= n; k++) {
                expected += k * pmf[k];
                expected_sq += k * k * pmf[k];
            }
            const variance = expected_sq - expected * expected;
            
            expect(variance).toBeCloseTo(n * p * (1 - p), 3);
        });
    });

    describe('Edge Cases and Error Handling', () => {
        test('should handle invalid probability values', () => {
            expect(() => bernoulli_trial(-0.1)).toThrow();
            expect(() => bernoulli_trial(1.1)).toThrow();
        });

        test('should handle invalid normal parameters', () => {
            expect(() => normal_cdf(0, 0, 0)).toThrow(); // Zero standard deviation
            expect(() => normal_cdf(0, 0, -1)).toThrow(); // Negative standard deviation
        });

        test('should handle invalid inverse CDF probabilities', () => {
            expect(() => inverse_normal_cdf(-0.1, 0, 1)).toThrow();
            expect(() => inverse_normal_cdf(1.1, 0, 1)).toThrow();
        });

        test('should handle invalid binomial parameters', () => {
            expect(() => binomial(-1, 0.5)).toThrow();
            expect(() => binomial_distribution(-1, 0.5)).toThrow();
            expect(() => binomial_distribution(10, -0.1)).toThrow();
            expect(() => binomial_distribution(10, 1.1)).toThrow();
        });
    });

    describe('Numerical Stability', () => {
        test('should handle extreme normal values', () => {
            expect(normal_cdf(10, 0, 1)).toBeGreaterThan(0.999999);
            expect(normal_cdf(-10, 0, 1)).toBeLessThan(0.000001);
            
            expect(inverse_normal_cdf(0.999999, 0, 1)).toBeGreaterThan(4);
            expect(inverse_normal_cdf(0.000001, 0, 1)).toBeLessThan(-4);
        });

        test('should handle very small probabilities', () => {
            expect(normal_probability_above(6, 0, 1)).toBeLessThan(0.000001);
            expect(normal_probability_below(-6, 0, 1)).toBeLessThan(0.000001);
        });

        test('should handle large binomial parameters', () => {
            const pmf = binomial_distribution(100, 0.5);
            expect(pmf).toHaveLength(101);
            expect(pmf[50]).toBeGreaterThan(0.05); // Most probable outcome
        });
    });

    describe('Performance Tests', () => {
        test('should handle many calculations efficiently', () => {
            const start = Date.now();
            
            for (let i = 0; i < 1000; i++) {
                normal_cdf(i / 100, 0, 1);
                inverse_normal_cdf(0.5, 0, 1);
                binomial_distribution(10, 0.5);
            }
            
            const duration = Date.now() - start;
            expect(duration).toBeLessThan(2000); // Should complete within 2 seconds
        });

        test('should handle large binomial calculations', () => {
            const start = Date.now();
            const pmf = binomial_distribution(1000, 0.5);
            const duration = Date.now() - start;
            
            expect(pmf).toHaveLength(1001);
            expect(duration).toBeLessThan(1000); // Should complete within 1 second
        });
    });

    describe('Special Cases', () => {
        test('should handle standard normal distribution', () => {
            // Standard normal (μ=0, σ=1)
            expect(normal_cdf(1.96, 0, 1)).toBeCloseTo(0.975, 3);
            expect(normal_cdf(-1.96, 0, 1)).toBeCloseTo(0.025, 3);
            
            // 68-95-99.7 rule
            expect(normal_probability_between(-1, 1, 0, 1)).toBeCloseTo(0.6827, 3);
            expect(normal_probability_between(-2, 2, 0, 1)).toBeCloseTo(0.9545, 3);
            expect(normal_probability_between(-3, 3, 0, 1)).toBeCloseTo(0.9973, 3);
        });

        test('should handle fair coin binomial distribution', () => {
            const pmf = binomial_distribution(2, 0.5);
            expect(pmf[0]).toBeCloseTo(0.25, 6); // TT
            expect(pmf[1]).toBeCloseTo(0.5, 6);  // TH or HT
            expect(pmf[2]).toBeCloseTo(0.25, 6); // HH
        });

        test('should handle deterministic cases', () => {
            // Always success
            expect(binomial(10, 1)).toBe(10);
            
            // Always failure
            expect(binomial(10, 0)).toBe(0);
            
            // Single trial
            const single = binomial(1, 0.7);
            expect([0, 1]).toContain(single);
        });
    });

    describe('Consistency Tests', () => {
        test('normal_cdf should be monotonic increasing', () => {
            const x1 = -2, x2 = 0, x3 = 2;
            const p1 = normal_cdf(x1, 0, 1);
            const p2 = normal_cdf(x2, 0, 1);
            const p3 = normal_cdf(x3, 0, 1);
            
            expect(p1).toBeLessThan(p2);
            expect(p2).toBeLessThan(p3);
        });

        test('inverse_normal_cdf should be monotonic increasing', () => {
            const p1 = 0.1, p2 = 0.5, p3 = 0.9;
            const x1 = inverse_normal_cdf(p1, 0, 1);
            const x2 = inverse_normal_cdf(p2, 0, 1);
            const x3 = inverse_normal_cdf(p3, 0, 1);
            
            expect(x1).toBeLessThan(x2);
            expect(x2).toBeLessThan(x3);
        });

        test('binomial probabilities should be symmetric for p=0.5', () => {
            const pmf = binomial_distribution(10, 0.5);
            expect(pmf[3]).toBeCloseTo(pmf[7], 6);
            expect(pmf[2]).toBeCloseTo(pmf[8], 6);
            expect(pmf[0]).toBeCloseTo(pmf[10], 6);
        });
    });
});
