document.addEventListener('DOMContentLoaded', function(){
    console.log("hello world")
})


function display(pokemon){
    section = document.getElementById('detail')

    section.innerHTML = pokemon.name
}