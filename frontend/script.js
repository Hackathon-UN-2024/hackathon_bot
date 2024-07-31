function sendMessage() {
    var inputField = document.getElementById('mensaje');
    var mensaje = inputField.value;
    if (mensaje.trim() !== '') {
        addMessageBubble(inputField, mensaje, "saliente")

        let data = {
            "user_message": mensaje,
        }

        getBotMessage("http://localhost:3000/histories", data).then(response => {
            if (response == null) {
                return
            }

            // { bot_response: string }
            addMessageBubble(inputField, response.bot_response, "entrante")
        }).catch(error => {
            console.error(error);
        })
    }
}

function addMessageBubble(inputField, mensaje, messageDirection) {
    let chatBox = document.getElementById('chat-box');
    let newMessage = document.createElement('div');
    newMessage.classList.add('message', messageDirection);
    newMessage.textContent = mensaje;
    chatBox.appendChild(newMessage);
    inputField.value = '';
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function getBotMessage(url = '', data = {}) {
    if (data === {}) {
        return Promise.resolve(null)
    }

    const response = await fetch(url, {
        method: 'POST',
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });

    return response.json();
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