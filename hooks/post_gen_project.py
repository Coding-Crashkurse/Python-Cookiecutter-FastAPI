# cat post_gen_project.py
import os
import shutil

print(os.getcwd())  # prints /absolute/path/to/{{cookiecutter.project_slug}}

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

create_readme = '{{cookiecutter.create_readme}}' == 'y'
create_file_one = '{{cookiecutter.create_file_one}}' == 'y'
create_file_two = '{{cookiecutter.create_file_two}}' == 'y'

if not create_readme:
    # remove top-level file inside the generated folder
    remove('README.md')

if not create_file_one:
    # remove absolute path to file nested inside the generated folder
    remove(os.path.join(os.getcwd(), '{{cookiecutter.package_name}}', 'file_one.py'))

if not create_file_two:
    # remove relative file nested inside the generated folder
    remove(os.path.join('{{cookiecutter.package_name}}', 'file_two.py'))