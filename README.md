# Python autodoc with Sphinx

**Comparing Python documentation approaches**

This looks at Sphinx autodoc for automatically generating API documentation from Python docstrings. Uses a coffee machine simulator program to provide a simple codebase to experiment with documentation extraction.

**See also:** [mkdocstrings approach](https://github.com/JohnA-Oslo/mkdocstrings-test) - same Python code, but using MkDocs and mkdocstrings.


## Building the Documentation
```bash
# Set up environment
python -m venv venv
venv\Scripts\activate  # Windows
pip install sphinx furo

# Build documentation
cd docs
make html

# View in browser
start build/html/index.html
```

## Technologies

- Python 3.13
- Sphinx 9.1.0
- Furo theme
- Napoleon extension for Google-style docstrings

## Source code

The coffee machine simulator is from my Python learning coursework and includes classes for:

- CoffeeMaker - Resource management and drink preparation
- MoneyMachine - Payment processing and profit tracking
- Menu/MenuItem - Menu management and drink lookup