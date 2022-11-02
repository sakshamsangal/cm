import glob
import os


def view():
    for name in glob.glob(f'static/img/amber/*/*.jpg'):
        x = os.path.basename(name)
        os.replace(name, f'static/img/amber/{x}')


if __name__ == '__main__':
    view()
