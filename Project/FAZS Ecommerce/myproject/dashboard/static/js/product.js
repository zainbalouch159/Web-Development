product_add_form = document.getElementById('product-add-form')
console.log('product.js')
product_add_form.addEventListener('submit',async (event)=>{
    event.preventDefault()
    product_add_overlay= document.getElementById('Overlay')
    product_add_overlay.classList.add('hidden')
    product_add_overlay.classList.remove('flex')

    formdata =new FormData(product_add_form)

    response = await fetch(product_add_form.action,{
        method:'POST',
        body: formdata
    })
    data = await response.json()

    product_show = document.getElementById('product_show')
    product_section = document.createElement('div')
    product_section.classList.add('h-10', 'bg-orange-200', 'p-2', 'm-2', 'rounded', 'flex', 'justify-between')
    product_show.append(product_section)
    
    img_div= document.createElement('div')
    img_div.classList.add('flex', 'gap-2')
    product_section.append(img_div)

    product_img = document.createElement('img')
    product_img.classList.add('h-full', 'object-contain', 'rounded')
    product_img.src = data.image
    img_div.append(product_img)

    product_name = document.createElement('span')
    product_name.classList.add('text-orange-500')
    product_name.textContent= data.name
    img_div.append(product_name)

    right_div = document.createElement('div')
    right_div.classList.add('flex', 'gap-1', 'text-orange-500')
    product_section.append(right_div)

    price = document.createElement('span')
    price.textContent=`Rs ${data.price}`
    right_div.append(price)

    stock = document.createElement('span')
    stock.textContent=`Stock ${data.stock}`
    right_div.append(stock)

    sales = document.createElement('span')
    sales.textContent=`Sales ${data.sales}`
    right_div.append(sales)

    edit = document.createElement('a')
    edit.classList.add('fa-solid', 'fa-pencil')
    right_div.append(edit)

    product_delete = document.createElement('a')
    product_delete.classList.add('text-red-500')
    product_delete.href=`product_delete/${data.id}/`
    right_div.append(product_delete)

    delelte_symbol = document.createElement('i')
    delelte_symbol.classList.add('fa-solid', 'fa-trash')
    product_delete.append(delelte_symbol)
})