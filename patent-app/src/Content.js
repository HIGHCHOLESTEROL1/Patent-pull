import Home from './Home.js';
import { Route, Routes } from 'react-router-dom';

const Content = () => (
    <Routes>
        <Route path = "/" element = {<Home></Home>}></Route>
    </Routes>
);

export default Content;