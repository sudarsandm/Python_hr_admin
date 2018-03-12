import argparse

def create_parser():
    parser = argparse.ArgumentParser(description="""
    Human Resource module implemented for employees.
    """)
    parser.add_argument('--export',
            action='store_true',
            help='export current settings to inventory file')
    parser.add_argument('path', help='path for the inventory file(JSON)')
    return parser
