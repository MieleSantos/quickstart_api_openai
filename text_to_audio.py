from config import client

'tido de voz'
# ['alloy','echo','fable','onyx','nova','shimer']

response = client.audio.speech.create(model='tts-1', voice='onyx', input='')
response.write_to_file('meu_audio.mp3')
