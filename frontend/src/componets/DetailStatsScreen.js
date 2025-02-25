const DetailStatsScreen=({stat, selectedTab})=>{
    return(
      <div className={`display-stats ${selectedTab === "stats" ? "" : "hide"}`}>
        <div>HEALTH: {stat.health}</div>
        <div>SP. ATK: {stat.sp_attack}</div>
        <div>ATK: {stat.attack}</div>
        <div>SP. DEF: {stat.sp_defence}</div>
        <div>DEF: {stat.defence}</div>
        <div>SPEED: {stat.speed}</div>
      </div>
    )
  }

  export default DetailStatsScreen;