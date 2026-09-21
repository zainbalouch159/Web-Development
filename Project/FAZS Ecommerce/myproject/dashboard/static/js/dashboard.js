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

// Category Section
let category_menu = document.getElementById('category-options');
let category_show = document.getElementById('category_show');
console.log(1)
category_menu.addEventListener('change', async () => {
    console.log(2)
    let category_id = category_menu.value;

    if (!category_id) {
        category_show.innerHTML = '';
        return;
    }

    let response = await fetch(`category_products/${category_id}/`);
    let data = await response.json();
    console.log(data);
    category_show.innerHTML = '';

    data.products.forEach(product => {

        let product_section = document.createElement('div');
        product_section.className =
            'h-10 bg-orange-200 p-2 m-2 rounded flex justify-between';

        product_section.id = `product_section_${product.id}`;

        product_section.innerHTML = `
            <div class="flex gap-2">
                <img src="${product.image}"
                     alt="${product.name}"
                     class="h-full object-contain rounded">

                <span class="text-orange-500">
                    ${product.name}
                </span>
            </div>

            <div class="flex gap-1 text-orange-500">
                <span>Rs ${product.price}</span>
                <span>Stock ${product.stock}</span>
                <span>Sales ${product.sales}</span>

                <button
                    data-id="${product.id}"
                    class="fa-solid fa-pencil product_edit_button">
                </button>
            </div>
        `;

        category_show.append(product_section);
    });
});