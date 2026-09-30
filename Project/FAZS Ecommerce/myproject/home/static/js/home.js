

function updateArrows() {

    document.querySelectorAll('.carousel-wrapper').forEach(wrapper => {

        const row = wrapper.querySelector('.horizontal-row');
        const leftArrow = wrapper.querySelector('.left-arrow');
        const rightArrow = wrapper.querySelector('.right-arrow');

        if (!row || !leftArrow || !rightArrow) {
            return;
        }

        const hasOverflow =
            row.scrollWidth > row.clientWidth + 1;


        /* No overflow = no arrows */

        if (!hasOverflow) {

            leftArrow.classList.add('hidden');
            rightArrow.classList.add('hidden');

            return;
        }


        /* Overflow exists */

        rightArrow.classList.remove('hidden');


        /* Left arrow */

        if (row.scrollLeft <= 1) {
            leftArrow.classList.add('hidden');
        } else {
            leftArrow.classList.remove('hidden');
        }


        /* Right arrow */

        if (
            row.scrollLeft + row.clientWidth
            >= row.scrollWidth - 1
        ) {
            rightArrow.classList.add('hidden');
        } else {
            rightArrow.classList.remove('hidden');
        }

    });

}



function scrollRow(button, direction) {

    const wrapper =
        button.closest('.carousel-wrapper');

    const row =
        wrapper.querySelector('.horizontal-row');


    row.scrollBy({
        left: direction * 320,
        behavior: 'smooth'
    });


    /*
       Arrow state update after
       smooth scrolling
    */

    setTimeout(updateArrows, 350);

}



document.querySelectorAll('.horizontal-row').forEach(row => {

    row.addEventListener('scroll', updateArrows);

});


window.addEventListener('load', updateArrows);

window.addEventListener('resize', updateArrows);
