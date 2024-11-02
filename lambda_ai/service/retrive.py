import boto3
import json

from botocore.exceptions import ClientError

def retrive(input_prompt):
  # Use the native inference API to send a text message to Anthropic Claude.

    # Create a Bedrock Runtime client in the AWS Region of your choice.
    client = boto3.client('bedrock-agent-runtime', region_name="us-east-1")
    # Set the model ID,
    model_id = "anthropic.claude-3-5-sonnet-20240620-v1:0"
    kb_id = "ICQXXBQERM"
    # Define the prompt for the model.
    prompt = input_prompt
    response = client.retrieve_and_generate(
        input={
            'text': prompt
        },retrieveAndGenerateConfiguration={
            'knowledgeBaseConfiguration': {
                'knowledgeBaseId': kb_id,
                'modelArn': model_id,
            },
            'type': 'KNOWLEDGE_BASE'
        }
    )

    response_text = response["output"]["text"]

    return response_text

