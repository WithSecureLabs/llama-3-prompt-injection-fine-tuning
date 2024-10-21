import json
import random

def rename_and_shuffle_jsonl(input_file, output_file):
    with open(input_file, 'r') as input_file, open(output_file, 'w') as output_file:
        data = [json.loads(line.strip()) for line in input_file]

        for item in data:
            item['text'] = f"Answer the question about: <<<data>>>{item.pop('context')}<<</data>>>"
            item['instruction'] = item.pop('question')
            item['output'] = item.pop('ideal')

        random.shuffle(data)
        for item in data:
            json.dump(item, output_file, ensure_ascii=False)
            output_file.write('\n')

if __name__ == '__main__':
    input_file = 'dataset.jsonl'
    output_file = 'datasetReady.jsonl'
    rename_and_shuffle_jsonl(input_file, output_file)