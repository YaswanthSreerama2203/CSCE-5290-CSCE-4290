import re
def match_tag(string):
    pattern = r"<[/a-z]+>"
    match = re.findall(pattern, string)
    if match:
        print("Tags Matched",match)
    else:
        return None