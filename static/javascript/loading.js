const images = document.getElementsByTagName('img');

for (const image of images) {
    image.onload = () => {
        const imageClass = image.className;
        const currentLoader = document.querySelector(`.${imageClass} + .loader`);
        currentLoader.style.display = 'none';
    }
}

window.onload = () => {
    const loaders = document.querySelectorAll('.loader');
    loaders.forEach(loader => {
        loader.style.display = 'none';
    })
}