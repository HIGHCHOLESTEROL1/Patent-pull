import './SearchBar.css';
import search_icon from './search_icon.svg';

function call() {
    fetch('http://localhost:3001/run-pythonController')
        .then(response => response.text())
        .then(data => {
            console.log('Response from Python: ${data}');
        })
        .catch(error => console.log('Error: ${error}')
        );
}
function call2(){
    fetch('http://localhost:3001/run-pythonScraper')
        .then(response => response.text())
        .then(data => {
            console.log('Response from JavaScript: ${data}');
        })
        .catch(error => console.log('Error: ${error}')
        );
}

function SearchBar(){
    return(
        <div class = 'Bar'>
            <input type = "text" placeholder = "Search" name = "search"/>
            <button class="submit" onClick = {call2}><img src = {search_icon} className = "search-icon"></img></button>
        </div>
    )
}

export default SearchBar;