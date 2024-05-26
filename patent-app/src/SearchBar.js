import './SearchBar.css';
import search_icon from './search_icon.svg';

function call() {
    alert("you clicked a button");
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