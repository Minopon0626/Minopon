// index.js (またはプラグインのエントリーポイント)
const WebSocket = require('ws');

document.addEventListener('DOMContentLoaded', () => {
    const button = document.createElement('button');
    button.textContent = 'Send Hello';
    button.onclick = function() {
        const ws = new WebSocket('ws://localhost:8765');
        ws.onopen = function() {
            ws.send('hello');
            console.log('Sent "hello" to the server');
        };
    };

    document.body.appendChild(button);
});
