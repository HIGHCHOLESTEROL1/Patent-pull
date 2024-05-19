import logo from './patentLogo.svg';
import meImg from './me.jpg';
import navigation from './Navigation_bar.js';
import './Navigation_bar.css';
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

function App() {
  return (
    <div className="App">
      <ul>
          <li> <a href = {navigation.home}>Home</a></li>
          <li> <a href = {navigation.github}>Github</a></li>
          <li> <a href = {navigation.about}>About Us</a></li>
          <li> <a href = {navigation.contact}>Contact Us</a></li>
      </ul>
      <header className="App-header">
        <img src={logo} className="App-logo" alt="Logo" />
        <h2>
          Patent Check
        </h2>
      </header>
    </div>
  );
}

export default App;
