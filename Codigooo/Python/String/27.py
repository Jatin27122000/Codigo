import textwrap


given_text = """
    This is some text
    With indentation
        And more indentation
    """

dedented_text = textwrap.dedent(given_text)
print(dedented_text)
