#pragma once

#include <cmath>
#include <string>
#include <vector>
#include <random>

// Error function and normal distribution
double erf(double x);
double uniform_pdf(double x, double a = 0, double b = 1);
double uniform_cdf(double x, double a = 0, double b = 1);
double normal_pdf(double x, double mu = 0, double sigma = 1);
double normal_cdf(double x, double mu = 0.0, double sigma = 1.0);
double inverse_normal_cdf(double p, double mu = 0, double sigma = 1, double tolerance = 1e-05);

// Random functions
std::string random_choice(const std::vector<std::string>& choices);
std::string random_kid();
double random_normal();

// Probability distributions
int bernoulli_trial(double p);
int binomial(double p, int n);