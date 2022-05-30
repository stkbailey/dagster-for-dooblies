from is_this_thing_shit import ShitClassifier

from dagster import op

URL = "https://stkbailey.substack.com/p/thread-how-did-your-college-degree"


@op
def generate_url_op():
    "Classifies a website as shit."
    return URL


@op
def classify_website_op(url: str):
    "Classifies a website as shit."

    # execution code
    classifier = ShitClassifier()
    is_shit = classifier.is_this_website_shit(url)
    message = f"{url} is shit." if is_shit else f"{url} ain't shit."

    # logging result
    print(message)


if __name__ == "__main__":
    url = generate_url_op()
    classify_website_op(url)
