from together.utils import check_file
report = check_file("FormattedFinal.jsonl")
print(report)
assert report["is_check_passed"] == True

#check script from https://www.together.ai/blog/finetuning using check_file function-
#from Together’s SDK to verify that our dataset is valid and in the correct format.