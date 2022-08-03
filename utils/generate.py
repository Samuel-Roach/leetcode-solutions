import os
import argparse
from sys import argv
from datetime import date
import shutil

def main(argv):
    source_path = os.path.dirname(__file__)

    # Parse arguments
    parser = argparse.ArgumentParser(description='Generate the default folder structure for a Leetcode solution')
    parser.add_argument('-p', '--problem', type=int, required=True, dest='problem_id',
                        help='The problem ID, as seen on the Leetcode website')
    parser.add_argument('-t', '--title',  type=str, required=False, dest='problem_title', default='',
                        help='The problems title, as given on the Leetcode website')

    args = parser.parse_args(argv)

    # Create the folder
    today = date.today()
    folder_name = f'{args.problem_id}_{today.day}-{today.month}-{today.year}'
    folder_path = os.path.join(source_path, '..', folder_name)
    os.mkdir(folder_path)

    # Copy across the python files
    shutil.copy(os.path.join(source_path, 'templates', 'run.py'), folder_path)
    shutil.copy(os.path.join(source_path, 'templates', 'solution.py'), folder_path)

    # Replace the templated elements of problem.md
    problem_template = os.path.join(source_path, 'templates', 'problem.md')
    problem_path = os.path.join(folder_path, 'problem.md')

    with open(problem_template, 'r') as template:
        with open(problem_path, 'w') as output:
            for line in template:
                added_id = line.replace('{num}', str(args.problem_id))
                added_title = added_id.replace('{title}', args.problem_title if args.problem_title != '' else 'Lorem Ipsum')
                output.write(added_title)

    with open(os.path.join(source_path, '..', 'TODO.md'), 'a') as todo:
        todo.write(f'- [ ] {args.problem_id}\n')

if __name__ == '__main__':
    main(argv[1:])