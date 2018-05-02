import os
import random


# def app_to_keyword(app):
#     return monitored_applications[app][1]


# def app_to_name(app):
#     return monitored_applications[app][0]


def account_for_spaces(string):
    split = string.split(' ')
    fixed = split[0]
    for i in range(1,len(split)):
        fixed += '\\ ' + split[i]
    return fixed


def notify(message='default', title=None, subtitle=None, command=None):
    m = '-message \"{}\"'.format(message)
    i = '-appIcon \"{}\"'.format(str(os.path.join(str(os.getcwd()), 'assets/icon.png')))
    t = '-title \"{}\"'.format(title) if title else ''
    s = '-subtitle \"{}\"'.format(subtitle) if subtitle else ''
    e = '-execute \"{}\"'.format(command) if command else ''
    os.system('terminal-notifier {}'.format(' '.join([i, t, s, m, e])))


# def open_many_files(files):
#     cwd = os.getcwd()
#     for file in files:
#         os.system('open {}'.format(os.path.join(str(cwd), 'documents/', file)))


# def contains(file, keyword):
#     with open(os.path.join(str(os.getcwd()), 'documents/', file), 'r') as f:
#         return keyword in f.read()


def get_documents():
    return os.listdir(os.path.join(str(os.getcwd()), 'documents/'))


def check_files(application):
    files = get_documents()
    return [f for f in files if application in f]


def generate_open_files_command(files):
    pathed_files = [str(os.getcwd()) + '/documents/' + account_for_spaces(file) for file in files]
    return 'open {}'.format(' '.join(pathed_files))


def new_note(app_name, content, dirr):
    files = os.listdir(dirr + '/documents')
    file_name = app_name + '-' + str(random.randint(0, 10000)) + '.txt'
    while file_name in files:
        file_name = app_name + '-' + str(random.randint(0, 10000)) + '.txt'
    with open(dirr + '/documents/{}.txt'.format(file_name), 'w') as f:
        f.write(content)
