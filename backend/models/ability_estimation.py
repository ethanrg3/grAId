# Implements ability estimation methods using Multidimensional IRT (MIRT) principles

import numpy as np
from scipy.stats import multivariate_normal, norm
from scipy.optimize import minimize

def likelihood(theta, responses, items):
    """
    Compute the negative log-likelihood for MIRT MLE.
    """
    log_likelihood = 0
    for i, response in enumerate(responses):
        a, b, c = items[i]
        P = c + (1 - c) / (1 + np.exp(-np.dot(-a, theta - b))) # Multi-dimensional 3PL probability function
        log_likelihood += np.log(P) if response == 1 else np.log(1 - P) # Add to log-likehood the log probability of the response
    return -log_likelihood

def mle_estimation(responses, items, dim=2):
    """
    Maximum Likelihood Estimation (MLE) for MIRT ability estimation.
    """
    theta_init = np.zeros(dim) # Start with zero ability vector (initial guess for minimize function)
    result = minimize(likelihood, theta_init, args=(responses, items), method="BFGS") # Optimize the negative log-likelihood function
    return result.x if result.success else None # Return the ability vector if optimization was successful

def map_estimation(responses, items, prior_mu=None, prior_sigma=None):
    """
    Maximum A Posteriori (MAP) Estimation with a normal prior in MIRT.
    """
    if prior_mu is None:
        prior_mu = np.zeros(len(items[0][0])) # Default prior mean is zero for all ability dimensions
    if prior_sigma is None:
        prior_sigma = np.eye(len(items[0][0])) # Default prior covariance is the identity matrix
    
    def posterior(theta):
        """
        Compute the negative log-posterior for MAP estimation.
        """
        log_prior = multivariate_normal.logpdf(theta, prior_mu, prior_sigma) # Compute the log prior probability of the ability vector
        return likelihood(theta, responses, items) - log_prior # Return the negative log-posterior
    
    result = minimize(posterior, prior_mu, method='BFGS')
    return result.x if result.success else None

def eap_estimation(responses, items, prior_mu=None, prior_sigma=None, num_samples=1000):
    """
    Expected A Posteriori (EAP) Estimation for MIRT.
    """
    dim = len(items[0][0]) # Length of the discrimination vector (a) == number of ability dimensions
    if prior_mu is None:
        prior_mu = np.zeros(dim) # Default prior mean is zero for all ability dimensions
    if prior_sigma is None:
        prior_sigma = np.eye(dim) # Default prior covariance is the identity matrix

    thetas = np.random.multivariate_normal(prior_mu, prior_sigma, num_samples) # Sample ability vectors from the prior distribution
    posteriors = np.exp(-np.array([likelihood(theta, responses, items) for theta in thetas])) # Compute the posterior probability for each sample
    weights = posteriors / np.sum(posteriors) # Normalize the posterior probabilities to get weights
    return np.sum(thetas * weights[:, np.newaxis], axis=0) # Return the weighted sum of the ability vectors


if __name__ == "__main__":
    # Test the ability estimation methods
    responses = [1, 0, 1, 0, 1]
    items = [(np.array([1, 0]), 0, 0.2), (np.array([0, 1]), 0, 0.3), 
             (np.array([1, 1]), 0, 0.4), (np.array([1, 1]), 0, 0.5), 
             (np.array([1, 1]), 0, 0.6)]
    theta_mle = mle_estimation(responses, items)
    theta_map = map_estimation(responses, items)
    theta_eap = eap_estimation(responses, items)
    print("MLE:", theta_mle)
    print("MAP:", theta_map)
    print("EAP:", theta_eap)