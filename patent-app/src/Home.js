import logo from './patentLogo.svg';
function Home(){
    return(
        <header className="App-header">
        <img src={logo} className="App-logo" alt="Logo" />
        <h2>
          Patent Check
        </h2>
      </header>
    );
}

export default Home;