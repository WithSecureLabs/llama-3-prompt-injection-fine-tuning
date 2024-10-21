def combine_text_files(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

        for line1 in lines1:
            if "[XXX]" in line1:
                for line2 in lines2:
                    out.write(line1.replace("[XXX]", line2.strip()))
            else:
                out.write(line1)

if __name__ == '__main__':
    file1 = 'breakouts.txt'
    file2 = 'prompts.txt'
    output_file = 'output.txt'
    combine_text_files(file1, file2, output_file)