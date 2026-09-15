product_add_form = document.getElementById('product-add-form')
product_add_form.addevetListener('click',async (event)=>{
    event.preventdefault()
    product_add_overlay= document.getElementById('Overlay')
    product_add_overlay.classlist.add('hidden')
    product_add_overlay.classlist.remove('flex')

    formdata = FormData(product_add_form)

    response = await fetch(product_add_form.action,{
        mehtod:'POST',
        body: formdata
    })
    data = await response.json()

    product_section = document.getElementById('product_section')
    container_div=document.createElement('div')
    container_div.classlist.add('h-10', 'bg-orange-200',  'p-2', 'm-2', 'rounded', 'flex', 'justify-between', 'gap-1')
    product_section.append(container_div)
    
    img_div= document.createElement('div')
    img_div.classlist.add('flex', 'gap-2')
    container_div.append(img_div)

    product_img = document.createElement('img')
    product_img.classlist.add('h-full', 'object-contain', 'rounded')
    product_img.src = data.image
    img_div.append(product_img)

    product_name = document.createElement('span')
    product_name.classlist.add('text-orange-500')
    product_name.textContent=`Rs ${data.name}`
    img_div.append(product_name)

    right_div = document.createElement('div')
    right_div.classlist.add('flex', 'gap-1', 'text-orange-500')
    product_section.append(right_div)

    price = document.createElement('span')
    price.textContent=data.price
    right_div.append(price)

    sales = document.createElement('span')
    sales.textContent=data.sales
    right_div.append(sales)

    edit = document.createElement('a')
    edit.href=`/product_edit/${data.id}`
    edit.classlist.add('fa-solid fa-pencil')
    right_div.append(edit)

    product_delete = document.createElement('span')
    product_delete.href=`/product_delelte/${data.id}`
    product_delete.classlist.add('text-red-500')
    right_div.append(product_delete)

    delelte_symbol = document.createElement('i')
    delelte_symbol.classlist.add('fa-solid fa-pencil')
    product_delete.append(delelte_symbol)
})