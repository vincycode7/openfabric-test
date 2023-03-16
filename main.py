import os
import warnings
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText
from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time

from chatter import Chatter

global chatter_inst
chatter_inst = Chatter()

############################################################
# Callback function called on update config
############################################################
def config(configuration: ConfigClass):
    chatter_inst = Chatter()


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []
    for text in request.text:
        response = chatter_inst.chat(text)
        output.append(response)

    return SimpleText(dict(text=output))
