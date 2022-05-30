import yaml

from dagster import op, job, resource, Any, Out, Output
from is_this_thing_shit import ShitClassifier


URL = "https://stkbailey.substack.com/p/thread-how-did-your-college-degree"


@resource
def shit_classifier():
    "Object that can be used to classify things."
    return ShitClassifier()


@op(
    config_schema={"input": Any},
    out={
        "number": Out(float, is_required=False),
        "url": Out(str, is_required=False),
        "text": Out(str, is_required=False),
    },
)
def generate_input_op(context):
    "Classifies a website as shit."
    input = context.op_config["input"]
    if isinstance(input, float) or isinstance(input, int):
        return Output(float(input), output_name="number")
    elif isinstance(input, str) and input.startswith("http"):
        return Output(input, output_name="url")
    return Output(input, output_name="text")


@op(required_resource_keys={"shit_classifier"})
def classify_website_op(context, url: str):
    "Classifies a website as shit."
    classifier = context.resources.shit_classifier
    is_shit = classifier.is_this_website_shit(url)
    message = f"{url} is shit." if is_shit else f"{url} ain't shit."
    context.log.info(message)


@op(required_resource_keys={"shit_classifier"})
def classify_number_op(context, number: float):
    "Classifies a website as shit."
    classifier = context.resources.shit_classifier
    is_shit = classifier.is_this_number_shit(number)
    message = f"{number} is shit." if is_shit else f"{number} ain't shit."
    context.log.info(message)


@op(required_resource_keys={"shit_classifier"})
def classify_text_op(context, text: str):
    "Classifies a website as shit."
    classifier = context.resources.shit_classifier
    is_shit = classifier.is_this_text_shit(text)
    message = f"{text} is shit." if is_shit else f"{text} ain't shit."
    context.log.info(message)


configured_classifier = shit_classifier.configured({})
job_config = f"""
ops:
  generate_input_op:
    config:
      input: {URL}
"""


@job(
    resource_defs={"shit_classifier": configured_classifier},
    config=yaml.safe_load(job_config),
)
def classify_website_job():
    num, url, txt = generate_input_op()
    classify_number_op(num)
    classify_website_op(url)
    classify_text_op(txt)


if __name__ == "__main__":
    classify_website_job.execute_in_process()
