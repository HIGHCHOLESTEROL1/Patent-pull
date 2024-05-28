import './SearchBar.css';
import search_icon from './search_icon.svg';

function call() {
    fetch('http://localhost:3001/run-python')
        .then(response => response.text())
        .then(data => {
            console.log('Response from Python: ${data}');
        })
        .catch(error => console.log('Error: ${error}')
        );
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