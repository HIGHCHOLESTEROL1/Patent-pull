import logo from './patentLogo.svg';
import meImg from './me.jpg';
import navigation from './Navigation_bar.js';
import './Navigation_bar.css';
import './App.css';
import Content from './Content.js';
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
      <div className="header">
          <a href = {navigation.home}>Home</a>
          <a href = {navigation.github}target="_blank" rel="noreferrer">Github</a>
          <a href = {navigation.about}>About Us</a>
          <a href = {navigation.contact}>Contact Us</a>
      </div>
      <Content></Content>
    </div>
  );
}

export default App;
