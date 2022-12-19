import React from 'react';
import { auth } from '../firebase.js'

import { signOut } from "firebase/auth";
import { useNavigate } from 'react-router';


const UserProfile = () => {
    const navigate = useNavigate();

    const userSignOut = () => signOut(auth).then(() => {
      // Sign-out successful.
      console.log("Signed Out")
      navigate('/')
    }).catch((error) => {
      // An error happened.
    });

    return (
        <div>
            <button onClick={userSignOut}>SIGN OUT</button>
        </div>
    );
};

export default UserProfile;