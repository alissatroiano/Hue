function showLoading() {
    console.log('showLoading() called');
    var createArtBtn = document.getElementById('createArtBtn');
    var loadingMessage = document.getElementById('loadingMessage');
    var createArtForm = document.getElementById('createArtForm');

    if (createArtBtn && loadingMessage) {
        console.log('Elements found');
        createArtBtn.disabled = true;
        loadingMessage.style.display = 'block';
        createArtForm.style.display = 'none';
        return true;
    } else {
        console.log('Elements not found');
        return false;
    }
}
