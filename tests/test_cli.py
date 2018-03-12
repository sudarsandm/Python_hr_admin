import pytest

from hr import cli

@pytest.fixture()
def parser():
    return cli.create_parser()

def test_parser_without_arguments(parser):
    """
    Without a specified command line option the parser will exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args()

def test_parser_succeeds_with_a_path(parser):
    """
    With a path the parser should not exit.
    """
    args = parser.parse_args(['/some/path'])
    assert args.path == '/some/path'
    assert args.export == False

def test_parser_export_flag(parser):
    """
    The export value should default to False, but should set to True
    when passed to the parser.
    """
    args = parser.parse_args(['/some/path'])
    assert args.export == False
    assert args.path == '/some/path'

    args = parser.parse_args(['--export', '/some/path'])
    assert args.export == True
    assert args.path == '/some/path'
