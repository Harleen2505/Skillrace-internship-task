subjects = ["I", "YOU"]
verbs = ["PLAY", "LOVE"]
objects = ["CRICKET", "LUDO"]

def generate_sentences():
    sentences = []
    for subject in subjects:
        for verb in verbs:
            for obj in objects:
                sentence = f"{subject} {verb} {obj}."
                sentences.append(sentence)
    return sentences

def main():
    sentences = generate_sentences()
    print("Sentences:")
    for sentence in sentences:
        print(sentence)

if __name__ == "__main__":
    main()
