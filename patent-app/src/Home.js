import logo from './patentLogo.svg';
import patentImg from './patent.svg';
import SearchBar from './SearchBar.js';
function Home(){
    return(
        <header className="App-header">
        <img src={patentImg} className="App-logo" alt="Logo" />
        <h2>
          Patent Check
        </h2>
        <SearchBar></SearchBar>
      </header>
    );
}

export default Home;