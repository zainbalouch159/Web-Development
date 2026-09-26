
// Product Edit
let product_edit = document.querySelectorAll('.product_edit_button');

product_edit.forEach(product => {

    product.addEventListener('click', async () => {

        // Show the product edit overlay
        let product_edit_overlay = document.getElementById('Edit_Product_Overlay');
        product_edit_overlay.classList.add('flex');
        product_edit_overlay.classList.remove('hidden');

        // Get id of the product to be edited
        let id = product.dataset.id;

        // Send to backend to get the product details
        let response = await fetch(`product_edit/${id}/`);
        let data = await response.json();

        // Populate the product edit form with the data received from backend
        let form = document.getElementById('product-edit-form');
        input = document.createElement('input')
        input.value = id
        input.name = 'product_id'
        input.classList.add('hidden')
        form.append(input)

        // Populate the product edit form with the data received from backend
        // Name 
        let name = document.getElementById('product-name-update');
        name.value = data.name;

        // Description
        let description = document.getElementById('product-description-update');
        description.value = data.description;

        // Stock
        let stock = document.getElementById('product-stock-update');
        stock.value = data.stock;

        // Discount
        let discount = document.getElementById('product-discount-update');
        discount.value = data.discount;

        // Info 
        let info = document.getElementById('product-info-update');
        info.value = data.info;

        // Image 
        let image = document.getElementById('product-image-preview');
        image.src = data.image;

        // Price 
        let price = document.getElementById('product-price-update');
        price.value = data.price;

        // Category
        let category = document.getElementById('category-menu-product-edit');
        category.value = data.category;

        // Collections
        let collections = document.getElementById('Collections-menu-product-edit');

        let collection_options = collections.options;
        for (let option of collection_options) {
            option.selected = false;
        }
        for (let option of collection_options) {
            if (data.collections.includes(Number(option.value))) {
                option.selected = true;
            }
        }
    });
});


// Collections Submit Product
let Collections_form = document.getElementById('Collections-add-form-product');

Collections_form.addEventListener('submit', async (event) => {

    event.preventDefault();

    // Overlay
    let CollectionsAddOverlay = document.getElementById('Collections-add-Overlay-product');
    CollectionsAddOverlay.classList.remove('flex');
    CollectionsAddOverlay.classList.add('hidden');

    // Fetching data
    let formdata = new FormData(Collections_form);

    let response = await fetch(Collections_form.action, {
        method: 'POST',
        body: formdata
    });

    let data = await response.json();

    // Creating a new option
    let new_Collections_option = document.createElement('option');

    new_Collections_option.value = data.id;
    new_Collections_option.textContent = data.title;

    if (Collections_form.dataset.data === 'edit') {
        let Collections_menubar = document.getElementById('Collections-menu-product-edit');

    Collections_menubar.appendChild(new_Collections_option);

        new_Collections_option.selected = true;
    }

    else if (Collections_form.dataset.data === 'add') {
        let Collections_menubar = document.getElementById('Collections-menu-product-add');
        Collections_menubar.appendChild(new_Collections_option);
        new_Collections_option.selected = true;
    }
});

// Category Submit in product
let category_form = document.getElementById('category-add-form-product');

category_form.addEventListener('submit', async (event) => {

    // Prevent the default form submission behavior
    event.preventDefault();

    // Overlay
    categoryAddOverlay.classList.remove('flex');
    categoryAddOverlay.classList.add('hidden');
    
    // Sending data to the backend using fetch API
    let formdata = new FormData(category_form);

    let response = await fetch(category_form.action, {
        method: 'POST',
        body: formdata
    });

    let data = await response.json();
    // Create a new option element for the newly added category
    let new_category_option = document.createElement('option');

    new_category_option.value = data.id;
    new_category_option.textContent = data.name;

    if (category_form.dataset.data === 'edit') {
        let category_menubar = document.getElementById('category-menu-product-edit');
        
        category_menubar.appendChild(new_category_option);
        
        new_category_option.selected = true;
    }

    if (category_form.dataset.data === 'add') {
        let category_menubar = document.getElementById('category-menu-product-add');
        
        category_menubar.appendChild(new_category_option);
        
        new_category_option.selected = true;
    }
});



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

        delete_category_form = document.getElementById('delete_category_form');
        delete_category_form.dataset.id = category_id;

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

// Category Delete

let delete_category_form = document.getElementById('delete_category_form');
delete_category_form.addEventListener('submit', async (event) => {
    event.preventDefault();

    category_id = document.getElementById('category-options').value;


    response = await fetch(`category_delete/${category_id}/`)
    if (response.ok) {
        const category_option = document.getElementById(`Category_${category_id}`);
        category_option.remove();
        delete_category_form.classList.add('hidden');
        delete_category_form.classList.remove('flex');
        category_show.innerHTML = '';
    }
})

// Collection Section

let collection_menu = document.getElementById('collection-options');
let collection_show = document.getElementById('collection_show');

collection_menu.addEventListener('change', async () => {

    let collection_id = collection_menu.value;

    if (collection_id === '') {
        collection_show.innerHTML = '';
        return;
    }

    let collection_form =
        document.getElementById('delete_collection_form');

    collection_form.dataset.id = collection_id;

    if (collection_menu.options[collection_menu.selectedIndex].text.trim().toLowerCase() !== 'other') {
        let delete_collection_form =
            document.getElementById('delete_collection_form');

        delete_collection_form.classList.add('flex');
        delete_collection_form.classList.remove('hidden');
    }

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

// Collection Delete

let delete_collection_form = document.getElementById('delete_collection_form');
delete_collection_form.addEventListener('submit', async (event) => {
    event.preventDefault();

    collection_id = delete_collection_form.dataset.id;

    response = await fetch(`delete_collection/${collection_id}/`)

    if (response.ok) {
        const collection_option = document.getElementById(`Collection_${collection_id}`);
        collection_option.remove();
        delete_collection_form.classList.add('hidden');
        delete_collection_form.classList.remove('flex');
        collection_show.innerHTML = '';
    }
});
