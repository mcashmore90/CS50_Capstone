import React, { useEffect } from 'react';

const Navbar = () => {
  useEffect(() => {
    const rightButton = document.getElementById('nav-right-button');
    rightButton.onclick = function() {

        document.getElementById("right-panel").style.display = "block";
        document.getElementById("left-panel").style.display = "none";
        document.getElementById("nav-left-button").style.display = "flex";
        document.getElementById("nav-right-button").style.display = "none";
    };

    const leftButton = document.getElementById('nav-left-button');
    leftButton.onclick = function() {

        document.getElementById("left-panel").style.display = "block";
        document.getElementById("right-panel").style.display = "none";
        document.getElementById("nav-right-button").style.display = "flex";
        document.getElementById("nav-left-button").style.display = "none";
    };
  }, []);

  return (
    <div class="navbar">
    <div class="nav-left-button" id="nav-left-button" >&lt;&lt;</div>
    <div class="nav-right-button" id="nav-right-button">&gt;&gt;</div>
    </div>
  );
}

export default Navbar;