# This entrypoint file to be used in development. Start by reading README.md
import prob_calculator
from unittest import main

# hat = prob_calculator.Hat(blue=2, green=2)
# print(hat.draw(20))

# probability = prob_calculator.experiment(
#     hat=hat,
#     expected_balls={"blue": 1,
#                     "green": 1},
#     num_balls_drawn=2,
#     num_experiments=2)
# print("Probability:", probability)

# Run unit tests automatically
main(module='test_module', exit=False)
