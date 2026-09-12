const productAddBtn = document.getElementById('Product-add');
const overlay = document.getElementById('Overlay');


    // 1. Product add overlay elements

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

    // 2. Category add overlay elements
     categoryAddBtn = document.getElementById('add-category-button');
     categoryAddOverlay = document.getElementById('Category-add-Overlay');

    if (categoryAddBtn && categoryAddOverlay) {
        console.log('category')
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



// Category submit

category_form = document.getElementById('category-add-form')

category_form.addEventListener('submit', async (event) => {

    event.preventDefault()

    categoryAddOverlay.classList.remove('flex');
    categoryAddOverlay.classList.add('hidden');

    formdata = new FormData(category_form)

     response = await fetch(category_form.action, {
        method: 'POST',
        body: formdata
    })
    data = await response.json()

    new_category_option = document.createElement('option')

    new_category_option.value = data.id
    new_category_option.textContent = data.name

    category_menubar = document.getElementById('category-menu')

    category_menubar.appendChild(new_category_option)

    new_category_option.selected = true
})

    // 2. Collections add overlay elements
     CollectionsAddBtn = document.getElementById('add-Collections-button');
     CollectionsAddOverlay = document.getElementById('Collections-add-Overlay');

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



// Collections submit

Collections_form = document.getElementById('Collecitons-add-form')

Collections_form.addEventListener('submit', async (event) => {

    event.preventDefault()

    CollectionsAddOverlay.classList.remove('flex');
    CollectionsAddOverlay.classList.add('hidden');

    formdata = new FormData(Collections_form)

     response = await fetch(Collections_form.action, {
        method: 'POST',
        body: formdata
    })
    data = await response.json()

    new_Collections_option = document.createElement('option')

    new_Collections_option.value = data.id
    new_Collections_option.textContent = data.name

    Collections_menubar = document.getElementById('Collections-menu')

    Collections_menubar.appendChild(new_Collections_option)

    new_Collections_option.selected = true
})