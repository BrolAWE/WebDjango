var protocol = '';
if (window.location.protocol === 'https:') {
    protocol = 'wss:';
} else {
    protocol = 'ws:';
}

var chatSocket = new WebSocket(
    protocol + '//' + window.location.host +
    '/ws/chat/1/');

chatSocket.onmessage = function(e) {
    var data = JSON.parse(e.data);
    var message = data['message'];
    document.querySelector('#chat-log').value += (message + '\n');
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    var messageInputDom = document.querySelector('#chat-message-input');
    var message = messageInputDom.value;
    var user = document.querySelector("#user").innerHTML;
    chatSocket.send(JSON.stringify({
        'message': user+": "+message
    }));

    messageInputDom.value = '';
    userInputDom.value = '';
};