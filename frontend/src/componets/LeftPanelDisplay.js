import Screen from './Screen';
import Controls from './Controls';

const LeftPanelDisplay = ({
    data,
    selectNext,
    selectPrevious,
    currentIndex,
    selectItem,
    pokemonImage,
    isViewDetail
  }) => {
    return (
      <div class="left-panel" id="left-panel" >
        <div class="top-shadow">
          <div class="top-bar">
            <div class="light-layout">
              <div class="blue-frame">
                <div class="blue-light"></div>
              </div>

              <div class="red-light"></div>
              <div class="yellow-light"></div>
              <div class="green-light"></div>
            </div>
          </div>
        </div>
        <div class="left-panel-layout">
          <div class="left-layout">
            <div class="display-shadow">
            <div class="display">
              <div class="display-top">
                <div class="red-dot"></div>
                <div class="red-dot"></div>
              </div>
              <Screen
                data={data}
                currentIndex={currentIndex}
                pokemonImage={pokemonImage}
                isViewDetail={isViewDetail}
              />
              <div class="display-bottom">
                <div class="bottom-red-dot"></div>
                <div>
                  <div class="grill"></div>
                  <div class="grill"></div>
                  <div class="grill"></div>
                  <div class="grill"></div>
                </div>
              </div>
            </div>
            </div>
            <Controls
              selectNext={selectNext}
              selectPrevious={selectPrevious}
              selectItem={selectItem}
              isViewDetail={isViewDetail}
            />
          </div>

          <div class="side-hinge">
            <div class="top-hinge"></div>
            <div class="bottom-hinge"></div>
          </div>
        </div>
      </div>
    );
  };

  export default LeftPanelDisplay;