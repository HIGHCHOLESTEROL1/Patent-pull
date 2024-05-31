import logo from './patentLogo.svg';
import patentImg from './patent.svg';
import SearchBar from './SearchBar.js';
import InfoBox from './InfoBox.js';
function Home(){
    return(
        <header className="App-header">
        <img src={patentImg} className="App-logo" alt="Logo" />
        <h2>
          Patent Check
        </h2>
        <SearchBar></SearchBar>
        <InfoBox></InfoBox>
      </header>
    );
}

export default Home;