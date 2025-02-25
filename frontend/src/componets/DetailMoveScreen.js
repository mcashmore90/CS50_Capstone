import React from 'react';

const DetailMoveScreen=({moves, selectedTab, moveIndex,isMoreInfo})=>{
    return(
      <div className={`${selectedTab === "moves" ? "" : "hide"}`}>
        
        {(moves|| []).map((move, index) => (
          <React.Fragment>
          <div className={`${index===moveIndex && isMoreInfo? "":"hide"}`}>{move.description}</div>
          <div className={`display-stats ${index === moveIndex  && !isMoreInfo? "" : "hide"}`}>
            
              <div>{move.name}</div>
              <img src={move.type.image} className="icon-image" alt={move.type.name} />
            <div>ACC: {move.accuracy}</div>      
            <div>PP: {move.pp}</div>
          <div>POWER: {move.power}</div>       
          </div>
        </React.Fragment>
        ))} 
    </div>
    )
  }

  export default DetailMoveScreen;