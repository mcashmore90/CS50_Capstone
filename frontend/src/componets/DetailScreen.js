import React from "react";
import DetailInfoScreen from "./DetailInfoScreen";
import DetailDescriptionScreen from "./DetailDescriptionScreen";
import DetailStatsScreen from "./DetailStatsScreen";
import DetailMoveScreen from "./DetailMoveScreen";

const DetailScreen=({ selectedTab, selectedPokemon, moveIndex,isMoreInfo })=> {

    return (
      <div className="detail-screen">
        
        {selectedPokemon  && Object.keys(selectedPokemon).length > 0 &&(
        <React.Fragment>
          <DetailInfoScreen selectedTab={selectedTab} selectedPokemon={selectedPokemon}/>
          <DetailDescriptionScreen selectedTab={selectedTab} selectedPokemon={selectedPokemon}/>
          <DetailStatsScreen selectedTab={selectedTab} stat={selectedPokemon}/>
          <DetailMoveScreen selectedTab={selectedTab} moves={selectedPokemon.moves} moveIndex={moveIndex} isMoreInfo={isMoreInfo}/>
        </React.Fragment>
        )}
      </div>
  )
  }

  export default DetailScreen;