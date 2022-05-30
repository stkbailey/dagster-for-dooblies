import yaml

from dagster import op, job, resource
from is_this_thing_shit import ShitClassifier


URL = "https://stkbailey.substack.com/p/thread-how-did-your-college-degree"


@resource
def shit_classifier():
    "Object that can be used to classify things."
    return ShitClassifier()


@op(config_schema={"url": str})
def generate_url_op(context):
    "Classifies a website as shit."
    return context.op_config["url"]


@op(required_resource_keys={"shit_classifier"})
def classify_website_op(context, url: str):
    "Classifies a website as shit."
    classifier = context.resources.shit_classifier
    is_shit = classifier.is_this_website_shit(url)
    message = f"{url} is shit." if is_shit else f"{url} ain't shit."
    context.log.info(message)


configured_classifier = shit_classifier.configured({})
job_config = f"""
ops:
  generate_url_op:
    config:
      url: {URL}
"""


@job(
    resource_defs={"shit_classifier": configured_classifier},
    config=yaml.safe_load(job_config),
)
def classify_website_job():
    url = generate_url_op()
    classify_website_op(url)


if __name__ == "__main__":
    classify_website_job.execute_in_process()
