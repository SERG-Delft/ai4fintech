# pip install pyyaml
import yaml
from pathlib import Path


# location of ai4fintech github pages sources
afr_src = '../'
root = 'report.qmd'

def read_qmd(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
    	lines = [line.rstrip() for line in file]
    return lines

def lines_to_string(lines):
	return "\n".join(lines)

def process_qmd(lines):
    in_yaml = False
    yaml_lines = []
    content_lines = []

    for line in lines:
        stripped_line = line.strip()

        if stripped_line == '---':
            in_yaml = not in_yaml
            continue

        if in_yaml:
        	yaml_lines.append(stripped_line)
        else:
        	content_lines.append(stripped_line)

    yaml_data = process_yaml(yaml_lines)
    return (yaml_data, content_lines)

def process_yaml(yaml_lines):
    yaml_data = yaml.safe_load("\n".join(yaml_lines)) if yaml_lines else {}
    return yaml_data

def do_root():
    lines = read_qmd(root)
    print(lines_to_string(lines))

def do_intro():
    lines = read_qmd(afr_src + 'index.md')
    (yaml, content) = process_qmd(lines)
    print(lines_to_string(content))

def do_track_list():
    lines = read_qmd(afr_src + 'tracks.md')
    (yaml, content) = process_qmd(lines)
   # last 9 lines are jekyll for loop to show tracks
    print(lines_to_string(content[:-9]))

def load_qmd(file_name):
    lines = read_qmd(file_name)
    return process_qmd(lines)

def do_tracks():
    track_names = sorted(
    	[f.name
        for f in Path(afr_src + '_tracks').glob("*.md") 
        if f.is_file()
    ])
    tracks = [load_qmd(afr_src + '_tracks/' + t) for t in track_names]

    do_overview(tracks)
    do_track_content(tracks)

def do_overview(tracks):
    header = "| Id | Track title | PhD candidate | Track lead(s)"
    bar = "|-|--------|----|----|"
    print(header)
    print(bar)

    fmt = "| {} | {} | {} | {} |"
    for (yaml, content) in tracks:
        if yaml.get('inactive'):
            continue
        print(fmt.format(
        	yaml['track-id'], 
        	yaml['title'], 
        	yaml['phd'],
        	yaml['leader']
        ))

    print('\n')


def do_track_content(tracks):
    fmt_head = "\n# Track {}: {}\n"
    fmt_members = "**PhD candidate:** {}  \n**Track leader(s):** {}  \n"
    for (yaml, content) in tracks:
        if yaml.get('inactive'):
            continue
        print(fmt_head.format(yaml['track-id'], yaml['title']))
        print(fmt_members.format(yaml['phd'], yaml['leader']))
        print(lines_to_string(content))

def do_students():
    section = "\n\\newpage\n# Bachelor and Master Students\n"
    print(section)
 
    with open(afr_src + "_data/students.yml", "r") as file:
        data = yaml.safe_load(file)
 
    fmt = "1. {}. _[{}]({})_. {}. Advisors: {}"
    for student in data:
    	if student['level'] != 'PhD':
            print(fmt.format(
            	student['name'],
            	student['topic'],
                student.get('link', 'null'),
            	student['status'],
            	student['supervision']
            ))


def main():
    do_root()
    do_intro()
    do_track_list()
    do_tracks()
    do_students()

main()