import './SearchBar.css';
import search_icon from './search_icon.svg';
import { spawn } from 'node:child_process';

const y = require('child_process');

function call() {
    const myProg = spawn('python', ['./controller/Control.py'])
}

function SearchBar(){
    return(
        <div class = 'Bar'>
            <input type = "text" placeholder = "Search" name = "search"/>
            <button class="submit" onClick = {call}><img src = {search_icon} className = "search-icon"></img></button>
        </div>
    )
}

export default SearchBar;