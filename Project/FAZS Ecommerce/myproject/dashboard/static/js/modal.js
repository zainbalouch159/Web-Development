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

// Category Add Overlay in product
let categoryAddBtnedit = document.getElementById('add-category-button-product-edit');
let categoryAddBtnadd = document.getElementById('add-category-button-product-add');
let categoryAddOverlay = document.getElementById('Category-add-Overlay-product');

// Category Add overlay
categoryAddOverlay.addEventListener('click', (event) => {
    if (event.target === categoryAddOverlay) {
        categoryAddOverlay.classList.remove('flex');
        categoryAddOverlay.classList.add('hidden');
    }
});

// For category Add Overlay in product edit form
categoryAddBtnedit.addEventListener('click', () => {
    form = document.getElementById('category-add-form-product');
    form.dataset.data = 'edit';
    categoryAddOverlay.classList.add('flex');
    categoryAddOverlay.classList.remove('hidden');

});

// For category Add Overlay in product add form

categoryAddBtnadd.addEventListener('click', () => {
    form = document.getElementById('category-add-form-product');
    form.dataset.data = 'add';
    categoryAddOverlay.classList.add('flex');
    categoryAddOverlay.classList.remove('hidden');

});

// Collections Add Overlay in Product
let CollectionsAddBtnedit = document.getElementById('add-Collections-button-product-edit');
let CollectionsAddBtnadd = document.getElementById('add-Collections-button-product-add');
let CollectionsAddOverlayproduct = document.getElementById('Collections-add-Overlay-product');
let CollectionsAddFormproduct = document.getElementById('Collections-add-form-product');
// Collections add overlay in Product 
CollectionsAddOverlayproduct.addEventListener('click', (event) => {
    if (event.target === CollectionsAddOverlayproduct) {
        CollectionsAddOverlayproduct.classList.remove('flex');
        CollectionsAddOverlayproduct.classList.add('hidden');
    }
});

// Collection add in product edit form 
CollectionsAddBtnedit.addEventListener('click', () => {
    CollectionsAddFormproduct.dataset.data = 'edit';
    CollectionsAddOverlayproduct.classList.add('flex');
    CollectionsAddOverlayproduct.classList.remove('hidden');
});

// Collection add in product add form 
CollectionsAddBtnadd.addEventListener('click', () => {
    CollectionsAddFormproduct.dataset.data = 'add';
    CollectionsAddOverlayproduct.classList.add('flex');
    CollectionsAddOverlayproduct.classList.remove('hidden');
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

// Product Edit Overlay Close
let product_edit_overlay = document.getElementById('Edit_Product_Overlay');

product_edit_overlay.addEventListener('click', (event) => {

    if (event.target === product_edit_overlay) {
        product_edit_overlay.classList.add('hidden');
        product_edit_overlay.classList.remove('flex');
    }
});

// Collection Add Overlay in collection section
let collectionAddBtn = document.getElementById('collection_add_btn');
let collectionAddOverlay = document.getElementById('Collection-add-Overlay_collection');

collectionAddBtn.addEventListener('click', () => {
    collectionAddOverlay.classList.add('flex');
    collectionAddOverlay.classList.remove('hidden');
});

collectionAddOverlay.addEventListener('click', (event) => {
    if (event.target === collectionAddOverlay) {
        collectionAddOverlay.classList.remove('flex');
        collectionAddOverlay.classList.add('hidden');
    }
});