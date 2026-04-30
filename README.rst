====================
How to build locally
====================

    #
    # First time only
    #
    python -m venv .venv

    #
    # Begin session
    #
    . .venv/bin/activate
    # If needed:
    pip install -r requirements.txt
    cd docs/
    make html
    # Then open: _build/html/index.html

    #
    # End session
    #
    deactivate
