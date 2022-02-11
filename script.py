import os
import csv

from subprocess import check_output

files = []
truth_dir = "./truth"
text_dir = "./text"
truth_files = os.listdir(truth_dir)
text_files = os.listdir(text_dir)
truth_files = sorted(truth_files)
text_files = sorted(text_files)


def get_diff(truth, text):
    # checks to make sure both files are text files
    if truth.endswith('.txt') and text.endswith('.txt'):
        print(truth, text)
        diff_out = check_output(['diffchecker', f'truth/{truth}', f'text/{text}'])
        diff_out = diff_out.decode('utf-8')
        diff_out = diff_out.split(': ')
        diff_out = diff_out[1].strip()
        return diff_out


def write_csv(results):
    with open('diffs.csv', 'w') as csvfile:
        fieldnames = ['file', 'diff']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for res in results:
            writer.writerow({
                'file': res['file'],
                'diff': res['diff']
            })


for x in range(0, len(text_files)):
    diff = get_diff(truth_files[x], text_files[x])
    files.append({'file': text_files[x], 'diff': diff})

    write_csv(files)

print("Diffs successfully created!")
