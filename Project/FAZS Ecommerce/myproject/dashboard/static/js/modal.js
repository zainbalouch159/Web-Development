// Product Add
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

// Category Add Overlay in product edit form
let categoryAddBtn = document.getElementById('add-category-button-product');
let categoryAddOverlay = document.getElementById('Category-add-Overlay-product');

if (categoryAddBtn && categoryAddOverlay) {

    categoryAddBtn.addEventListener('click', () => {
        form = document.getElementById('category-add-form-product');
        form.dataset.data = 'edit';
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


// Product Edit Overlay Close
let product_edit_overlay = document.getElementById('Edit_Product_Overlay');

product_edit_overlay.addEventListener('click', (event) => {

    if (event.target === product_edit_overlay) {
        product_edit_overlay.classList.add('hidden');
        product_edit_overlay.classList.remove('flex');
    }
});



