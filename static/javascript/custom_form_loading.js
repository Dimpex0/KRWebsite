const formBtn = document.querySelector('.custom-form button');
const customForm = document.querySelector('.custom-form');

formBtn.onclick = () => {
    if (customForm.checkValidity()) {
        formBtn.textContent = '';
        formBtn.classList.toggle('form-btn-loading');
    }
}