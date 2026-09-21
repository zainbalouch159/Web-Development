// Delete Product Function
function delete_product(form) {
    form.addEventListener('submit', async (event) => {
        event.preventDefault()

        const formdata = new FormData(form)
        const id = formdata.get('product_id')

        const response = await fetch(form.action, {
            method: 'POST',
            body: formdata
        })

        const data = await response.json()

        if (data === 'success') {
            const product = document.getElementById(`product_section_${id}`)
            product.remove()
        }
    })
}


// Product Delete 
delete_form = document.querySelectorAll('.delete_product_form')

delete_form.forEach(form => {
    delete_product(form)
});

