#!/usr/bin/env python
# encoding: utf-8
"""
Dialogue Manager

"""
__author__ = 'byu@ist.psu.edu (Bo Yu)'

import uuid

from PlanGraph import PlanGraph
import BasicActions

class DialogueManager():
    """manage the dialogue process"""
    def __init__(self, context, dlg_id=""):
        if dlg_id:
            self.id = dlg_id
        else:
            # make a random id
            self.id = str(uuid.uuid4())
        self.participants = []

        self.context = context
        self.planGraph = PlanGraph()
                                
    def addParticipant(self, newParticipant):
        """docstring for addParticipant"""
        pId = newParticipant.get("id", "")
        if pId:
            self.participants.append(newParticipant)
                                        
    def process(self, message):
        """process the incoming message, mocked up to test ArcPy atm"""
        response = {}
        if message["speech"]:
            if message["speech"]["operation"] == "buffer":
                input_file = "C:\Work\Data\World\CITIES.SHP"
                distance = 10
                output_file = "C:\Work\Data\World\CITIES_buffer.SHP"
                BasicActions.buffer(input_file, output_file, distance)
                response["response"] = {
                    "map": {"output_layers": [output_file,]}
                }
                
        return response