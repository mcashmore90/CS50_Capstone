
function showRightPanel(){

    document.getElementById("right-panel").style.display = "block";
    document.getElementById("left-panel").style.display = "none";

    document.getElementById("nav-left-button").style.display="flex";
    document.getElementById("nav-right-button").style.display = "none";
}

function showLeftPanel(){

    document.getElementById("left-panel").style.display = "block";
    document.getElementById("right-panel").style.display = "none";

    document.getElementById("nav-right-button").style.display="flex";
    document.getElementById("nav-left-button").style.display = "none";
}