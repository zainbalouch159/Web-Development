let i = -1;
let data;
let url = "https://dogapi.dog/api/v2/breeds";

let load = document.createElement("div")
load.id = "load"
load.innerHTML = `Loading....`
document.body.append(load)

let btn = document.createElement("button")
btn.id = "dog-fact"
btn.innerHTML = `Click to get dog facts`
document.body.append(btn);

let error1 = document.createElement("div")
error1.style.color = "red"
error1.style.display = "none"
document.body.append(error1);

let prev = document.createElement("button")
prev.style.margin = "5px"
prev.style.display = "none"
prev.innerHTML = `Previous`
document.body.append(prev)

    (async () => {
        try {
            btn.style.display = "none"
            let response = await fetch(url)
            if (response.ok) {
                data = await response.json()
                load.style.display = "none"
                btn.style.display = "block"
                console.log(data)
            } else {
                error1.innerText = `Server error: ${response.status}`
                error1.style.display = "block"
                load.style.display = "none"
            }
        }
        catch (error) {
            error1.innerText = `Network error`
            error1.style.display = "block"
            load.style.display = "none"
        }
    })()


btn.addEventListener("click", () => {
    i++
    if (i >= data.data.length) {
        i = 0
    }
    else if (i > 0) {
        prev.style.display = "block"
    }
    if (i <= 0) {
        prev.style.display = "none"
    }
    display()
})

function display() {
    let paraold = document.getElementById("des")
    let containerold = document.getElementById("container")

    if (containerold) {
        containerold.remove()
    }
    if (paraold) {
        paraold.remove()
    }

    let par = document.createElement("p")
    par.id = "des"
    par.innerHTML = `Dog name: <b>${data.data[i].attributes.name}</b> <br> <br>
        <b>Description</b> <br> <br>
        ${data.data[i].attributes.description} <br> <br> <b> Origin </b> <br> <br>
        Era: ${data.data[i].attributes.origin.era}<br>
        Region: ${data.data[i].attributes.origin.region} <br>
        Country: ${data.data[i].attributes.origin.country} <br><br>
        Other names: ${data.data[i].attributes.other_names.join(", ")}<br><br>
        Recognized by: ${data.data[i].attributes.recognized_by.join(", ")}<br><br> Images <br>
        `
    document.body.append(par)

    let images = data.data[i].attributes.images;
    if (images) {
        let container = document.createElement("div")
        container.id = "container"
        images.forEach(image => {
            let img = document.createElement("img")
            img.src = image.thumb
            container.append(img)
            
        });
        document.body.append(container)
    }
}

prev.addEventListener("click", () => {
    i--;

    display()
    if (i <= 0) {
        prev.style.display = "none"
    }
})