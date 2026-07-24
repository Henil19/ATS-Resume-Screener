import re


def tokenize(text):

    tokens = re.findall(
        r"\b[\w.]+\b",
        text
    )

    return tokens

if __name__ == "__main__":

    sample = "Python SQL ML Node.js TensorFlow AWS React.js"

    print(tokenize(sample))