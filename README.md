# generating_docs_using_pydoc
This repository contains a minimal example to generate docs for python projects

Create docstrings for the functions, in your python file , in our case "sample.py"

then execute this command to generate "filename.html" as the doc file

//Notice there is no extension in filename = "sample"

pydoc -w sample

--------------------------------------------

### With Sphinx:

1. `pip install sphinx sphinx_rtd_theme`

2. `mkdir docs myprojdir`

3. `cd docs`

4. `sphinx-quickstart`

5. Hit `yes` for everything and fill in the required project details.

6. Inside file `docs/source/conf.py` put these lines to include your project in python path:
    ```
    import os
    import sys
    sys.path.insert(0, os.path.abspath('../../'))
    ```

6. And then inside `docs` directory, run:
    ```
    sphinx-apidoc -f -o source/ ../myprojdir && \
    make html && \
    xdg-open build/html/index.html
    ```
    
7. To use markdown as well:

    `pip install recommonmark`
    
    and inside `conf.py`
    
    
    ```
    source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser',
    }
    source_suffix = ['.rst', '.md']
    ```
    
    And then add the markdown files inside `docs/source` we have `example.md` and `example2.md`.
    Include these two files in index.rst so that they can be parsed.
