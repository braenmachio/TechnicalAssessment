import logging, os


def palindrome_logging():
    """Initializes the root logging infrastructure with file targets."""
    logging.basicConfig(
        filename=os.path.join("logs", "palindrome.log") ,
        filemode="a",
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.DEBUG,
        force=True
    )

def polymer_logging():
    logging.basicConfig(
        force=True,
        filename=os.path.join("logs", "polymer.log"),
        filemode="a",
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s ",
        level=logging.DEBUG        
        )
    pass