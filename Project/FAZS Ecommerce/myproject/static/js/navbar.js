searchicon = document.getElementById("search")
searchicon.addEventListener("click", () => {

      search_input.classList.toggle("translate-x-full");
    search_input.classList.toggle("translate-x-0");

    search_input.classList.toggle("opacity-0");
    search_input.classList.toggle("opacity-100");

    search_input.classList.toggle("pointer-events-none");


});