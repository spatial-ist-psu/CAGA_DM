# Create your views here.
from django.conf import settings 
from django.http import HttpResponse
from CAGA_DM.PlanGraph.DialogueManager import DialogueManager

import json

# maintain the list of ongoing dialogues
currDialogues = []

def getDialogueById(dialogueId):
    """docstring for __getDialogueById"""
    if dialogueId:
        # check the current ongoing dialogue first
        for dialogue in currDialogues:
            if dialogue.id == dialogueId:
                return dialogue
    return None

def addDialogue(dlg_obj):
    # if more than the total number of dialogues, pop out the first dialogue
    if len(currDialogues) >= settings.DIALOGUE_NUM:
        currDialogues.pop(0)
    currDialogues.append(dlg_obj)

    
def dlgsHandler(request):
    """list all the current dialogues"""
    if request.method == "GET":
        response = []
        for dialogue in currDialogues:
            response.append(dialogue.id)
        return HttpResponse(json.dumps(response), mimetype='application/json')

def updateDlg(request):
    """update the dialogue with incoming message"""
    if request.method == "POST":
        response = {}
        data = json.loads(request.raw_post_data)
        dlg_id = data.get("dlg_id", "")
        if dlg_id:
            dlg = getDialogueById(dlg_id)
            if dlg:
                message = data.get("message", {})
                if message:
                    response = dlg.process(message)
                    response["status"] = "success"
        else:
            response["status"] = "error"
        return HttpResponse(json.dumps(response), mimetype='application/json')
    
def startDlg(request):
    """start a new dialogue in the given context, with the initial participant"""
    if request.method == "POST":
        response = {}
        data = json.loads(request.raw_post_data)
        dlg_id = data.get("dlg_id", "")
        if dlg_id:
            # check whether the id is alrady associated with existing dialogues
            if getDialogueById(dlg_id):
                response["status"] = "error"
                response["message"] = "the dialogue already exists!"
                return HttpResponse(json.dumps(response), mimetype='application/json')
        participants = data.get("participants", [])
        context = data.get("context", "")
        if participants and context:
            dialogue = DialogueManager(context, dlg_id)
            if dialogue:
                for participant in participants:
                    dialogue.addParticipant(participant)
                addDialogue(dialogue)
                response["status"] = "success"
                response["dlg_id"] = dialogue.id
            else:
                response["status"] = "error"
                response["message"] = "cannot create the dialogue manager!"
        else:
            response["status"] = "error"
            response["message"] = "please indicate the context and specify at least one participant!"
        return HttpResponse(json.dumps(response), mimetype='application/json')
    
def stopDlg(request):
    dlg_id = request.REQUEST.get("dlg_id", "")
    response = {}
    if dlg_id:
        dlg = getDialogueById(dlg_id)
        if dlg:
            # the place to do some persistence and clean-up before removing the dialogue
            currDialogues.remove(dlg)
            response["status"] = "success"
    else:
        response["status"] = "error"
        response["message"] = "cannot find the dialogue!"
    return HttpResponse(json.dumps(response), mimetype='application/json')