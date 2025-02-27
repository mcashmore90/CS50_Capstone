const DetailDescriptionScreen =({selectedPokemon, selectedTab})=>{
    return(
      <div className={`display-desc ${selectedTab === "desc" ? "" : "hide"}`}>
        {selectedPokemon.desc.toUpperCase()}
      </div>
    )
  }

  export default DetailDescriptionScreen;