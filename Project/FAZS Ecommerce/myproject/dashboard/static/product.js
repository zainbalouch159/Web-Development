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
    
})