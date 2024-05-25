import './SearchBar.css';

function SearchBar(){
    return(
        <div class = 'Bar'>
            <button type="submit"><i class="fa fa-search"></i></button>
            <input type = "text" placeholder = "Search" name = "search"/>
        </div>
    )
}

export default SearchBar;