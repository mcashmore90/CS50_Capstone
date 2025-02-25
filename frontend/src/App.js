import logo from './logo.svg';
import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [currentIndex, setIndex] = React.useState(0);
  const [pokemonList, setPokemonList] = React.useState([]);
  const [selectedPokemon, setSelectedPokemon] = React.useState({});
  const [isViewDetail, setIsViewDetail] = React.useState(false)
  const [selectedTab, setSelectedTab] = React.useState("");
  const [isMoveDetail, setIsMoveDetail] = React.useState(false);
  const [isLoading, setIsLoading] = React.useState(true);
  const [paging, setPaging] = React.useState({});

  useEffect(() => {
    fetch("/pokemon")
      .then((response) => response.json())
      .then((result) => {
        setPokemonList(result.data.pokemon);
        setPaging({
          hasNext: result.data.hasNext,
          hasPrevious: result.data.hasPrevious,
          nextPageNumber: result.data.nextPageNumber,
          previousPageNumber: result.data.previousPageNumber
        })
        setIsLoading(false);
      })
      .catch((error) => console.error("Error fetching data:", error));
  }, []);

  const selectNext = () => {
    if (currentIndex < pokemonList.length - 1) {
      setIndex(currentIndex + 1);
    } else {
      if(paging.hasNext)
      {
      fetch(`/pokemon?page=${paging.nextPageNumber}`)
        .then((response) => response.json())
        .then((result) => {
          setPaging({
            hasNext: result.data.hasNext,
            hasPrevious: result.data.hasPrevious,
            nextPageNumber: result.data.nextPageNumber,
            previousPageNumber: result.data.previousPageNumber
          })
          setIndex(0)
          setPokemonList(result.data.pokemon);
        });}
    }
  };

  const selectPrevious = () => {
    if (currentIndex > 0) {
      setIndex(currentIndex - 1);
    } else {
      if(paging.hasPrevious){
      fetch(`/pokemon?page=${paging.previousPageNumber}`)
        .then((response) => response.json())
        .then((result) => {
          setIndex(result.data.pokemon.length-1);
          setPokemonList(result.data.pokemon);
          setPaging({
            hasNext: result.data.hasNext,
            hasPrevious: result.data.hasPrevious,
            nextPageNumber: result.data.nextPageNumber,
            previousPageNumber: result.data.previousPageNumber
          })
        });}
    }
  };

  const selectItem = () => {
    setIsViewDetail((prevState) => {
      if (!prevState) { 
        fetch(`pokemon/${pokemonList[currentIndex].pokemonId}`)
          .then((response) => response.json())
          .then((result) => {
            console.log(result.pokemon)
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
    return <div>Loading Data...</div>;
  }

  return (
    <div className="pokedex">
      <p>testing react componets</p>
      {/* <LeftPanelDisplay
        data={pokemonList}
        selectNext={selectNext}
        selectPrevious={selectPrevious}
        currentIndex={currentIndex}
        selectItem={selectItem}
        pokemonImage={selectedPokemon.image}
        isViewDetail={isViewDetail}
      />

      <RightPanelDisplay selectedPokemon={selectedPokemon} selectedTab={selectedTab} selectTab={selectTab} isMoveDetail={isMoveDetail} isViewDetail={isViewDetail}/> */}
    </div>
  );
}

export default App;
