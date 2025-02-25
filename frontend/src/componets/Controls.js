const Controls = ({
    selectNext,
    selectPrevious,
    selectItem,
    isViewDetail,
  }) => {
    return (
      <div className="controls">
        <div className="select-btn hoverable" onClick={selectItem}>{isViewDetail?"BACK":"ENTER"}</div>
        <div className="middle-control">
          <div className="bar">
            <div className="red-bar"></div>
            <div className="blue-bar"></div>
          </div>
          <div className="green-box"></div>
        </div>
        <div className="dpad-control">
          <div></div>
          <div className={`dpad-up ${!isViewDetail?"hoverable":""}`} onClick={!isViewDetail ? selectPrevious : null} >
            <div className="dpad-arrow-outline-up">
              <div className="dpad-arrow-up"></div>
            </div>
          </div>
          <div></div>
          <div className="dpad-left">
            <div className="dpad-arrow-outline-left">
              <div className="dpad-arrow-left"></div>
            </div>
          </div>
          <div className="dpad-middle">
            <div className="dpad-circle"></div>
          </div>
          <div className="dpad-right">
            <div className="dpad-arrow-outline-right">
              <div className="dpad-arrow-right"></div>
            </div>
          </div>
          <div></div>
          <div className={`dpad-down ${!isViewDetail?"hoverable":""}`} onClick={!isViewDetail ? selectNext: null}>
            <div className="dpad-arrow-outline-down">
              <div className="dpad-arrow-down"></div>
            </div>
          </div>
          <div></div>
        </div>
      </div>
    );
  };


  export default Controls;