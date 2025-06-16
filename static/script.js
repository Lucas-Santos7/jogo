document.getElementById('menuBtn').onclick = function() {
    document.getElementById('sideMenu').classList.toggle('open');
};

window.addEventListener('message', (event) => {
    if (event.data.source === 'readyplayerme') {
        if (event.data.eventName === 'v1.avatar.exported') {
            const avatarUrl = event.data.data.url;
            // Salve o avatarUrl ou use como quiser
            console.log('Avatar URL:', avatarUrl);
        }
    }
});

// Exemplo de clique nas partes do avatar (futuramente)
// document.getElementById('avatar').onclick = function(event) {
//     // Lógica para identificar a parte clicada e abrir opções de customização
// };