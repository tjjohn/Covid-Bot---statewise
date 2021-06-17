# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionResult(Action):

     def name(self) -> Text:
         return "action_result"    # define in stories & doamin

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text=" result on loading")

         return []
     
        
        
class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "nameaction"      

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
          entities = tracker.latest_message['entities']
          n=''
          for e in entities:
            if e['entity']=='person':
                n=e['value']
                
            if n=='john':
                m="hey young boy"
            if n=='mary':
                m="hey young girl"
            if n=='jose':
                m="hey "+n +"how are youl"
                

          dispatcher.utter_message(text=m)

          return []

class Actioncovid(Action):

     def name(self) -> Text:
         return "action_covid"    # define in stories & doamin

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
         url="https://api.covid19india.org/data.json"
         
         response = requests.get(url).json()
         
         
         
         entities = tracker.latest_message['entities']
         for e in entities:
          if e['entity']=='state':
            entity_extracted=e['value']
         
         for jdata in response['statewise']:
          try:   
              if jdata['state']==entity_extracted.title():        # comparing extracted state with entity
                  message="Active cases: "+jdata["active"] + "    Total Death: "+  jdata["deaths"] +  "   Today's Covid  cases:"   + jdata["deltaconfirmed"] + "   Today's Death count:"   +  jdata["deltadeaths"] + "   Today's Recovered count:" + jdata["deltarecovered"] + "   Updated data till "  +jdata["lastupdatedtime"]  
             
          except:     
               message="  data cannot be fetched"
         dispatcher.utter_message(text=message)

         return []