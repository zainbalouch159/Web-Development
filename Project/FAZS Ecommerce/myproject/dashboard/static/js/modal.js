let productAddBtn = document.getElementById('Product-add');
let overlay = document.getElementById('Overlay');

// Product Add Overlay
if (productAddBtn && overlay) {
    productAddBtn.addEventListener('click', () => {
        overlay.classList.add('flex');
        overlay.classList.remove('hidden');
    });

    overlay.addEventListener('click', (event) => {
        if (event.target === overlay) {
            overlay.classList.remove('flex');
            overlay.classList.add('hidden');
        }
    });
}

// Category Add Overlay in product add form
let categoryAddBtn = document.getElementById('add-category-button');
let categoryAddOverlay = document.getElementById('Category-add-Overlay');

if (categoryAddBtn && categoryAddOverlay) {
    categoryAddBtn.addEventListener('click', () => {
        categoryAddOverlay.classList.add('flex');
        categoryAddOverlay.classList.remove('hidden');
    });

    categoryAddOverlay.addEventListener('click', (event) => {
        if (event.target === categoryAddOverlay) {
            categoryAddOverlay.classList.remove('flex');
            categoryAddOverlay.classList.add('hidden');
        }
    });
}

// Category Submit in product add form
let category_form = document.getElementById('category-add-form');

category_form.addEventListener('submit', async (event) => {

    event.preventDefault();

    categoryAddOverlay.classList.remove('flex');
    categoryAddOverlay.classList.add('hidden');

    let formdata = new FormData(category_form);

    let response = await fetch(category_form.action, {
        method: 'POST',
        body: formdata
    });

    let data = await response.json();

    let new_category_option = document.createElement('option');

    new_category_option.value = data.id;
    new_category_option.textContent = data.name;

    let category_menubar = document.getElementById('category-menu');

    category_menubar.appendChild(new_category_option);

    new_category_option.selected = true;
});

// Category Add Overlay in category section
let categoryAddBtn1 = document.getElementById('category_add_btn');
let categoryAddOverlay1 = document.getElementById('Category-add-Overlay_categorty_section');

if (categoryAddBtn1) {
    categoryAddBtn1.addEventListener('click', () => {
        categoryAddOverlay1.classList.add('flex');
        categoryAddOverlay1.classList.remove('hidden');
    });

    categoryAddOverlay1.addEventListener('click', (event) => {
        if (event.target === categoryAddOverlay1) {
            categoryAddOverlay1.classList.remove('flex');
            categoryAddOverlay1.classList.add('hidden');
        }
    });
}



// Collections Add Overlay
let CollectionsAddBtn = document.getElementById('add-Collections-button');
let CollectionsAddOverlay = document.getElementById('Collections-add-Overlay');

if (CollectionsAddBtn && CollectionsAddOverlay) {

    CollectionsAddBtn.addEventListener('click', () => {
        console.log("Collection add button clicked");

        CollectionsAddOverlay.classList.add('flex');
        CollectionsAddOverlay.classList.remove('hidden');
    });

    CollectionsAddOverlay.addEventListener('click', (event) => {
        if (event.target === CollectionsAddOverlay) {
            CollectionsAddOverlay.classList.remove('flex');
            CollectionsAddOverlay.classList.add('hidden');
        }
    });
}


// Collections Submit
let Collections_form = document.getElementById('Collections-add-form');

Collections_form.addEventListener('submit', async (event) => {

    event.preventDefault();

    CollectionsAddOverlay.classList.remove('flex');
    CollectionsAddOverlay.classList.add('hidden');

    let formdata = new FormData(Collections_form);

    let response = await fetch(Collections_form.action, {
        method: 'POST',
        body: formdata
    });

    let data = await response.json();

    let new_Collections_option = document.createElement('option');

    new_Collections_option.value = data.id;
    new_Collections_option.textContent = data.title;

    let Collections_menubar = document.getElementById('Collections-menu');

    Collections_menubar.appendChild(new_Collections_option);

    new_Collections_option.selected = true;
});

// Product Edit Overlay Close
let product_edit_overlay = document.getElementById('Edit_Product_Overlay');

product_edit_overlay.addEventListener('click', (event) => {

    if (event.target === product_edit_overlay) {
        product_edit_overlay.classList.add('hidden');
        product_edit_overlay.classList.remove('flex');
    }
});


// Product Edit
let product_edit = document.querySelectorAll('.product_edit_button');

product_edit.forEach(product => {

    product.addEventListener('click', async () => {

        let product_edit_overlay = document.getElementById('Edit_Product_Overlay');

        product_edit_overlay.classList.add('flex');
        product_edit_overlay.classList.remove('hidden');

        let id = product.dataset.id;

        let response = await fetch(`product_edit/${id}/`);
        let data = await response.json();

        let form = document.getElementById('product-edit-form');
        input = document.createElement('input')
        input.value=id
        input.name='product_id'
        input.classList.add('hidden')
        form.append(input)

        let name = document.getElementById('product-name-update');
        name.value = data.name;

        let description = document.getElementById('product-description-update');
        description.value = data.description;

        let stock = document.getElementById('product-stock-update');
        stock.value = data.stock;

        let discount = document.getElementById('product-discount-update');
        discount.value = data.discount;

        let info = document.getElementById('product-info-update');
        info.value = data.info;

        let image = document.getElementById('product-image-preview');
        image.src = data.image;

        let price = document.getElementById('product-price-update');
        price.value = data.price;


        let category = document.getElementById('product-category-update');
        category.value = data.category;

        let collections = document.getElementById('product-collections-update');

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


