function sendMessage() {
    var inputField = document.getElementById('mensaje');
    var mensaje = inputField.value;
    if (mensaje.trim() !== '') {
        var chatBox = document.getElementById('chat-box');
        var newMessage = document.createElement('div');
        newMessage.classList.add('message', 'saliente');
        newMessage.textContent = mensaje;
        chatBox.appendChild(newMessage);
        inputField.value = '';
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}

document.getElementById('mensaje').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
        event.preventDefault();
    }
});

document.getElementById('theme-switch').addEventListener('change', function() {
    document.body.classList.toggle('dark-mode');
    localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));
});

window.onload = function() {
    if (localStorage.getItem('darkMode') === 'true') {
        document.body.classList.add('dark-mode');
        document.getElementById('theme-switch').checked = true;
    }

    document.getElementById('start-button').addEventListener('click', function() {
        document.getElementById('splash-screen').classList.add('fade-out');
        setTimeout(function() {
            document.getElementById('splash-screen').style.display = 'none';
            document.getElementById('chat-container').classList.remove('hidden');
        }, 1000); // Duración de la transición en milisegundos
    });
}