import numpy as np

def select_next_item(theta, item_bank, asked_items):
    """
    Select the next question based on maximum Fisher information across multiple dimensions.
    We want to select the item that maximizes the Fisher information, which is the expected value of the negative Hessian of the log-likelihood function. 
    The Fisher information is a measure of how much information an item provides about the student's ability. 
    The more information an item provides, the better it is at discriminating between students with different abilities (more personalized/targeted).

    Parameters:
    - theta (np array): Current ability estimate vector for the student.
    - item_bank (list of tuples): List of item parameters (a, b, c) for each item.
    - asked_items (list of ints): List of indices of items that have already been asked.

    Returns:
    - int: Index of the next best question to ask.  
    """
    best_item = None
    best_info = -np.inf # Initialize best information to negative infinity
    for i, (a, b, c) in enumerate(item_bank):
        if i in asked_items:
            continue # Skip items that have already been asked
        
        P = c + (1 - c) / (1 + np.exp(-np.dot(-a, theta - b))) # Compute response probability for the item
        Q = 1 - P # Compute the complementary probability
        info = np.dot(a, a) * P * Q # Compute the Fisher information for the item (notice P * Q is maximized when P = Q = 0.5 or 50/50 chance)

        if info > best_info:
            best_item = i
            best_info = info

    return best_item

    # Takeaway: Fisher Information is highest when a student has a 50/50 chance of getting a question right! 
    # This is why adaptive testing keeps students "on edge" with challenging but fair questions.

def retest_missed_items(responses, items, asked_items, alternate_items):
    