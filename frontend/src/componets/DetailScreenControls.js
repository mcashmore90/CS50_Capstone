const DetailScreenControls=({selectNextMove,selectPreviousMove,showMore,isMoveDetail})=>{
    return(
      <div className="right-middle-btn">
        <div className="white-btns">
          <div className={`white-btn ${isMoveDetail?"hoverable":""}`} onClick={isMoveDetail?selectPreviousMove:null}>{isMoveDetail?"PREV.":""}</div>
          <div className={`white-btn ${isMoveDetail?"hoverable":""}`} onClick={isMoveDetail?selectNextMove:null}>{isMoveDetail?"NEXT":""}</div>
        </div>
        <div className={`yellow-btn ${isMoveDetail?"hoverable":""}`} onClick={isMoveDetail?showMore:null}>{isMoveDetail?"MORE":""}</div>
      </div>
    )
  }
  

  export default DetailScreenControls;