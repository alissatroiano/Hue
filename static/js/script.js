// find images without an alt attribute
// and give them a red border

function nonAltImages() {
    const images = document.getElementByName('img');
    for (let i = 0; i < images.length; i++) {
        if (images[i].alt === '') {
            images[i].style.border = '3px solid red';
        }
    }
}