# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyttsx3
from models import initialize_machine
# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech
def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()

	

machine=initialize_machine("machine4@gmail.com","123456789")
	
	

while(1):
	
	# Exception handling to handle
	# exceptions at the runtime
	try:
		
		# use the microphone as source for input.
		with sr.Microphone() as source2:
			
			# wait for a second to let the recognizer
			# adjust the energy threshold based on
			# the surrounding noise level
			products=machine.get_products()
			for product in products:
				print(vars(product))
			picked_item=None	
			picked_amount=None	
			r.adjust_for_ambient_noise(source2, duration=0.2)
			txt="what item do you want"
			SpeakText(txt)		
			#listens for the user's input
			audio2 = r.listen(source2)
			# Using google to recognize audio
			MyText = r.recognize_google(audio2)
			MyText = MyText.lower()
			print("Did you say ",MyText)
			for product in products:
				if MyText== product.name.lower():
					picked_item=product
			r.adjust_for_ambient_noise(source2, duration=0.2)
			txt="amount"
			SpeakText(txt)
			audio2 = r.listen(source2)
			MyText = r.recognize_google(audio2)
			MyText = MyText.lower()
			print("Did you say" ,MyText)
			picked_amount=int(MyText)
			if picked_item and picked_amount:
				machine.add_item_to_cart(picked_item,picked_amount)
				order=machine.view_cart()
				SpeakText(order)


			
			
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:
		print("unknown error occurred")


