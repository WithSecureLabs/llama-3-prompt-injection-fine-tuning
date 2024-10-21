import json
import random

def combine_jsonl_with_text(email_file, text_file, output_file):
  with open(email_file, 'r') as email_file, open(text_file, 'r') as text_file, open(output_file, 'w') as output_file:
    email_lines = email_file.readlines()
    text_lines = text_file.readlines()

    for email_line in email_lines:
      email_data = json.loads(email_line.strip())
      original_context = email_data['context']

      if random.random() <1/8:
        for text_line in text_lines:
          if random.random() <1/16:
            new_email = email_data.copy()
            new_email['context'] += text_line.strip()
            json.dump(new_email, output_file, ensure_ascii=False)
            output_file.write('\n')

          elif random.random() <1/16:
            new_email = email_data.copy()
            new_email['context'] += "\n\n" + text_line.strip()
            json.dump(new_email, output_file, ensure_ascii=False)
            output_file.write('\n')

          elif random.random() <1/16:
            new_email = email_data.copy()
            insert_index = random.randint(0, len(original_context))
            new_email['context'] += text_line.strip()
            new_email['context'] = original_context[:insert_index] + text_line.strip() + original_context[insert_index:]
            json.dump(new_email, output_file, ensure_ascii=False)
            output_file.write('\n')
      else:
        json.dump(email_data, output_file, ensure_ascii=False)
        output_file.write('\n')

if __name__ == '__main__':
  email_file = 'emails.jsonl'
  text_file = 'output.txt'
  output_file = 'dataset.jsonl'
  combine_jsonl_with_text(email_file, text_file, output_file)