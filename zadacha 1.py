def generate_combinations(word):
  """
  Генерира всички възможни комбинации от букви от дадена дума.

  Args:
    word: Думата, от която да се генерират комбинациите.

  Returns:
    Едномерен масив, съдържащ всички възможни комбинации от букви.
  """

  combinations = []
  for i in range(len(word)):
    for j in range(i, len(word)):
      combination = word[i:j + 1]
      combinations.append(combination)
  return combinations


def main():
  word = "Python"
  combinations = generate_combinations(word)
  for combination in combinations:
    print(combination)


if __name__ == "__main__":
  main()
