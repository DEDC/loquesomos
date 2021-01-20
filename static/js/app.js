document.addEventListener('DOMContentLoaded', function () {
    dropdown = document.querySelectorAll('a.dropdown')
    dropdown.forEach(element => {
        element.addEventListener('click', function (e) {
            e.preventDefault()
            console.log(element.getAttribute('href'))
            todrop = document.querySelector(element.getAttribute('href'))
            todrop.classList.toggle('hide')
        })
    });
})