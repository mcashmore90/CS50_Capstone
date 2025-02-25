function DetailControls({ selectTab, selectedTab,isViewDetail }) {
    return (
      <div className="blue-btn-layout">
        <div className={`${selectedTab==="info"? "selected-blue-btn":""} blue-button-info ${isViewDetail?"hoverable":""}`} onClick={isViewDetail?() => selectTab("info"):null}>
          {isViewDetail?"INFO":""}
        </div>
        <div className={`${selectedTab==="desc"? "selected-blue-btn":""} blue-button-desc ${isViewDetail?"hoverable":""}`} onClick={isViewDetail?() => selectTab("desc"):null}>
          {isViewDetail?"DESC.":""} 
        </div>
        <div className={`${selectedTab==="stats"? "selected-blue-btn":""} blue-button-stats ${isViewDetail?"hoverable":""}`} onClick={isViewDetail?() => selectTab("stats"):null}>
          {isViewDetail?"STATS":""}
        </div>
        <div className={`${selectedTab==="moves"? "selected-blue-btn":""} blue-button-moves ${isViewDetail?"hoverable":""}`} onClick={isViewDetail?() => selectTab("moves"):null}>
          {isViewDetail?"MOVES":""}
        </div>
        <div className="blue-button"></div>
        <div className="blue-button"></div>
        <div className="blue-button"></div>
        <div className="blue-button"></div>
        <div className="blue-button"></div>
        <div className="blue-button"></div>
      </div>
    );
  }


  export default DetailControls;