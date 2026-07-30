import numpy as np

from utils.embedding_engine import (
    embed_text,
    embed_texts
)


def cosine_similarity(vector_a, vector_b):
    """
    Compute cosine similarity between two vectors.
    """

    numerator = np.dot(
        vector_a,
        vector_b
    )

    denominator = (
        np.linalg.norm(vector_a)
        *
        np.linalg.norm(vector_b)
    )

    if denominator == 0:
        return 0.0

    return float(
        numerator / denominator
    )


def compute_overall_similarity(
    resume_text,
    job_text
):
    """
    Compute semantic similarity between
    an entire resume and job description.
    """

    resume_embedding = embed_text(
        resume_text
    )

    job_embedding = embed_text(
        job_text
    )

    similarity = cosine_similarity(
        resume_embedding,
        job_embedding
    )

    return round(
        similarity * 100,
        2
    )


def compute_skill_similarity(
    resume_skills,
    job_skills,
    threshold=0.70
):
    """
    Compute semantic similarity
    between resume skills and job skills.
    """

    if not resume_skills or not job_skills:

        return {
            "semantic_matches": [],
            "missing_concepts": list(job_skills)
        }

    # -----------------------------------------
    # Convert sets to sorted lists
    # SentenceTransformer expects a list.
    # Sorting provides deterministic ordering.
    # -----------------------------------------

    resume_skills = sorted(
        list(resume_skills)
    )

    job_skills = sorted(
        list(job_skills)
    )

    resume_embeddings = embed_texts(
        resume_skills
    )

    job_embeddings = embed_texts(
        job_skills
    )

    semantic_matches = []

    missing_concepts = []

    for job_index, job_vector in enumerate(
        job_embeddings
    ):

        best_score = 0.0
        best_skill = None

        for resume_index, resume_vector in enumerate(
            resume_embeddings
        ):

            score = cosine_similarity(
                resume_vector,
                job_vector
            )

            if score > best_score:

                best_score = score

                best_skill = resume_skills[
                    resume_index
                ]

        if best_score >= threshold:

            semantic_matches.append(

                {
                    "resume_skill":
                        best_skill,

                    "job_skill":
                        job_skills[
                            job_index
                        ],

                    "similarity":
                        round(
                            best_score * 100,
                            2
                        )
                }

            )

        else:

            missing_concepts.append(

                job_skills[
                    job_index
                ]

            )

    return {

        "semantic_matches":
            semantic_matches,

        "missing_concepts":
            missing_concepts

    }


def build_semantic_data(
    resume_text,
    job_text,
    resume_skills,
    job_skills
):
    """
    Build the semantic data object used
    throughout Phase 7.
    """

    overall_similarity = (
        compute_overall_similarity(
            resume_text,
            job_text
        )
    )

    skill_results = (
        compute_skill_similarity(
            resume_skills,
            job_skills
        )
    )

    return {

        "overall_similarity":
            overall_similarity,

        "semantic_matches":
            skill_results[
                "semantic_matches"
            ],

        "missing_concepts":
            skill_results[
                "missing_concepts"
            ]

    }