function showLoading() {
    console.log('showLoading() called');
    var createArtBtn = document.getElementById('createArtBtn');
    var loadingMessage = document.getElementById('loadingMessage');

    if (createArtBtn && loadingMessage) {
        console.log('Elements found');
        createArtBtn.disabled = true;
        loadingMessage.style.display = 'block';
        return true;
    } else {
        console.log('Elements not found');
        return false;
    }
}
