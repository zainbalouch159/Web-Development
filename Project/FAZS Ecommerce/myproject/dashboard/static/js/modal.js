document.addEventListener('DOMContentLoaded', () => {

    // 1. Product add overlay elements
    const productAddBtn = document.getElementById('Product-add');
    const overlay = document.getElementById('Overlay');

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
    const categoryAddBtn = document.getElementById('add-category-button');
    const categoryAddOverlay = document.getElementById('Category-add-Overlay');

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

    document.getElementById('cagtegory-submit').addEventListener('click',()=>{
        categoryAddOverlay.classList.remove('flex');
                categoryAddOverlay.classList.add('hidden');
                document.getElementById('category-menu').classList.add('hidden')
    })
});