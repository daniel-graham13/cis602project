# Python Calculator

This application is a web-based calculator built using FastAPI (backend) and HTML/JavaScript (frontend). It is stateless and does not use a database. The data model focuses on request/response interactions and internal expression evaluation.

## Project layout

    calculator.py       # fastapi backend logic
    docs/               # documentation via mkdocs
    ├── datamodel.md    # documentation for the whole project
    ├── index.md        # documentation home page
    └── testing.md      # documentation for testing
    index.html          # calculator frontend ui
    mkdocs.yml          # configuration for mkdocs
    requirements.txt    # python dependencies
    tests/              # test case files
    ├── blackbox.py     # black box testing
    └── whitebox.py     # white box testing

