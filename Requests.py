import requests
response=requests.get('https://api.rentcode.net/api/v2/order/19886259/check?apiKey=vivvTm7TgEYIJFV7I9tQvnvLsDtT9WQ8k51eeBPZAiQv')

# response=requests.get('https://api.rentcode.net/api/v2/order/request?apiKey=vivvTm7TgEYIJFV7I9tQvnvLsDtT9WQ8k51eeBPZAiQv&ServiceProviderId=3&MaximumSms=1&AllowVoiceSms=false')
print('status_code',response.status_code)
print(response.json())