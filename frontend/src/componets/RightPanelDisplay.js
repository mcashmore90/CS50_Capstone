import React, { useState, useEffect } from 'react';
import DetailScreen from './DetailScreen';
import DetailControls from './DetailControls';
import DetailScreenControls from './DetailScreenControls';

const RightPanelDisplay = ({selectedPokemon,selectedTab,selectTab,isMoveDetail,isViewDetail}) =>{
    const { useState,useEffect } = React;
    const [moveIndex, setMoveIndex] = useState(0);
    const [isMoreInfo, setIsMoreInfo] = useState(false)

    useEffect(()=>{
      setMoveIndex(0);
      setIsMoreInfo(false)
    },[selectedPokemon, selectedTab]);

    const selectNextMove=()=>{
      if(moveIndex < selectedPokemon.moves.length-1)
      {
        setMoveIndex(moveIndex+1)
      }
    }

    const selectPreviousMove=()=>{
      if(moveIndex > 0)
      {
        setMoveIndex(moveIndex-1)
      }
    }

    const showMore=()=>{
      setIsMoreInfo((prevState)=>{
        return !prevState
      })
    }

    return (
      <div className="right-panel" id="right-panel">
        <div className="top-outline">
          <div className="top-bg"></div>
        </div>
        <div className="right-panel-body">
          <div className="right-layout">
            <DetailScreen selectedTab={selectedTab} selectedPokemon={selectedPokemon} moveIndex={moveIndex} isMoreInfo={isMoreInfo}/>
            <DetailControls selectTab={selectTab} selectedTab={selectedTab} isViewDetail={isViewDetail}/>
            <div className="right-top-btn">
              <div className="top-red-lights">
                <div className="top-red-light"></div>
                <div className="top-red-light"></div>
              </div>
              <div className="top-black-bars">
                <div className="top-black-bar"></div>
                <div className="top-black-bar"></div>
              </div>
            </div>
            <DetailScreenControls selectNextMove={selectNextMove} selectPreviousMove={selectPreviousMove} showMore={showMore} isMoveDetail={isMoveDetail}/>
            <div className="right-bottom-btn">
              <div className="bottom-btn"></div>
              <div className="bottom-btn"></div>
            </div>
          </div>
        </div>
      </div>
    );
  }

  export default RightPanelDisplay;