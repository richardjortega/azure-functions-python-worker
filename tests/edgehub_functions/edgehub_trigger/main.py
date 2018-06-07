import azure.functions


def main(message: azf.EdgeHubMessage, context) -> str:
    return 'Hello World!'
