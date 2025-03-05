
import React, { useRef, useEffect } from 'react'
const Screen = ({ data, currentIndex, pokemonImage }) => {
    const itemRefs = useRef([]);

  useEffect(() => {
    if (itemRefs.current[currentIndex]) {
      itemRefs.current[currentIndex].scrollIntoView({
        behavior: 'smooth',
        block: 'nearest',
      });
    }
  }, [currentIndex, pokemonImage]);

    return (
      <div className="screen">
          <img className={`pokemonImage ${pokemonImage? "":"hide"}`}  src={pokemonImage} alt="Pokemon" />
          <div className={`list ${pokemonImage? "hide":""}`}>
          {data.map((item, index) => (
            <div
              key={index}
              ref={(el) => (itemRefs.current[index] = el)}
              className={`${index === currentIndex ? 'select-item' : ''}`}
            >
              {item.pokemonName.toUpperCase()}
            </div>
          ))}
        </div>
      </div>
    );
  };

export default Screen;