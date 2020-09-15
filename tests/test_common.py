__version__ = "v20200915"
# Removal of some weird randomness in PyPDF2 Export
def cleanup(file):
    return str(file).replace("/PDF /Text", "").replace("/Text /PDF", "")
