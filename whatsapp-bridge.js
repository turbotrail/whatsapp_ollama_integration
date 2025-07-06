const { Client, LocalAuth } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const axios = require('axios');

const client = new Client({ authStrategy: new LocalAuth() });

client.on('qr', qr => qrcode.generate(qr, { small: true }));
client.on('ready', () => console.log('WhatsApp is ready!'));

client.on('message', async msg => {
    if (msg.body && msg.body.includes('@ollama')) {
        const cleanMessage = msg.body.replace('@ollama', '').trim();
        const res = await axios.post('http://localhost:6000/message', {
            message: cleanMessage,
            from: msg.from
        });
        msg.reply(res.data.reply);
    }
});

client.initialize();