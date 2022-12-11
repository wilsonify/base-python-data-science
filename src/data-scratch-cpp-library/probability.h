import math
import random


double random_normal() ;

double random_kid() ;

double uniform_pdf(x, a=0, b=1) ;

double uniform_cdf(x, a=0, b=1) ;

double normal_pdf(x, mu=0, sigma=1) ;

double normal_cdf(x, mu=0.0, sigma=1.0) ;

double inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001) ;
double bernoulli_trial(p) ;

double binomial(p, n) ;

def mysqrt(x: float) -> float:  // noqa: E501
    /*  square root  */
    return math.sqrt(x)
}

def mystrength(actual: float, expected: float) -> float:  // noqa: E501
    /*  signal strength  */
    eps = 0.001
    strength = actual / (expected + eps)
    return strength
}