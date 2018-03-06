from models.constants import monitored_applications
import os


def app_to_keyword(app):
    return monitored_applications[app][1]


def app_to_name(app):
    return monitored_applications[app][0]


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
    e = '-execute \"{}\"'.format(command) if command else '' # THIS COMMAND MUST BE SURROUNDED BY \"
    print(m, t, s, e)
    os.system('terminal-notifier {}'.format(' '.join([i, t, s, m, e])))


def open_many_files(files):
    cwd = os.getcwd()
    for file in files:
        os.system('open {}'.format(os.path.join(str(cwd), 'Documents/', file)))


def contains(file, keyword):
    with open(os.path.join(str(os.getcwd()), 'Documents/', file), 'r') as f:
        return keyword in f.read()


def get_documents():
    return os.listdir(os.path.join(str(os.getcwd()), 'Documents/'))


def check_files(keyword):
    files = get_documents()
    return [f for f in files if f != '.DS_Store' and contains(f, keyword)]


def generate_open_files_command(files):
    pathed_files = [str(os.getcwd()) + '/Documents/' + file for file in files]
    return 'open {}'.format(' '.join(pathed_files))
