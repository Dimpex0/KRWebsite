const albumImages = document.querySelectorAll('.images-container img');
const focusedImage = document.getElementsByClassName('focused-img')[0];
const focusedImageContainer = document.getElementsByClassName('focused-container')[0];
const leftArrow = document.getElementsByClassName('left-arrow')[0];
const rightArrow = document.getElementsByClassName('right-arrow')[0];
const closeBtn = document.getElementsByClassName('close-btn')[0];

let currentIndex;

for (let i = 0; i < albumImages.length; i++) {
    const image = albumImages[i]
    image.onclick = () => {
        setFocusedImage(image)
    }
}

function setFocusedImage(image) {
    for (const albumImage of albumImages) {
        albumImage.style.opacity = '0.2'
    }
    focusedImageContainer.style.display = 'block'
    focusedImage.src = image.src;
    currentIndex = Array.from(albumImages).indexOf(image);
}

rightArrow.onclick = () => {
    if (currentIndex < albumImages.length - 1) {
        setFocusedImage(albumImages[currentIndex + 1])
    } else {
        setFocusedImage(albumImages[0])
    }
}

leftArrow.onclick = () => {
    if (currentIndex > 0) {
        setFocusedImage(albumImages[currentIndex - 1])
    } else {
        setFocusedImage(albumImages[albumImages.length - 1])
    }
}

function closeFocused() {
    focusedImage.src = '';
    focusedImageContainer.style.display = 'none';
    for (const image of albumImages) {
        image.style.opacity = '1';
    }
}

closeBtn.onclick = () => {
    closeFocused()
}
