# Phyton Script: Enter Sub Questions
# Written By: Stephen Lam
# Date: 23-Dec-2015
# Screen resolution Specification: (1680,1050)

# Import GUI Intyerface
import pyautogui,time,string


#Variable Declarations
addButton=(1108,262)
questionField=(474,254)
confirmButton1=(759,180)
confirmButton=(759,180)
answerOption=(473,411)
addAnswer=(657,412)
saveButton=(520,640)
addButton2=(1108,262)
saveButton2=(503,489)

#Declare formData
#Engine Driven Pumps:

formData =[
{'question':'Do I understand what I need to do?','type':'Drop Down','answer':'Yes','answer1':'No','answer2':'','answer3':'','answer4':''},
{'question':'Do I need a SWMS for any ‘High Risk’ construction work?','type':'Drop Down','answer':'Yes','answer1':'No','answer2':'','answer3':'','answer4':''},
{'question':'Do I need any permits (e.g. hot work/confined space/dig?)?','type':'Drop Down','answer':'Yes','answer1':'No','answer2':'','answer3':'','answer4':''},
{'question':'Do I have the correct PPE in good condition for the task?','type':'Drop Down','answer':'Yes','answer1':'No','answer2':'','answer3':'','answer4':''},
{'question':'Do I have the suitable tools and equipment for the task?','type':'Drop Down','answer':'Yes','answer1':'No','answer2':'','answer3':'','answer4':''},
{'question':'Do I have my vehicle parked appropriately?','type':'Drop Down','answer':'Yes','answer1':'No','answer2':'','answer3':'','answer4':''},
{'question':'Am I trained, competent, licensed and fit to perform this task?','type':'Drop Down','answer':'Yes','answer1':'No','answer2':'','answer3':'','answer4':''},
{'question':'Manual Handling (e.g. Lifting, awkward positions, impacts, over-exertion)','type':'Drop Down','answer':'Yes','answer1':'No','answer2':'','answer3':'','answer4':''},
{'question':'Gravity (e.g. slips, trips and falls and struck by falling objects)','type':'Drop Down','answer':'Yes','answer1':'No','answer2':'','answer3':'','answer4':''},
{'question':'Mechanical (e.g. Caught in moving parts, struck by plant or flying objects)','type':'Drop Down','answer':'Yes','answer1':'No','answer2':'','answer3':'','answer4':''},
{'question':'Electrical (e.g. Electrocution from faulty tools or working close to live power)','type':'Drop Down','answer':'Yes','answer1':'No','answer2':'','answer3':'','answer4':''},
{'question':'Chemical (e.g. Inhaling, swallowing or touching acid, solvents or asbestos)','type':'Drop Down','answer':'Yes','answer1':'No','answer2':'','answer3':'','answer4':''},
{'question':'Pressure (e.g. Contact with highly pressurised fluid/gas or air)','type':'Drop Down','answer':'Yes','answer1':'No','answer2':'','answer3':'','answer4':''},
{'question':'Noise (e.g. Hearing damage, masking of emergency alarms)','type':'Drop Down','answer':'Yes','answer1':'No','answer2':'','answer3':'','answer4':''},
{'question':'Biological (e.g. Contracting diseases e.g. Hepatitis and Legionnaires)','type':'Drop Down','answer':'Yes','answer1':'No','answer2':'','answer3':'','answer4':''},
{'question':'Radiation (e.g. Exposure to radiation such as x-rays, sunlight or ultra-violet)','type':'Drop Down','answer':'Yes','answer1':'No','answer2':'','answer3':'','answer4':''},
{'question':'Psychological (e.g. stress, violence, fatigue, depression)','type':'Drop Down','answer':'Yes','answer1':'No','answer2':'','answer3':'','answer4':''},
{'question':'Heat and Cold ( e.g. Working with hot or cold objects or exposure to environment)','type':'Drop Down','answer':'Yes','answer1':'No','answer2':'','answer3':'','answer4':''},
{'question':'Risk(s) worked out?  ','type':'Drop Down','answer':'Yes','answer1':'No','answer2':'','answer3':'','answer4':''},
{'question':'SWMS1','type':'Free Text'},
{'question':'SWMS2','type':'Free Text'},
{'question':'SWMS3','type':'Free Text'},
{'question':'SWMS4','type':'Free Text'},
{'question':'SWMS completed ','type':'Drop Down','answer':'Yes','answer1':'No','answer2':'','answer3':'','answer4':''},
{'question':'Safe to proceed','type':'Drop Down','answer':'Yes','answer1':'No','answer2':'','answer3':'','answer4':''},



]



# {'question':'Python Script Question1','type':'Check Box','answer':'Yes','answer1':'','answer2':'','answer3':'','answer4':''},
#{'question':'Python Script Question3','type':'Free Text'},
#{'question':'Python Script Question3','type':'Free Text'},
#{'question':'Python Script Question4','type':'Large Text'},
#{'question':'Python Script Question5','type':'Date Field'}]

# Coding the form responses and controlling the keyboard and mouse via the pyautogui
'''

{'question':'SWMS: Project','type':'Free Text'},
{'question':'SWMS: SWMS No','type':'Free Text'},
{'question':'SWMS: Work Activity','type':'Free Text'},

{'question':'SWMS: Work Activity Description','type':'Free Text'},
{'question':'SWMS: Date Reviews','type':'Date Field'},

{'question':'SWMS: Codes of Practice / Standards Consulted','type':'Large Text'},
{'question':'SWMS: Plant and Equipment Required for this Activity','type':'Large Text'},
{'question':'SWMS: Details of Maintenance Checks Required for this Activity:','type':'Large Text'},
{'question':'SWMS: Materials Used','type':'Large Text'},
{'question':'SWMS: MSDS Required','type':'Large Text'},
{'question':'SWMS: Personnel Qualifications Required for this Activity','type':'Large Text'},
{'question':'SWMS: Specific Training Required for this Activity','type':'Large Text'},


{'question':'SWMS: Name1','type':'Free Text'},
{'question':'SWMS: Position1','type':'Free Text'},
{'question':'SWMS: Experience1','type':'Free Text'},

{'question':'SWMS: Name2','type':'Free Text'},
{'question':'SWMS: Position2','type':'Free Text'},
{'question':'SWMS: Experience2','type':'Free Text'},

{'question':'SWMS: Name3','type':'Free Text'},
{'question':'SWMS: Position3','type':'Free Text'},
{'question':'SWMS: Experience3','type':'Free Text'},

{'question':'SWMS: Activity1','type':'Free Text'},
{'question':'SWMS: Hazard1','type':'Free Text'},
{'question':'SWMS: Risk Rating1 (C)','type':'Drop Down','answer':'1','answer1':'2','answer2':'3','answer3':'4','answer4':'5'},
{'question':'SWMS: Risk Rating1 (P)','type':'Drop Down','answer':'1','answer1':'2','answer2':'3','answer3':'4','answer4':'5'},
{'question':'SWMS: Risk Rating1 (R)','type':'Drop Down','answer':'1','answer1':'2','answer2':'3','answer3':'4','answer4':'5'},
{'question':'SWMS: Control1','type':'Free Text'},
{'question':'SWMS: Risk Rating1 After Control(C)','type':'Drop Down','answer':'1','answer1':'2','answer2':'3','answer3':'4','answer4':'5'},
{'question':'SWMS: Risk Rating1 After Control(P)','type':'Drop Down','answer':'1','answer1':'2','answer2':'3','answer3':'4','answer4':'5'},
{'question':'SWMS: Risk Rating1 After Control(R)','type':'Drop Down','answer':'1','answer1':'2','answer2':'3','answer3':'4','answer4':'5'},
{'question':'SWMS: Person1','type':'Free Text'},

{'question':'SWMS: Activity2','type':'Free Text'},
{'question':'SWMS: Hazard2','type':'Free Text'},
{'question':'SWMS: Risk Rating2 (C)','type':'Drop Down','answer':'1','answer1':'2','answer2':'3','answer3':'4','answer4':'5'},
{'question':'SWMS: Risk Rating2 (P)','type':'Drop Down','answer':'1','answer1':'2','answer2':'3','answer3':'4','answer4':'5'},
{'question':'SWMS: Risk Rating2 (R)','type':'Drop Down','answer':'1','answer1':'2','answer2':'3','answer3':'4','answer4':'5'},
{'question':'SWMS: Control2','type':'Free Text'},
{'question':'SWMS: Risk Rating2 After Control(C)','type':'Drop Down','answer':'1','answer1':'2','answer2':'3','answer3':'4','answer4':'5'},
{'question':'SWMS: Risk Rating2 After Control(P)','type':'Drop Down','answer':'1','answer1':'2','answer2':'3','answer3':'4','answer4':'5'},
{'question':'SWMS: Risk Rating2 After Control(R)','type':'Drop Down','answer':'1','answer1':'2','answer2':'3','answer3':'4','answer4':'5'},
{'question':'SWMS: Person2','type':'Free Text'},

{'question':'SWMS: Activity3','type':'Free Text'},
'''
#pyautogui.PAUSE=10
pyautogui.moveTo(addButton)
pyautogui.click()
pyautogui.PAUSE=10
pyautogui.PAUSE=1

for info in formData:
	# Give the user a chance to kill the script
	print('>>>>> CTRL + C to kill the script <<<<<')
	time.sleep(3)

	pyautogui.moveTo(questionField)
	pyautogui.click()
	pyautogui.typewrite(info['question'])
	pyautogui.press('tab')
	pyautogui.press('tab')
	pyautogui.press('down')
	pyautogui.moveTo(confirmButton1)
	pyautogui.click()

	if info['type'] =='Check Box':
		pyautogui.moveTo(answerOption)
		pyautogui.click()
		if info['answer']!="":
			pyautogui.typewrite(info['answer'])
			pyautogui.moveTo(addAnswer)
			pyautogui.click()
		if info['answer1']!="":
			pyautogui.typewrite(info['answer1'])
			pyautogui.moveTo(addAnswer)
			pyautogui.click()
		if info['answer2']!="":
			pyautogui.typewrite(info['answer2'])
			pyautogui.moveTo(addAnswer)
			pyautogui.click()
		if info['answer3']!="":
			pyautogui.typewrite(info['answer3'])
			pyautogui.moveTo(addAnswer)
			pyautogui.click()
		if info['answer4']!="":
			pyautogui.typewrite(info['answer4'])
			pyautogui.moveTo(addAnswer)
			pyautogui.click()
		pyautogui.moveTo(saveButton)
		pyautogui.click()
		time.sleep(10)
	elif info['type'] =='Drop Down':
		pyautogui.press('down')
		pyautogui.moveTo(confirmButton)
		pyautogui.click()
		pyautogui.moveTo(answerOption)
		pyautogui.click()
		if info['answer']!="":
			pyautogui.typewrite(info['answer'])
			pyautogui.moveTo(addAnswer)
			pyautogui.click()
		if info['answer1']!="":
			pyautogui.typewrite(info['answer1'])
			pyautogui.moveTo(addAnswer)
			pyautogui.click()
		if info['answer2']!="":
			pyautogui.typewrite(info['answer2'])
			pyautogui.moveTo(addAnswer)
			pyautogui.click()
		if info['answer3']!="":
			pyautogui.typewrite(info['answer3'])
			pyautogui.moveTo(addAnswer)
			pyautogui.click()
		if info['answer4']!="":
			pyautogui.typewrite(info['answer4'])
			pyautogui.moveTo(addAnswer)
			pyautogui.click()
		pyautogui.moveTo(saveButton)
		pyautogui.click()
		time.sleep(10)
	elif info['type'] =='Free Text':
		pyautogui.press('down')
		pyautogui.moveTo(confirmButton)
		pyautogui.click()
		pyautogui.press('down')
		pyautogui.moveTo(confirmButton)
		pyautogui.click()
		pyautogui.moveTo(saveButton2)
		pyautogui.click()
		time.sleep(10)
	elif info['type'] =='Large Text':
		pyautogui.press('down')
		pyautogui.moveTo(confirmButton)
		pyautogui.click()
		pyautogui.press('down')
		pyautogui.moveTo(confirmButton)
		pyautogui.click()
		pyautogui.press('down')
		pyautogui.moveTo(confirmButton)
		pyautogui.click()
		pyautogui.moveTo(saveButton2)
		pyautogui.click()
		time.sleep(10)
	elif info['type'] =='Date Field':
		pyautogui.press('down')
		pyautogui.moveTo(confirmButton)
		pyautogui.click()
		pyautogui.press('down')
		pyautogui.moveTo(confirmButton)
		pyautogui.click()
		pyautogui.press('down')
		pyautogui.moveTo(confirmButton)
		pyautogui.click()
		pyautogui.press('down')
		pyautogui.moveTo(confirmButton)
		pyautogui.click()
		pyautogui.moveTo(saveButton2)
		pyautogui.click()
		time.sleep(10)




	pyautogui.click(addButton2)
