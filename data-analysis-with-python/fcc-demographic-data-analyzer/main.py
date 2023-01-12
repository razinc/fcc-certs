# import pandas as pd
# import numpy as np

# data = pd.read_csv("adult.data.csv")
# # print(data.head())

# data = data[["education", "education-num", "marital-status"]]
# # print(data.head())

# predict = "education"
# x = np.array(data.drop([predict], 1))
# # print(x)

# y = np.array(data[predict])
# # print(y)

# z = data.drop([predict], axis = 1)
# print(z)

# # This entrypoint file to be used in development. Start by reading README.md
# import demographic_data_analyzer
# from unittest import main


# # Run unit tests automatically
# main(module='test_module', exit=False)


# This entrypoint file to be used in development. Start by reading README.md
import demographic_data_analyzer
from unittest import main

# Test your function by calling it here
demographic_data_analyzer.calculate_demographic_data()

# Run unit tests automatically
main(module='test_module', exit=False)