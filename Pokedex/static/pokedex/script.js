document.addEventListener('DOMContentLoaded', function(){
    console.log("hello world")
    highlightItem(selectIndex)
})

selectIndex = 0;

function selectNext(){
    selectIndex+=1;
    console.log(selectIndex)
    if(selectIndex>4){
        console.log('at limit')
        selectIndex = 0
        getNextSection()
    }
    else{
        highlightItem(selectIndex)
    }
    
}

function selectPrevious(){
    selectIndex-=1;
    if(selectIndex<0)
    {
        selectIndex = 4
        getPreviousSection()

    }
    highlightItem(selectIndex)
}

function highlightItem(index){
    items = document.querySelectorAll('.item')
    items.forEach(item => item.classList.remove('selected'));
    items[index].classList.add('selected');
}

function getNextSection(){
    console.log('getting next')
    fetch('/update_selection', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify(
            offset = 5
        )
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        display = document.getElementById('listDisplay')
        display.innerHTML = ""

        data.newList.forEach((element,value) => {
            item = document.createElement('li')
            item.innerText = element.name;
            item.className="item"
            display.appendChild(item)
        });
        
        highlightItem(selectIndex)
    }
    
)}

function getPreviousSection(){
    console.log('getting next')
    fetch('/update_selection', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify(
            offset = -5
        )
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        display = document.getElementById('listDisplay')
        display.innerHTML = ""

        data.newList.forEach((element,value) => {
            item = document.createElement('li')
            item.innerText = element.name;
            item.className="item"
            display.appendChild(item)
        });
        
        highlightItem(selectIndex)
    }
    
)}


function updateList(){

}

// Function to get CSRF token from cookies
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