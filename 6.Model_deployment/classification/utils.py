import pickle


def load_pipeline(path: str):
    """
    This is a helper function to load the pipeline artefacts.
    """
    with open(path, "rb") as f:
        return pickle.load(f)
