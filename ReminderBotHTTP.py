import urllib.request, urllib.error, urllib.parse
import json

# SENDING GETME REQUEST AND RETURNING THE ANSWER
def GetMeRequest(startURL=r'https://api.telegram.org/bot', token=''):
    """Sends the "getMe" request for bot with token at startURL and returns the answer"""
    httpRequest = urllib.request.Request(startURL + token + r'/getMe')
    try:
        httpResponse = urllib.request.urlopen(httpRequest)
    except urllib.error.HTTPError as e:
        return (1, str(e.code) + ' ' + e.msg)
    httpResponseText = httpResponse.read().decode('utf-8')
    decodedAnswer = json.loads(httpResponseText)
    return (0, decodedAnswer)


# SENDING GETUPDATE REQUEST AND RETURNING THE ANSWER
def SendGetUpdatesRequest(next_update_num = -101, limit = 100, timeout = 2, token ='', start_URL =r'https://api.telegram.org/bot'):
    """Sends the "getUpdates" request for bot with token at startURL and returns the answer, the -101 updatenum leads to no updatenum in request"""
    if next_update_num == -101:
        request_data = 'limit=' + str(limit) + '&timeout=' + str(timeout) + '&allowed_updates=["message"]'
    else:
        request_data = 'offset=' + str(next_update_num) + '&limit=' + str(limit) + '&timeout=' + str(timeout) + '&allowed_updates=["message"]'

    http_request = urllib.request.Request(start_URL + token + r'/getUpdates?' + request_data)
    print('Sent request: ' + start_URL + token + r'/getUpdates?' + request_data)
    try:
        http_response = urllib.request.urlopen(http_request)
    except urllib.error.HTTPError as e:
        return (1, str(e.code) + ' ' + e.msg)

    http_response_text = http_response.read().decode('utf-8')
    decoded_answer = json.loads(http_response_text)
    print('Answer (decoded): ' + str(decoded_answer))
    return (0, decoded_answer)


# SENDING MESSAGE TO A SOURCE
def SendMessageToChat(chat_id, text, parse_mode, startURL=r'https://api.telegram.org/bot', token=''):
    """Sends a <text> message to the chat with <chat_id>, marked up with <parse_mode> if defined"""
    message_request = 'chat_id=' + str(chat_id) + '&text=' + urllib.parse.quote(text)
    if parse_mode in ('Markdown', 'HTML'):
        message_request += '&parse_mode=' + parse_mode

    http_request = urllib.request.Request(startURL + token + r'/sendMessage?' + message_request)
    print('Sent request: ' + startURL + token + r'/sendMessage?' + message_request)
    try:
        http_response = urllib.request.urlopen(http_request)
    except urllib.error.HTTPError as e:
        return (1, str(e.code) + ' ' + e.msg)

    http_response_text = http_response.read().decode('utf-8')
    decoded_answer = json.loads(http_response_text)
    print('Answer (decoded): ' + str(decoded_answer))
    return (0, decoded_answer)
