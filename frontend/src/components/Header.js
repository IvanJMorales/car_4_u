import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import "../styles/Header.css"

import { auth } from "../firebase";
import { onAuthStateChanged } from "firebase/auth";


const Header = () => {

    const [userInfo, setUserInfo] = useState();

    // Observer for user state changed in login.js
    useEffect(() => {
        onAuthStateChanged(auth, (user) => {
            if (user) {
                setUserInfo(user)
                console.log(user.email)
            } else {
                setUserInfo(null)
            }
        })
    }, []);

    if (userInfo) {
        return (
            <div className='header'>
                <div className='logo'>
                    <Link to='/' className='logo-link'>
                        <div className='logo'>
                        </div>
                    </Link>
                </div>
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
    
                    {/*Line in navbar*/}
                    <li>
                        <div class="vl"></div>
                    </li>
                    {/*USER LOGIN*/}
                    <li className='nav-item'>
                        <Link to='/profile' className='link'>
                            Hi, {userInfo.email}
                        </Link>
                    </li>
                </ul>
            </div>
        );
    } else if (userInfo == null) {
        console.log("USER IS NULL")
        return (
            <div className='header'>
                <div className='logo'>
                    <Link to='/' className='logo-link'>
                        <div className='logo'>
                        </div>
                    </Link>
                </div>
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
    
                    {/*Line in navbar*/}
                    <li>
                        <div className="vl"></div>
                    </li>
                    {/*USER LOGIN*/}
                    <li className='nav-item'>
                        <Link to='/login' className='link'>
                            LOGIN
                        </Link>
                    </li>
                </ul>
            </div>
        );
    }
};

export default Header;