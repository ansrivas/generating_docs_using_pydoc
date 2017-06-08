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
