from is_this_thing_shit import ShitClassifier

from dagster import op


@op
def classify_website_op():
    "Classifies a website as shit."
    # config
    URL = "https://stkbailey.substack.com/p/thread-how-did-your-college-degree"

    # execution code
    classifier = ShitClassifier()
    is_shit = classifier.is_this_website_shit(URL)
    message = f"{URL} is shit." if is_shit else f"{URL} ain't shit."

    # logging result
    print(message)


if __name__ == "__main__":

    classify_website_op()
