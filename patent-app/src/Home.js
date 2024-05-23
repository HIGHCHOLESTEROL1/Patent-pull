import logo from './patentLogo.svg';
import patentImg from './patent.svg';
function Home(){
    return(
        <header className="App-header">
        <img src={patentImg} className="App-logo" alt="Logo" />
        <h2>
          Patent Check
        </h2>
      </header>
    );
}

export default Home;