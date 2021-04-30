'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]
random_list = [36, 99, 0, 1.5]


def stats(number_list):
  min_val = min(number_list)
  max_val = max(number_list)
  sum_val = sum(number_list)
  avg_val = sum(number_list) / len(number_list)
  print(f"Minimum value is: {min_val}")
  print(f"Maximum value is: {max_val}")
  print(f"Sum equals: {sum_val} ")
  print(f"Average value is: {avg_val}")


stats(example_list)
stats(random_list)

