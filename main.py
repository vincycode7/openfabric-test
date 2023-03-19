import os
import warnings
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText
from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time
from chatter import Chatter

# Suppress warning messages
warnings.filterwarnings("ignore")

# Initialize a global instance of Chatter
global chatter_inst
chatter_inst = Chatter()

############################################################
# Callback function called on update config
############################################################
def config(configuration: ConfigClass):
    """
    Callback function called on update config.

    This function is called when a new configuration is applied to the system.
    It updates the global chatter_inst object with a new instance of Chatter.
    """
    global chatter_inst
    chatter_inst = Chatter()

############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    """
    Callback function called on each execution pass.

    This function takes a SimpleText object as input and uses the global chatter_inst
    object to generate a response for each input text. It returns a new SimpleText object
    containing the responses.

    Args:
        request (SimpleText): A SimpleText object containing the input text.
        ray (OpenfabricExecutionRay): An object containing execution context.

    Returns:
        SimpleText: A SimpleText object containing the response text.
    """
    output = []

    # Check if input text exists
    if not request or not request.text:
        raise ValueError("Input text is empty or does not exist")

    # Loop through input texts and generate responses
    for text in request.text:
        try:
            response = chatter_inst.chat(text)
            output.append(response)
        except Exception as e:
            # Log error message
            error_msg = f"Error generating response for input text: {text}. Error: {e}"
            print(error_msg)
            with open("error_log.txt", "a") as f:
                f.write(error_msg + "\n")

    # Return SimpleText object containing output text
    return SimpleText(dict(text=output))
