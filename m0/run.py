from is_this_thing_shit import ShitClassifier


def classify_website():
    "Classifies a website as shit."
    # config
    url = "https://stkbailey.substack.com/p/thread-how-did-your-college-degree"

    # execution code
    classifier = ShitClassifier()
    is_shit = classifier.is_this_website_shit(url)
    message = f"{url} is shit." if is_shit else f"{url} ain't shit."

    # logging result
    print(message)


if __name__ == "__main__":
    classify_website()
