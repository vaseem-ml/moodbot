from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk import Action
from rasa_sdk.events import SlotSet, FollowupAction

##for action_greet
class actionGreet(Action):
	def name(self) -> Text:
		return "action_greet"

	def run(self,
			dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict]:

		starting_action = ["action 1", "action 2", "action 3", "action 4", "action 5"]

		buttons = []
		for action in starting_action:
			title = action
			payload = "/inform"
			buttons.append(
                {"title": "{}".format(title), "payload": payload})


		message = "You also can choose from here "
		dispatcher.utter_button_message(message, buttons);