import os

rename_patterns = [
    ('__project_name__', '{{cookiecutter.project_name}}'),
    ('__app_name__', '{{cookiecutter.app_name}}'),
]


def replace(text):
    output = text
    for pattern in rename_patterns:
        output = output.replace(pattern[0], pattern[1])
    return output, text != output


def main():
    for dirpath, dirnames, filenames in os.walk('.'):
        for filename in filenames:
            fullpath = os.path.join(dirpath, filename)
            with open(fullpath) as fp:
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
            fullpath = os.path.join(dirpath, filename)
            new_fullpath, changed = replace(fullpath)
            if changed:
                os.rename(fullpath, new_fullpath)

if __name__ == '__main__':
    main()
