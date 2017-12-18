import os

RENAME_PATTERNS = [
    ('__project_name__', '{{cookiecutter.project_name}}'),
    ('__app_name__', '{{cookiecutter.app_name}}'),
]

IGNORE_FILES = ['rename.py', 'README.md']
IGNORE_DIRS = ['.git']


def replace(text):
    output = text
    for pattern in RENAME_PATTERNS:
        output = output.replace(pattern[0], pattern[1])
    return output, text != output


def is_ignore_dir(dirpath):
    for dir in IGNORE_DIRS:
        if dir in dirpath:
            return True
    return False


def main():
    for dirpath, dirnames, filenames in list(os.walk('.'))[:]:
        if is_ignore_dir(dirpath):
            continue

        for filename in filenames:
            fullpath = os.path.join(dirpath, filename)
            if filename in IGNORE_FILES:
                continue
            with open(fullpath, 'r') as fp:
                text = fp.read()
            text, changed = replace(text)
            if changed:
                with open(fullpath, 'w') as fp:
                    fp.write(text)

        for dirname in dirnames:
            fullpath = os.path.join(dirpath, dirname)
            new_fullpath, changed = replace(fullpath)
            if changed:
                os.rename(fullpath, new_fullpath)

        for filename in filenames:
            if filename in IGNORE_FILES:
                continue
            fullpath = os.path.join(dirpath, filename)
            new_fullpath, changed = replace(fullpath)
            if changed:
                os.rename(fullpath, new_fullpath)

if __name__ == '__main__':
    main()
