const DetailInfoScreen=({selectedPokemon, selectedTab})=>{
    return(
      <div className={selectedTab === "info" ? "" : "hide"}>
        <div className="detail-info-screen">
          <div>{selectedPokemon.name.toUpperCase()} </div>
          <div># {selectedPokemon.number} </div>
          <div className="info-screen-types">
            {(selectedPokemon.types || []).map((type) => (
              <img src={type.image} className="icon-image" alt={type.name} key={type.name} />
            ))}
          </div>
      </div>
      <div>HEIGHT: {selectedPokemon.height} m</div>
      <div>WEIGHT: {selectedPokemon.weight} Kg</div>
      </div>
    )
  }

  export default DetailInfoScreen;