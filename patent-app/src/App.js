import logo from './patentLogo.svg';
import meImg from './me.jpg';
import './App.css';
import { Children } from 'react';

const me = {
  name: 'Brian Wang-chen',
  image : meImg,
  imageSize : 60,
};

function MeDisplay(){
  return(
    <img className = "Avatar" src = {me.image} alt = "Avatar photo" 
        style = {{width : me.imageSize, height : me.imageSize}}></img>
  );
}

function AboutUsButton(){
  return(
    <button>
        About us
    </button>
  );
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="Logo" />
        <h2>
          Patent Check
        </h2>
        <p>
          by {me.name}
        </p>
        <MeDisplay/>
        <a href="https://github.com/HIGHCHOLESTEROL1/Patent-pull" target="_blank">GitHub</a>
      </header>
    </div>
  );
}

export default App;
