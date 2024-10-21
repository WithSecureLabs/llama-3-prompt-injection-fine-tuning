import json
import openpyxl

def convert_jsonl_to_excel(jsonl_file, excel_file):
  wb = openpyxl.Workbook()
  sheet = wb.active
  sheet.append(["Prompt", "Base Model Answer", "Original Canary Detected", "Tuned Model Answer", "Tuned Canary Detected"])

  with open(jsonl_file, 'r') as f:
    for line in f:
      data = json.loads(line)
      prompt = data["prompt"]
      base_model_answer = data["base_model_answer"]
      original_canary_detected = data["original_model_canary_detected"]
      tuned_model_answer = data["tuned_model_answer"]
      tuned_canary_detected = data["tuned_model_canary_detected"]
      sheet.append([prompt, base_model_answer, original_canary_detected, tuned_model_answer, tuned_canary_detected])

  wb.save(excel_file)

jsonl_file = "output.jsonl"
excel_file = "processed_emails.xlsx"

convert_jsonl_to_excel(jsonl_file, excel_file)

print(f"successfully converted {jsonl_file} to {excel_file}")