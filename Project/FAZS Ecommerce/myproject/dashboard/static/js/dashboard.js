// Delete Product Function
function delete_product(form) {
    form.addEventListener('submit', async (event) => {
        event.preventDefault()

        const formdata = new FormData(form)
        const id = form.dataset.id

        const response = await fetch(`product_delete/${id}/`, {
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

category_menu.addEventListener('change', async () => {
    
    let category_id = category_menu.value;
    if (category_menu.value !== '' && category_menu.options[category_menu.selectedIndex].text.trim().toLowerCase() !== 'other') {

        input_category_id = document.getElementById('category_id_delete');
        input_category_id.value = category_id;

        delete_category_form = document.getElementById('delete_category_form');
        delete_category_form.classList.add('flex');
        delete_category_form.classList.remove('hidden');

    } else {
        delete_category_form.classList.add('hidden');
        delete_category_form.classList.remove('flex');
        
    }
    if (!category_id) {
        category_show.innerHTML = '';
        return;
    }

    let response = await fetch(`category_products/${category_id}/`);
    let data = await response.json();

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

            </div>
        `;

        category_show.append(product_section);

    });

});

// Collection Section

let collection_menu = document.getElementById('collection-options');
let collection_show = document.getElementById('collection_show');

collection_menu.addEventListener('change', async () => {

    let collection_id = collection_menu.value;

    if (collection_id === '') {
        collection_show.innerHTML = '';
        return;
    }

    let input_collection_id =
        document.getElementById('collection_id_delete');

    input_collection_id.value = collection_id;

    let delete_collection_form =
        document.getElementById('delete_collection_form');

    delete_collection_form.classList.add('flex');
    delete_collection_form.classList.remove('hidden');

    let response =
        await fetch(`collection_products/${collection_id}/`);

    let data = await response.json();

    collection_show.innerHTML = '';

    data.products.forEach(product => {

        let product_section = document.createElement('div');

        product_section.className =
            'h-10 bg-orange-200 p-2 m-2 rounded flex justify-between';

        product_section.id =
            `collection_product_section_${product.id}`;

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

            </div>
        `;

        collection_show.append(product_section);
    });
});