import os
import sys

from css_parser import CssParser
from css_parser import CssRuleset
from css_parser import CssRule

print("CSS Override Remover")

if len(sys.argv) < 3:
    print("ERROR: Less than 2 arguments detected. Exiting.")
    sys.exit(1)

if not os.path.exists(sys.argv[1]):
    print("ERROR: CSS file %s not found. Exiting." % sys.argv[1])
    sys.exit(1)

if not os.path.exists(sys.argv[2]):
    print("ERROR: CSS file %s not found. Exiting." % sys.argv[2])
    sys.exit(1)

css_path_1 = sys.argv[1]
with open(css_path_1, 'r') as css_file_handle_1:
    css_string_1 = css_file_handle_1.read()

css_path_2 = sys.argv[2]
with open(css_path_2, 'r') as css_file_handle_2:
    css_string_2 = css_file_handle_2.read()

parser = CssParser()

css_parsed_1 = parser.parse_string(css_string_1)
css_parsed_2 = parser.parse_string(css_string_2)

print("Exiting")
