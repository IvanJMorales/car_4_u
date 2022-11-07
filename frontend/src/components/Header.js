import React from 'react';
import { Link } from 'react-router-dom';
import "../styles/Header.css"

const Header = () => {
    return (
        <div className='header'>
            <Link to='/'>
                <div className='logo'>
                    <ul>
                        <li className='nav-item'>
                        </li>
                    </ul>
                </div>
            </Link>
            <ul className='navbar'>
                <li className='nav-item'>
                    <Link to='/search-page' className='link'>
                        SEARCH CARS
                    </Link>
                </li>
                <li className='nav-item'>
                    <Link to='/how-it-works' className='link'>
                        HOW IT WORKS
                    </Link>
                </li>
                <li className='nav-item'>
                    <Link to='/right-car-for-you' className='link'>
                        RIGHT CAR FOR YOU?
                    </Link>
                </li>
                
                {/*<li className='nav-item'>
                    <Link to='/logout' className='link'> 
                        LOGOUT
                    </Link>
                </li>
                <li className='nav-item'>
                    <Link to='/login' className='link'>
                        LOGIN
                    </Link>
                </li>*/}
            </ul>
        </div>
    );
};

export default Header;