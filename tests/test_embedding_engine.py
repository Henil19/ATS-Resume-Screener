from utils.embedding_engine import (
    embed_text,
    embed_texts
)


def test_single_embedding():
    """
    Test single sentence embedding.
    """

    embedding = embed_text(
        "Python Machine Learning"
    )

    assert embedding is not None

    assert len(
        embedding.shape
    ) == 1

    assert embedding.shape[0] > 0

    print(
        "[PASS] Single Embedding"
    )


def test_batch_embeddings():
    """
    Test batch embeddings.
    """

    embeddings = embed_texts(

        [
            "Python",
            "Machine Learning",
            "Docker"
        ]

    )

    assert embeddings is not None

    assert len(
        embeddings.shape
    ) == 2

    assert embeddings.shape[0] == 3

    print(
        "[PASS] Batch Embeddings"
    )


def main():

    print("=" * 50)

    print(
        "Embedding Engine Tests"
    )

    print("=" * 50)

    test_single_embedding()

    test_batch_embeddings()

    print()

    print(
        "Embedding Engine Passed"
    )


if __name__ == "__main__":

    main()