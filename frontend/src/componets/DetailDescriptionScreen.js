const DetailDescriptionScreen =({selectedPokemon, selectedTab})=>{
    return(
      <div className={`display-desc ${selectedTab === "desc" ? "" : "hide"}`}>
        {selectedPokemon.desc}
      </div>
    )
  }

  export default DetailDescriptionScreen;