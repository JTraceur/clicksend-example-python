import clicksend_client
from clicksend_client import MmsMessage
from clicksend_client.rest import ApiException
import json
import base64

#Get API Details from user:
configuration = clicksend_client.Configuration()
configuration.username = input('Enter your clicksend API Username: ')
configuration.password = input('enter your clicksend API Key: ')

#Open and read env var file:
with open('./environment vars.json', 'r') as evFile:
    evData = evFile.read()

evFile.close() #Close file after we are finished with it

#Load environment variables from JSON
eV = json.loads(evData)

#Bootup instance of API:
mmsInstance = clicksend_client.MMSApi(clicksend_client.ApiClient(configuration))

#Package message:
print('Packaging message...')
mmsMsg = MmsMessage(
    to = eV['sendTo'],
    body = f'Hello, this is {eV["senderName"]} completing the code test for {eV["senderQuest"]} role. Checkout my code at: {eV["githubURL"]}. Sent from {eV["sentFrom"]}',
    subject = 'Msg Test'
)
mmsMessages = clicksend_client.MmsMessageCollection(
    media_file = eV['pictureFileURL'],
    messages = [mmsMsg]
)

print(mmsMessages)

#Send MMS:
try:
    print('Sending message...')
    serverResponse = mmsInstance.mms_send_post(mmsMessages)
    print('Message sent!')
except ApiException as e:
    print(f'ERR: {e}')