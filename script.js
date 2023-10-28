document.querySelectorAll['.sidebar-dropdown-toggle'].ForEach(function(item){
    item.addEventListener('click', function(e){
        e.preventDefault()
        const parent = item.closest('.group')
        parent.classList.add('.selected') 

    })
})

console.log("Hello world")