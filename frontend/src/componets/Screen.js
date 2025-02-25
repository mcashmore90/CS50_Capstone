import logo from '../loading_icon.png';

const Screen = ({ data, currentIndex, pokemonImage, isLoadingPage }) => {

    if (isLoadingPage) {
      return  (
        <div className='loading-screen'>
          <img src={logo} className="loading-icon" alt="logo" />
        </div>
      );
    }

    return (
      <div className="screen">
        { pokemonImage ? (
          <img className="pokemonImage" src={pokemonImage} alt="Pokemon" />
          
        ) : (
          <ul className="list">
            {data.map((item, index) => (
              <li className={index === currentIndex ? "select-item" : ""} key={item.id}>
                {item.pokemonName}
              </li>
            ))}
          </ul>
        )}
      </div>
    );
  };

export default Screen;