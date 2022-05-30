import yaml

from dagster import op, job
from is_this_thing_shit import ShitClassifier


URL = "https://stkbailey.substack.com/p/thread-how-did-your-college-degree"


@op(config_schema={"url": str})
def generate_url_op(context):
    "Classifies a website as shit."
    return context.op_config["url"]


@op
def classify_website_op(url: str):
    "Classifies a website as shit."

    # execution code
    classifier = ShitClassifier()
    is_shit = classifier.is_this_website_shit(url)
    message = f"{url} is shit." if is_shit else f"{url} ain't shit."

    # logging result
    print(message)


job_config = f"""
ops:
  generate_url_op:
    config:
      url: {URL}
"""


@job(config=yaml.safe_load(job_config))
def classify_website_job():
    url = generate_url_op()
    classify_website_op(url)


if __name__ == "__main__":
    classify_website_job.execute_in_process()
