from sentence_transformers import SentenceTransformer


# ==========================================
# Singleton Model Instance
# ==========================================

_model = None


def get_model():
    """
    Lazily loads and returns the Sentence Transformer model.

    The model is loaded only once and reused for the
    lifetime of the application.
    """

    global _model

    if _model is None:

        _model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    return _model


def embed_text(text):
    """
    Generate an embedding for a single piece of text.

    Parameters
    ----------
    text : str

    Returns
    -------
    numpy.ndarray
    """

    model = get_model()

    embedding = model.encode(
        text,
        convert_to_numpy=True
    )

    return embedding


def embed_texts(texts):
    """
    Generate embeddings for multiple texts.

    Parameters
    ----------
    texts : list[str]

    Returns
    -------
    numpy.ndarray
    """

    model = get_model()

    embeddings = model.encode(
        texts,
        convert_to_numpy=True
    )

    return embeddings