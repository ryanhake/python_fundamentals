'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats():
  min_val = min(example_list)
  max_val = max(example_list)
  sum_val = sum(example_list)
  avg_val = sum(example_list) / len(example_list)
  print(f"Minimum value is: {min_val}")
  print(f"Maximum value is: {max_val}")
  print(f"Sum equals: {sum_val} ")
  print(f"Average value is: {avg_val}")


stats()

