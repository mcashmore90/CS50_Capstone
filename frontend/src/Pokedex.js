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
  const [isLoadingPage, setIsLoadingPage] = React.useState(false);
  const [paging, setPaging] = React.useState({});


  const [isRightPanelVisible, setRightPanelVisible] = useState(true);
  const [isLeftPanelVisible, setLeftPanelVisible] = useState(true);
  const [isNavLeftButtonVisible, setNavLeftButtonVisible] = useState(false);
  const [isNavRightButtonVisible, setNavRightButtonVisible] = useState(true);


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
      setIsLoadingPage(true);
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
          setIsLoadingPage(false);
        });}
    }
  };

  const selectPrevious = () => {
    if (currentIndex > 0) {
      setIndex(currentIndex - 1);
    } else {
      if(paging.hasPrevious){
      setIsLoadingPage(true);
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
          setIsLoadingPage(false);
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

  const showLeftPanel =()=>{
    setRightPanelVisible(false);
    setLeftPanelVisible(true);
    setNavLeftButtonVisible(false);
    setNavRightButtonVisible(true);
  }

  const showRightPanel =()=>{
    setRightPanelVisible(true);
    setLeftPanelVisible(false);
    setNavLeftButtonVisible(true);
    setNavRightButtonVisible(false);
  }

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
        isLoadingPage={isLoadingPage}
        isLeftPanelVisible={isLeftPanelVisible}
      />

      <RightPanelDisplay 
      selectedPokemon={selectedPokemon} 
      selectedTab={selectedTab} 
      selectTab={selectTab} 
      isMoveDetail={isMoveDetail} 
      isViewDetail={isViewDetail}
      isRightPanelVisible ={isRightPanelVisible}/> 

    </div>
    </div>
  );
}

export default Pokedex;