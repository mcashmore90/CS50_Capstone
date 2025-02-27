import React, { useState, useEffect } from 'react';
import LeftPanelDisplay from './componets/LeftPanelDisplay'
import RightPanelDisplay from './componets/RightPanelDisplay';
import Navbar from './componets/Navbar';
import logo from './loading_icon.png';

function Pokedex() {
  const [currentIndex, setIndex] = React.useState(0);
  const [pokemonList, setPokemonList] = React.useState([]);
  const [selectedPokemon, setSelectedPokemon] = React.useState({});
  const [isViewDetail, setIsViewDetail] = React.useState(false)
  const [selectedTab, setSelectedTab] = React.useState("");
  const [isMoveDetail, setIsMoveDetail] = React.useState(false);
  const [isLoading, setIsLoading] = React.useState(true);

  useEffect(() => {
    fetch("/pokemon")
      .then((response) => response.json())
      .then((result) => {
        setPokemonList(result.data);
        setIsLoading(false);
      })
      .catch((error) => console.error("Error fetching data:", error));
  }, []);

  const selectNext = () => {
    setIndex((prevIndex) =>
      prevIndex < pokemonList.length - 1 ? prevIndex + 1 : prevIndex
    );
  };

  const selectPrevious = () => {
    setIndex((prevIndex) =>
      prevIndex > 0 ? prevIndex - 1 : prevIndex
    );
  };

  const selectItem = () => {
    setIsViewDetail((prevState) => {
      if (!prevState) { 
        fetch(`pokemon/${pokemonList[currentIndex].pokemonId}`)
          .then((response) => response.json())
          .then((result) => {
            setSelectedPokemon(result.pokemon);
          });
          selectTab('info');
      }
      else{
        setSelectedPokemon({});
        selectTab('');
      }
      return !prevState;
    });
      
  };

  const selectTab = (tab) => {
    setSelectedTab(tab);
    if(tab=="moves"){
      setIsMoveDetail(true)
    }
    else{
      setIsMoveDetail(false)
    }
  };

  if (isLoading) {
    return (<div>
        <img src={logo} className="loading-icon" alt="logo" />
    <div className='loading-text'>Loading Data...</div>
    </div>
);
  }

  return (    
    <div>
    <Navbar/>
    <div className="pokedex">
 
       <LeftPanelDisplay
        data={pokemonList}
        selectNext={selectNext}
        selectPrevious={selectPrevious}
        currentIndex={currentIndex}
        selectItem={selectItem}
        pokemonImage={selectedPokemon.image}
        isViewDetail={isViewDetail}
      />

      <RightPanelDisplay 
      selectedPokemon={selectedPokemon} 
      selectedTab={selectedTab} 
      selectTab={selectTab} 
      isMoveDetail={isMoveDetail} 
      isViewDetail={isViewDetail}/> 

    </div>
    </div>
  );
}

export default Pokedex;