document.addEventListener('DOMContentLoaded', function(){
    console.log("hello world")
})

function callNextApi(index){
    return fetch("/pokemon-next",{
        method: 'POST',
        headers:{
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            currentIndex:index
        }),})
    .then(response=>response.json())
    .then(result=>{return result} )
}

function display(pokemon){
    section = document.getElementById('detail')

    section.innerHTML = pokemon.name
}


// Function to get CSRF token from cookies - 'csrftoken'
//Provided by Microsoft Copilot
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}