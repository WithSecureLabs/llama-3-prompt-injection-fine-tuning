def average_characters_per_line(jsonl_file):
  total_chars = 0
  line_count = 0

  with open(jsonl_file, 'r') as f:
    for line in f:
      total_chars += len(line)
      line_count += 1

  if line_count > 0:
    average_chars = total_chars / line_count
  else:
    average_chars = 0

  return average_chars, total_chars, line_count

if __name__ == "__main__":
  jsonl_file = "FormattedFinal.jsonl"
  average_length, total_characters, line_count = average_characters_per_line(jsonl_file)
  print("")
  print(f"Average no. of characters per line, total characters, line count: {average_length, total_characters, line_count}")