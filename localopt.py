import numpy as np

# Define the objective function (example: f(x) = x^2)
def objective_function(x):
    return x ** 2

# Define the derivative of the objective function (gradient)
def gradient(x):
    return 2 * x

# Gradient descent optimization function
def gradient_descent(learning_rate, num_iterations):
    # Initial guess
    x = 5.0
    
    for _ in range(num_iterations):
        # Compute the gradient of the objective function at the current point
        grad = gradient(x)
        
        # Update the current point using the gradient descent rule
        x -= learning_rate * grad
        
        # Print the current point and objective value
        print(f"x = {x}, f(x) = {objective_function(x)}")
    
    return x

# Set the learning rate and number of iterations
learning_rate = 0.1
num_iterations = 10

# Perform gradient descent optimization
optimal_x = gradient_descent(learning_rate, num_iterations)

print("Optimal solution:", optimal_x)
print("Optimal objective value:", objective_function(optimal_x))
