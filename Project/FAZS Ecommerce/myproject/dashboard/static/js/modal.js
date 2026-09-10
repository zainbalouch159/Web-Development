add_button = document.getElementById('Product-add').addEventListener('click', (event) => {
    overlay = document.getElementById('Overlay')
    overlay.classList.add('flex')
    overlay.classList.remove('hidden')

})

overlay = document.getElementById('Overlay')
overlay.addEventListener('click', (event) => {
    if (event.target == overlay) {
        overlay.classList.remove('flex')
        overlay.classList.add('hidden')
    }
})