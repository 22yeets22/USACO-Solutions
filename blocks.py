def count(string):
  occurances = [0] * 26
  for char in string:
    occurances[ord(char) - ord('a')] += 1
  return occurances


with open('blocks.in', 'r') as fin, open('blocks.out', 'w') as fout:
  board_count = int(fin.readline())
  letters_required = [0] * 26
  for _ in range(board_count):
    word1_count, word2_count = map(count, fin.readline().split())  # Count the occurances in both words

    # Find the max letter count in both words in these two lists
    for letter_required, letter1_count, letter2_count in zip(letters_required, word1_count, word2_count):
      letter_required += max(letter1_count, letter2_count)
      
  fout.write('\n'.join(letters_required))  # Write result to file