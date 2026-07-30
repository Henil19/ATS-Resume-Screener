def load_prompt(
    prompt_path
):
    """
    Load a prompt file.

    Parameters
    ----------
    prompt_path : str

    Returns
    -------
    str
    """

    with open(
        prompt_path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()